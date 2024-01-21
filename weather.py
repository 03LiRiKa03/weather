from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwards):
        super(MyGridLayout, self). __init__(**kwards)
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        
class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == "__main__":
    MyApp().run()
