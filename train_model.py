import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# Load dataset
df = pd.read_csv("datasets/smart_crop_dataset.csv")


# Features and Labels
X = df.drop("label", axis=1)

y = df["label"]


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)


# Save Model
pickle.dump(
    model,
    open("models/crop_recommendation_model.pkl", "wb")
)

print("Model Trained and Saved Successfully")