import pandas as pd

from utils.rules import apply_agriculture_rules

from utils.recommendation import (
    get_top_crop_recommendations
)

from utils.encoder import (

    soil_type_mapping,
    season_mapping,
    irrigation_mapping,
    farming_mapping
)


# =========================================
# HUMAN READABLE INPUTS
# =========================================

soil_type = "Black"

season = "Kharif"

irrigation_requirement = "Medium"

water_availability = "Medium"

farming_method = "Traditional"


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
# CREATE INPUT DATAFRAME
# =========================================

input_df = pd.DataFrame([{

    "Nitrogen": 48,

    "phosphorus": 51,

    "potassium": 61,

    "temperature": 24,

    "humidity": 88,

    "ph": 7.4,

    "rainfall": 3,

    "soil_type": soil_encoded,

    "season": season_encoded,

    "irrigation_requirement": irrigation_encoded,

    "water_availability": water_encoded,

    "farming_method": farming_encoded

}])


# =========================================
# GET ML RECOMMENDATIONS
# =========================================

recommendations = get_top_crop_recommendations(
    input_df
)


# =========================================
# APPLY RULE ENGINE
# =========================================

recommendations = apply_agriculture_rules(

    recommendations,

    rainfall=3,

    soil_type=soil_type,

    season=season
)


# =========================================
# PRINT RESULTS
# =========================================

print("\n===== TOP CROP RECOMMENDATIONS =====\n")


for index, rec in enumerate(

    recommendations,

    start=1
):

    print(

        f"{index}. {rec['crop']} "
        f"| Confidence: {rec['confidence']}%"
    )