from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd

from utils.soil_lookup import get_soil_data

from utils.weather import get_weather

from utils.recommendation import (
    get_top_crop_recommendations
)

from utils.rules import (
    apply_agriculture_rules
)

from utils.ai_suggestions import (
    generate_crop_suggestion
)

from utils.encoder import (

    soil_type_mapping,

    season_mapping,

    irrigation_mapping,

    farming_mapping
)


# =========================================
# FASTAPI APP
# =========================================

app = FastAPI()


# =========================================
# WEATHER API KEY
# =========================================

API_KEY = "fc1d2a35bbf05bc73510408b68667c56"


# =========================================
# INPUT MODEL
# =========================================

class CropInput(BaseModel):

    district: str

    soil_type: str

    season: str

    irrigation_requirement: str

    water_availability: str

    farming_method: str


# =========================================
# HOME ROUTE
# =========================================

@app.get("/")

def home():

    return {

        "message":
        "Kisan Sathi Smart Agriculture API Running"
    }


# =========================================
# RECOMMENDATION ROUTE
# =========================================

@app.post("/recommend")

def recommend_crop(data: CropInput):


    try:

        # =====================================
        # VALIDATE INPUTS
        # =====================================

        if data.soil_type not in soil_type_mapping:

            return {

                "error":
                "Invalid soil type"
            }


        if data.season not in season_mapping:

            return {

                "error":
                "Invalid season"
            }


        if (
            data.irrigation_requirement
            not in irrigation_mapping
        ):

            return {

                "error":
                "Invalid irrigation requirement"
            }


        if (
            data.water_availability
            not in irrigation_mapping
        ):

            return {

                "error":
                "Invalid water availability"
            }


        if (
            data.farming_method
            not in farming_mapping
        ):

            return {

                "error":
                "Invalid farming method"
            }


        # =====================================
        # SOIL LOOKUP
        # =====================================

        soil_data = get_soil_data(
            data.district
        )


        if soil_data is None:

            return {

                "error":
                "District not found in Karnataka soil database"
            }


        # =====================================
        # WEATHER LOOKUP
        # =====================================

        try:

            weather_data = get_weather(

                data.district,

                API_KEY
            )

        except Exception:

            return {

                "error":
                "Weather API failed"
            }


        # =====================================
        # ENCODE INPUTS
        # =====================================

        soil_encoded = soil_type_mapping[
            data.soil_type
        ]


        season_encoded = season_mapping[
            data.season
        ]


        irrigation_encoded = irrigation_mapping[
            data.irrigation_requirement
        ]


        water_encoded = irrigation_mapping[
            data.water_availability
        ]


        farming_encoded = farming_mapping[
            data.farming_method
        ]


        # =====================================
        # CREATE MODEL INPUT
        # =====================================

        input_df = pd.DataFrame([{

            "Nitrogen":
            soil_data['nitrogen'],

            "phosphorus":
            soil_data['phosphorus'],

            "potassium":
            soil_data['potassium'],

            "temperature":
            weather_data['temperature'],

            "humidity":
            weather_data['humidity'],

            "ph":
            soil_data['ph'],

            "rainfall":
            weather_data['rainfall'],

            "soil_type":
            soil_encoded,

            "season":
            season_encoded,

            "irrigation_requirement":
            irrigation_encoded,

            "water_availability":
            water_encoded,

            "farming_method":
            farming_encoded

        }])


        # =====================================
        # ML PREDICTION
        # =====================================

        recommendations = (

            get_top_crop_recommendations(
                input_df
            )
        )


        # =====================================
        # APPLY RULE ENGINE
        # =====================================

        recommendations = (

            apply_agriculture_rules(

                recommendations,

                rainfall=
                weather_data['rainfall'],

                soil_type=
                data.soil_type,

                season=
                data.season
            )
        )


        # =====================================
        # GENERATE AI SUGGESTIONS
        # =====================================

        try:

            ai_suggestion = (
                generate_crop_suggestion(

                    district=data.district,

                    weather=weather_data,

                    soil_data=soil_data,

                    recommendations=
                    recommendations
                )
            )

        except Exception:

            ai_suggestion = (
                "AI suggestion service unavailable"
            )


        # =====================================
        # FINAL RESPONSE
        # =====================================

        return {

            "district":
            data.district,

            "soil_data":
            soil_data,

            "weather":
            weather_data,

            "recommendations":
            recommendations,

            "ai_suggestion":
            ai_suggestion
        }


    except Exception as e:

        return {

            "error":
            str(e)
        }