import pandas as pd


soil_df = pd.read_csv("datasets/smart_crop_dataset.csv")


def get_soil_data():

    return {
        "nitrogen": 48,
        "phosphorus": 51,
        "potassium": 61,
        "ph": 7.4
    }