from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

username_helper = '''
Image:
    source: "C:\\Users\\User\\Desktop\\2\\kivy_venv\\sun.JPG" #тут йому щось не нрав
    size_hint: .1, .1
    pos_hint: {"center_x": .5, "center_y": .95}Image:
    source: "C:\\Users\\User\\Desktop\\2\\kivy_venv\\sun.JPG"
    size_hint: .1, .1
    pos_hint: {"center_x": .5, "center_y": .95}
    
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
    
    def print_text(self, text):
        on_release: MDApp.print_text("чайнік")
        print(text)


    
    
        
    
    
if __name__ == "__main__":
    WeatherApp().run() 
