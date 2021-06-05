from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from decimal import Decimal, getcontext
import math
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SwapTransition
from kivy.properties import NumericProperty

getcontext().prec = 5
Window.size = (480, 680)

from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')


def get_calculate(w):
    parking_axes = str(math.ceil(float(w) * 0.006))
    # if parking_axes % 4:
    #     parking_axes += 4 - parking_axes % 4
    # parking_axes_str = str(parking_axes)
    weight = Container.check.__getattribute__('weight')
    return {'parking_axes': parking_axes, 'weight': weight}


class CalcScreen(Screen):
    def __init__(self, weight, text_input, **kwargs):
        super().__init__(**kwargs)
        self.weight = weight
        self.text_input.text = text_input

    def data_input(self):
        self.weight = int(self.text_input.text)
        return self.weight


class Container(GridLayout, CalcScreen):
    def __init__(self, weight, text_input, **kwargs):
        super().__init__(weight, text_input, **kwargs)
        self.weight = weight
        self.text_input.text = text_input

    def check(self):
        try:
            self.weight = CalcScreen.data_input(self)
        except:
            self.weight = 0
        calculate = get_calculate(self.weight)
        self.parking_axes.text = calculate.get('parking_axes')
        self.weight = calculate.get('weight')


class MyApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Container(name='data_out'))
        sm.add_widget(CalcScreen(name='data_in'))
        sm.current = 'data_out'
        return sm


if __name__ == '__main__':
    MyApp().run()
