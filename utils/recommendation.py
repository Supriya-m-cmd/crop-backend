import pickle

from utils.encoder import crop_mapping


# =========================================
# LOAD MODEL
# =========================================

model = pickle.load(
    open("models/crop_recommendation_model.pkl", "rb")
)


# =========================================
# GET TOP RECOMMENDATIONS
# =========================================

def get_top_crop_recommendations(input_data):

    probabilities = model.predict_proba(
        input_data
    )[0]

    crop_classes = model.classes_

    results = []

    for crop, prob in zip(
        crop_classes,
        probabilities
    ):

        results.append({

            "crop": crop_mapping.get(
                int(crop),
                "Unknown"
            ),

            "confidence": round(
                float(prob * 100),
                2
            )
        })

    results = sorted(

        results,

        key=lambda x: x['confidence'],

        reverse=True
    )

    return results[:3]