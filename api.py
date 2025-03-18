import json
import requests

API_KEY = "your_API_KEY"


class WeatherApi:

    def get_weather(self, city_name):

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

        try:
            get_weather = requests.get(url)
            weather_data = json.loads(get_weather.text)
            print(weather_data)
            if weather_data['cod'] != "404":
                temperature = round(weather_data['main']["temp"] - 273.15)
                humidity = weather_data["main"]["humidity"]
                weather_id = str(weather_data["weather"][0]["id"])
                wind_speed = round(weather_data["wind"]["speed"] * 18 / 5)
                return {
                    'temperature': temperature,
                    'humidity': humidity,
                    'weather_id': weather_id,
                    'wind_speed': wind_speed
                }

            else:
                print('Місто не знайдено!')
                return None

        except requests.ConnectionError as error:
            print(f"Немає з'єднання! Помилка: {error}")
            return None
