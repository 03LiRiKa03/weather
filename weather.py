from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

textinput = TextInput(text='Hello world')
def on_enter(instance, value):
    print('User pressed enter in', instance)

textinput = TextInput(text='Hello world', multiline=False)
textinput.bind(on_text_validate=on_enter)
textinput = TextInput(focus=True)


    
if __name__ == "__main__":
    App().run()