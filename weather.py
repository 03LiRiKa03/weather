from kivymd.app import MDApp
# from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from api import WeatherApi


# Builder.load_file('weather.kv')


class MyScreen(MDScreen):
    pass


class WeatherApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weather_api = WeatherApi()

    def build(self):
        search = MyScreen()
        return search

    def get_weather(self, city_name):
        weather = self.weather_api.get_weather(city_name)
        self.root.ids.temperature.text = (
            f"[b]{weather['temperature']}[/b]°" if weather is not None else f"[b]No data![/b]"
        )
        self.root.ids.humidity.text = (
            f"{weather['humidity']}%" if weather is not None else "No data!"
        )
        self.root.ids.wind_speed.text = (
            f"{weather['wind_speed']} km/h" if weather is not None else "No data!"
        )




if __name__ == "__main__":
    WeatherApp().run()

    
   
    

    
   
    
          
        

        
    
    
        
    
    
