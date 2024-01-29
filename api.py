import requests


API_KEY = "f7921f10dc460b8800faf0500fb1bb48"


class ApiApp:

    def get_weather(self, city_name):

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

        try:
            response = requests.get(url)
            x = response.json()
            print(x)
            if x["cod"] != "404":
                temperature = round(x['main']["temp"] - 273.15) #в терміналі тут помилка
                humidity = x["main"]["humidity"]
                id = str (x["weather"][0]["id"])
                wind_speed = round(x["wind"]["speed"]*18/5)
                # self.root.ids.temperature.text = f"[b]{temperature}[/b]°"
                # self.root.ids.humidity.text = f"{humidity}%"
                # self.root.ids.wind_speed.text = f"{wind_speed} km/h"
                return temperature, humidity, wind_speed
            else:
                print('Місто не знайдено!')
                return None, None, None
        
        except requests.ConnectionError:
            print("Немає з'єднання!")
            return None, None, None
