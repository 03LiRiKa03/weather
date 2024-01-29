from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
import requests
import ApiApp from api.py



username_helper = '''
MDFloatLayout:
    orientation: 'vertical'
    size_hint: 0.9, 0.9
       
    MDTextField:
        hint_text: "Місто"
        pos_hint: {"center_x": 0.5, "center_y": 0.9}        
        size_hint_x:None        
        width:800         
        multiline: True
        mode: "fill"
        fill_color: 0, 0, 0, .4
        icon_right: "magnify"
        on_text_validate: app.print_text(self.text)
        
    
    Image:
        source: "images//pngimg.com - sun_PNG13434.png"  
        size_hint: .2, .2
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        
    MDLabel:
        id: temperature
        text: "[b]40°[/b]" 
        markup: True
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        halign: "center"
        font_size: "50sp"
    Image:
        source: "images//219816.png"
        pos_hint: {"center_x": 0.37, "center_y": 0.5}
        size_hint: .1, .1
    MDLabel:
        id: humidity
        text: "80%"
        pos_hint: {"center_x": 0.9, "center_y": 0.55}
        font_size: "25sp"
    Image:
        source: "images//7650299.png"
        pos_hint: {"center_x": 0.55, "center_y": 0.5}
        size_hint: .1, .1
    MDLabel:
        id: wind_speed
        text: "80км/год"
        pos_hint: {"center_x": 1.1, "center_y": 0.5}
        font_size: "18sp"
    
    
     
    
'''   
  

    
class MyScreen(MDScreen):
    def __init__(self, **kwargs):
        super(MyScreen, self).__init__(**kwargs)
        self.md_bg_color = (0.29, 1, 1, 1)
    
       
class WeatherApp(MDApp):
    def build(self):
        search = MyScreen()
        username = Builder.load_string(username_helper)
        search.add_widget(username)
        return search
    
    
   
    
          
        

        
    
    
        
    
    
if __name__ == "__main__":
    WeatherApp().run() 
