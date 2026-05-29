from groq import Groq


# =========================================
# GROQ CLIENT
# =========================================
import os
from groq import Groq

api_key = os.environ.get("GROQ_API_KEY")

print("GROQ KEY FOUND:", bool(api_key))

client = Groq(
    api_key=api_key
)
# =========================================
# GENERATE AI SUGGESTIONS
# =========================================

def generate_crop_suggestion(

    district,

    weather,

    soil_data,

    recommendations
):


    top_crop = recommendations[0]['crop']


    prompt = f"""
    You are an expert agricultural AI assistant.

    District: {district}

    Weather:
    Temperature: {weather['temperature']}°C
    Humidity: {weather['humidity']}%
    Rainfall: {weather['rainfall']} mm
    Condition: {weather['condition']}

    Soil Data:
    Nitrogen: {soil_data['nitrogen']}
    Phosphorus: {soil_data['phosphorus']}
    Potassium: {soil_data['potassium']}
    pH: {soil_data['ph']}

    Recommended Crops:
    {recommendations}

    Explain:
    1. Why the top crop is suitable.
    2. Farming tips.
    3. Water advice.
    4. Fertilizer advice.
    5. Weather precautions.

    Keep answer short and farmer friendly.
    """


    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role": "user",

                "content": prompt
            }
        ],

        temperature=0.5,

        max_tokens=200
    )


    return completion.choices[0].message.content