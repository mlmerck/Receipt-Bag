from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

#Imports piechart saved by data.py


#Imports kv file (formatting) for use
Builder.load_file("layout.kv")
#Creates the main screen
class MainScreen(Screen):
    pass

#Creates the receipt screen
class ReceiptScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class S1Individual(Screen):
    pass

class SecondScreen(Screen):
    pass

class S2Individual(Screen):
    pass

class ThirdScreen(Screen):
    pass

class S3Individual(Screen):
    pass

class FourthScreen(Screen):
    pass

#Creates the screen manager, to enable switching between receipt and main screens
sm = ScreenManager()
sm.add_widget(MainScreen(name = 'main'))
sm.add_widget(ReceiptScreen(name = 'receipts'))
sm.add_widget(S1Individual(name = 's1'))
sm.add_widget(FirstScreen(name = 'b1'))
sm.add_widget(S2Individual(name = 's2'))
sm.add_widget(SecondScreen(name = 'b2'))
sm.add_widget(S3Individual(name = 's3'))
sm.add_widget(ThirdScreen(name = 'b3'))
sm.add_widget(FourthScreen(name = 'b4'))

#Defines the app, and names the window
class MyApp(App):
    def build(self):
        self.title = "CompleteReceipt"
        return sm

#Starts the app
if __name__ == '__main__':
    MyApp().run()