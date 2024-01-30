import json
import requests


API_KEY = "f7921f10dc460b8800faf0500fb1bb48"


class WeatherApi:

    def get_weather(self, city_name):

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

        try:
            get_weather = requests.get(url)
            status = get_weather.status_code
            weather_data = json.loads(get_weather.text)

            if status != "404":
                temperature = round(weather_data['main']["temp"] - 273.15)  # в терміналі тут помилка
                humidity = weather_data["main"]["humidity"]
                weather_id = str(weather_data["weather"][0]["id"])
                wind_speed = round(weather_data["wind"]["speed"]*18/5)
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
