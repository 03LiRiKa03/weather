from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder


username_helper = '''
<MyWidget>:
    canvas.before:
        Color:
            rgb(70, 176, 246) 
        Rectangle:
            pos: self.pos
            size: self.size
            
MDTextField:
    hint_text: "Місто"
    pos_hint: {"center_x": 0.5, "center_y": 0.9}        
    size_hint_x:None        
    width:800         
    multiline: True
    mode: "fill"
    fill_color: 0, 0, 0, .4 
    
'''      

class WeatherApp(MDApp):
    def build(self):
        search = Screen()
        username = Builder.load_string(username_helper)
        search.add_widget(username)
        return search
    
    
    
    
        
    
    
if __name__ == "__main__":
    WeatherApp().run() 