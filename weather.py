from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from api import ApiApp

Builder.load_file('weather.kv')


class MyScreen(MDScreen):
    pass
    
       
class WeatherApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weather = ApiApp()

    def build(self):
        search = MyScreen()
        return search

    def get_weather(self, text):
        temperature, humidity, wind_speed = self.weather.get_weather(text)
        print(temperature, humidity, wind_speed)

    
if __name__ == "__main__":
    WeatherApp().run() 
