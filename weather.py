from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Container(GridLayout):
    pass


class WeatherApp(App):
    def build(self):
        container = Container()
        return container
        
if __name__ == "__main__":
    WeatherApp().run()