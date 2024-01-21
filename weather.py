from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class WeatherApp(TextInput):
    pass

class MyApp(App):
    def build(self):
        
        return WeatherApp
        
          

    
    
    
if __name__ == "__main__":
    MyApp().run()