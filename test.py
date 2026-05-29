import os

import pandas as pd

from dotenv import load_dotenv

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
# LOAD ENV VARIABLES
# =========================================

load_dotenv()


# =========================================
# GET API KEY FROM .env
# =========================================

API_KEY = os.getenv(
    "OPENWEATHER_API_KEY"
)


# =========================================
# USER INPUT
# =========================================

district = "Hubli"

soil_type = "Black"

season = "Kharif"

irrigation_requirement = "Medium"

water_availability = "Medium"

farming_method = "Traditional"


# =========================================
# GET SOIL DATA
# =========================================

soil_data = get_soil_data(
    district
)


# =========================================
# CHECK SOIL DATA
# =========================================

if soil_data is None:

    print(
        "District not found in soil database"
    )

    exit()


# =========================================
# GET WEATHER DATA
# =========================================

weather_data = get_weather(

    district,

    API_KEY
)


# =========================================
# ENCODE INPUTS
# =========================================

soil_encoded = soil_type_mapping[
    soil_type
]

season_encoded = season_mapping[
    season
]

irrigation_encoded = irrigation_mapping[
    irrigation_requirement
]

water_encoded = irrigation_mapping[
    water_availability
]

farming_encoded = farming_mapping[
    farming_method
]


# =========================================
# CREATE MODEL INPUT
# =========================================

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


# =========================================
# GET ML RECOMMENDATIONS
# =========================================

recommendations = (

    get_top_crop_recommendations(
        input_df
    )
)


# =========================================
# APPLY RULE ENGINE
# =========================================

recommendations = (

    apply_agriculture_rules(

        recommendations,

        rainfall=
        weather_data['rainfall'],

        soil_type=
        soil_type,

        season=
        season
    )
)


# =========================================
# GENERATE AI SUGGESTIONS
# =========================================

ai_suggestion = generate_crop_suggestion(

    district=district,

    weather=weather_data,

    soil_data=soil_data,

    recommendations=recommendations
)


# =========================================
# FINAL OUTPUT
# =========================================

print("\n===================================")

print(" KISAN SATHI AI REPORT ")

print("===================================\n")


# =========================================
# TOP CROPS
# =========================================

print("===== TOP RECOMMENDED CROPS =====\n")


for index, rec in enumerate(

    recommendations,

    start=1
):

    print(

        f"{index}. {rec['crop'].upper()}"
    )

    print(

        f"   Confidence : "
        f"{rec['confidence']}%"
    )

    print("---------------------------------")


# =========================================
# WEATHER INFORMATION
# =========================================

print("\n===== WEATHER INFORMATION =====\n")

print(

    f"Temperature : "
    f"{weather_data['temperature']} °C"
)

print(

    f"Humidity    : "
    f"{weather_data['humidity']} %"
)

print(

    f"Rainfall    : "
    f"{weather_data['rainfall']} mm"
)

print(

    f"Condition   : "
    f"{weather_data['condition']}"
)


# =========================================
# SOIL HEALTH
# =========================================

print("\n===== SOIL HEALTH DATA =====\n")

print(

    f"Nitrogen    : "
    f"{soil_data['nitrogen']}"
)

print(

    f"Phosphorus  : "
    f"{soil_data['phosphorus']}"
)

print(

    f"Potassium   : "
    f"{soil_data['potassium']}"
)

print(

    f"pH Value    : "
    f"{soil_data['ph']}"
)


# =========================================
# AI SUGGESTIONS
# =========================================

print("\n===== AI FARMING SUGGESTIONS =====\n")

print(ai_suggestion)


print("\n===================================")

print(" END OF REPORT ")

print("===================================\n")