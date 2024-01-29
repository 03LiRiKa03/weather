from kivy.uix.button import Button 
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen


class MyScreen():
    pass
    
class MyScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MyScreen, self).__init__(**kwargs)
        self.md_bg_color = (0.29, 1, 1, 1)
    
       
class WeatherApp(MDApp):
    def build(self):
        search = MyScreen()
        return search
    
    def print_text(self, text):
        print(text)
        


    
        
    
    
        
    
    
if __name__ == "__main__":
    WeatherApp().run() 
