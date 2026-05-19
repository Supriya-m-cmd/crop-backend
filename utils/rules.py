# =========================================
# RULE ENGINE
# =========================================

def apply_agriculture_rules(

    recommendations,

    rainfall,

    soil_type,

    season

):

    adjusted = []


    for rec in recommendations:

        crop = rec['crop']

        confidence = rec['confidence']


        # =========================================
        # LOW RAINFALL RULES
        # =========================================

        if rainfall < 20:

            if crop in ['rice', 'jute']:

                confidence -= 20


        # =========================================
        # BLACK SOIL RULE
        # =========================================

        if soil_type == "Black":

            if crop == "cotton":

                confidence += 15


        # =========================================
        # HIGH RAINFALL RULE
        # =========================================

        if rainfall > 100:

            if crop == "rice":

                confidence += 15


        # =========================================
        # KHARIF RULE
        # =========================================

        if season == "Kharif":

            if crop in ['rice', 'cotton', 'maize']:

                confidence += 10


        # =========================================
        # REMOVE NEGATIVE VALUES
        # =========================================

        confidence = max(confidence, 0)


        adjusted.append({

            "crop": crop,

            "confidence": round(confidence, 2)
        })


    # =========================================
    # SORT RESULTS
    # =========================================

    adjusted = sorted(

        adjusted,

        key=lambda x: x['confidence'],

        reverse=True
    )


    # =========================================
    # NORMALIZE CONFIDENCE
    # =========================================

    top_confidence = adjusted[0]['confidence']


    for rec in adjusted:

        normalized = (

            rec['confidence'] / top_confidence
        ) * 100

        rec['confidence'] = round(
            normalized,
            2
        )


    return adjusted[:3]