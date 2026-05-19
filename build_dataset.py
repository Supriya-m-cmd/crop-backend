import pandas as pd
from sklearn.preprocessing import LabelEncoder


# =========================================
# LOAD DATASET
# =========================================

df = pd.read_csv("datasets/smart_crop_dataset.csv")


# =========================================
# CREATE LABEL ENCODERS
# =========================================

le_soil = LabelEncoder()

le_season = LabelEncoder()

le_irrigation = LabelEncoder()

le_farming = LabelEncoder()

le_label = LabelEncoder()


# =========================================
# ENCODE FEATURES
# =========================================

df['soil_type'] = le_soil.fit_transform(df['soil_type'])

df['season'] = le_season.fit_transform(df['season'])

df['irrigation_requirement'] = le_irrigation.fit_transform(
    df['irrigation_requirement']
)

df['water_availability'] = le_irrigation.transform(
    df['water_availability']
)

df['farming_method'] = le_farming.fit_transform(
    df['farming_method']
)

df['label'] = le_label.fit_transform(df['label'])


# =========================================
# PRINT EXACT MAPPINGS
# =========================================

print("\n===== SOIL TYPE MAPPING =====")

print(
    dict(
        zip(
            le_soil.classes_,
            le_soil.transform(le_soil.classes_)
        )
    )
)


print("\n===== SEASON MAPPING =====")

print(
    dict(
        zip(
            le_season.classes_,
            le_season.transform(le_season.classes_)
        )
    )
)


print("\n===== IRRIGATION MAPPING =====")

print(
    dict(
        zip(
            le_irrigation.classes_,
            le_irrigation.transform(le_irrigation.classes_)
        )
    )
)


print("\n===== FARMING MAPPING =====")

print(
    dict(
        zip(
            le_farming.classes_,
            le_farming.transform(le_farming.classes_)
        )
    )
)


print("\n===== LABEL MAPPING =====")

print(
    dict(
        zip(
            le_label.classes_,
            le_label.transform(le_label.classes_)
        )
    )
)