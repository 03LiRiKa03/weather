from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from api import WeatherApi

Builder.load_file('weather.kv')


class MyScreen(MDScreen):
    pass
    
       
class WeatherApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weather_api = WeatherApi()

    def build(self):
        search = MyScreen()
        return search

    def get_weather(self, text):
        weather = self.weather_api.get_weather(text)
        print(weather)

    
if __name__ == "__main__":
    WeatherApp().run() 
