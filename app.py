import kivy
kivy.require('2.3.0')

from kivy.app import App

from views.home import Home


class MyApp(App):
    def build(self):
        return Home()
    
if __name__ == '__main__':
    MyApp().run()
