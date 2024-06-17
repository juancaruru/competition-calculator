from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Home(GridLayout):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Hello world'))
        self.add_widget(Button(text='Click me'))