import requests


def get_weather(city, api_key):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    data = response.json()

    temperature = data['main']['temp']

    humidity = data['main']['humidity']

    rainfall = data.get('rain', {}).get('1h', 0)

    condition = data['weather'][0]['description']

    return {
        "temperature": temperature,
        "humidity": humidity,
        "rainfall": rainfall,
        "condition": condition
    }