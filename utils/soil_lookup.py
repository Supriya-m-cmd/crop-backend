import pandas as pd


# =========================================
# LOAD SOIL DATASET
# =========================================

soil_df = pd.read_csv(
    "datasets/Soil data.csv"
)


# =========================================
# KARNATAKA DISTRICT ALIASES
# =========================================

district_aliases = {

    # =====================================
    # BENGALURU
    # =====================================

    "bangalore": "Bengaluru urban",
    "bengaluru": "Bengaluru urban",
    "blr": "Bengaluru urban",

    "bangalore rural": "Bangalore Rural",
    "bengaluru rural": "Bangalore Rural",


    # =====================================
    # HUBBALLI - DHARWAD
    # =====================================

    "hubli": "Dharwad",
    "hubballi": "Dharwad",
    "hubli dharwad": "Dharwad",


    # =====================================
    # MYSURU
    # =====================================

    "mysore": "Mysuru",


    # =====================================
    # MANGALURU
    # =====================================

    "mangalore": "Dakshina Kannada",
    "mangaluru": "Dakshina Kannada",


    # =====================================
    # BELAGAVI
    # =====================================

    "belgaum": "Belagavi",


    # =====================================
    # KALABURAGI
    # =====================================

    "gulbarga": "Kalaburagi",


    # =====================================
    # BALLARI
    # =====================================

    "bellary": "Ballari",
    "hospet": "Ballari",
    "hospet": "Ballari",


    # =====================================
    # SHIVAMOGGA
    # =====================================

    "shimoga": "Shivamogga",


    # =====================================
    # CHIKKAMAGALURU
    # =====================================

    "chikmagalur": "Chikkamagaluru",


    # =====================================
    # VIJAYAPURA
    # =====================================

    "bijapur": "Vijayapura",


    # =====================================
    # UTTARA KANNADA
    # =====================================

    "karwar": "Uttara Kannada",


    # =====================================
    # KODAGU
    # =====================================

    "madikeri": "Kodagu",
    "coorg": "Kodagu",


    # =====================================
    # RAMANAGARA
    # =====================================

    "ramnagar": "Ramangara",
    "ramanagara": "Ramangara",


    # =====================================
    # YADGIR
    # =====================================

    "yadagiri": "Yadgir",


    # =====================================
    # CHIKKABALLAPURA
    # =====================================

    "chikkaballapur": "Chikkaballapura",


    # =====================================
    # TUMAKURU
    # =====================================

    "tumkur": "Tumakuru",


    # =====================================
    # BAGALKOTE
    # =====================================

    "bagalkot": "Bagalakote",


    # =====================================
    # DAVANAGERE
    # =====================================

    "davangere": "Davanagere",


    # =====================================
    # VIJAYANAGARA
    # =====================================

    "vijayanagar": "Vijayanagar",


    # =====================================
    # CHAMARAJANAGAR
    # =====================================

    "chamarajnagar": "Chamarajanagar"
}

# =========================================
# GET SOIL DATA
# =========================================

def get_soil_data(district):


    district = district.strip().lower()


    # =====================================
    # APPLY ALIAS
    # =====================================

    if district in district_aliases:

        district = district_aliases[district]


    # =====================================
    # FILTER DISTRICT
    # =====================================

    district_data = soil_df[

        soil_df['District'].str.lower()

        ==

        district.lower()
    ]


    # =====================================
    # DISTRICT NOT FOUND
    # =====================================

    if district_data.empty:

        return None


    # =====================================
    # AVERAGE SOIL VALUES
    # =====================================

    nitrogen = district_data[
        'Nitrogen Value'
    ].mean()


    phosphorus = district_data[
        'Phosphorous value'
    ].mean()


    potassium = district_data[
        'Potassium value'
    ].mean()


    ph = district_data[
        'pH'
    ].mean()


    # =====================================
    # RETURN SOIL PROFILE
    # =====================================

    return {

        "nitrogen":
        round(float(nitrogen), 2),

        "phosphorus":
        round(float(phosphorus), 2),

        "potassium":
        round(float(potassium), 2),

        "ph":
        round(float(ph), 2)
    }