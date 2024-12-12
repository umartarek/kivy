from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="Hello, Kivy!", on_press=self.change_text)

    def change_text(self, instance):
        instance.text = "You clicked me!"

if __name__ == '__main__':
    MyApp().run()
