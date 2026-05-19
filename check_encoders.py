import pandas as pd


df = pd.read_csv("datasets/smart_crop_dataset.csv")


print("\n===== UNIQUE SOIL TYPES =====")
print(df['soil_type'].unique())

print("\n===== UNIQUE SEASONS =====")
print(df['season'].unique())

print("\n===== UNIQUE IRRIGATION =====")
print(df['irrigation_requirement'].unique())

print("\n===== UNIQUE FARMING =====")
print(df['farming_method'].unique())

print("\n===== UNIQUE LABELS =====")
print(df['label'].unique())