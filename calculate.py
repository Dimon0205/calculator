import math
from decimal import getcontext

from kivy.config import Config
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout

getcontext().prec = 5
Window.size = (480, 680)

Config.set('kivy', 'keyboard_mode', 'systemanddock')


def get_calculate(weight, axes, axes_35, axes_45, axes_50, axes_55, axes_60, axes_65, axes_70, axes_75, axes_80,
                  axes_85, axes_90, axes_10, axes_11, axes_12, axes_13):
    axes_list = []
    press_coef = [.55, .33, .32, .31, .3]
    parking_axes = math.ceil(weight * 6 / 1000)
    if parking_axes % 4:
        parking_axes += 4 - parking_axes % 4
    parking_axes = str(parking_axes)
    press_35 = str(math.ceil(axes_35 * 35 / 10))
    press_45 = str(math.ceil(axes_45 * 45 / 10))
    press_50 = str(math.ceil(axes_50 * 50 / 10))
    press_55 = str(math.ceil(axes_55 * 55 / 10))
    press_60 = str(math.ceil(axes_60 * 60 / 10))
    press_65 = str(math.ceil(axes_65 * 65 / 10))
    press_70 = str(math.ceil(axes_70 * 70 / 10))
    press_75 = str(math.ceil(axes_75 * 75 / 10))
    press_80 = str(math.ceil(axes_80 * 80 / 10))
    press_85 = str(math.ceil(axes_85 * 85 / 10))
    press_90 = str(math.ceil(axes_90 * 90 / 10))
    press_10 = str(math.ceil(axes_10 * 100 / 10))
    press_11 = str(math.ceil(axes_11 * 110 / 10))
    press_12 = str(math.ceil(axes_12 * 120 / 10))
    press_13 = str(math.ceil(axes_13 * 130 / 10))

    all_axes = str(axes)

    return {'parking_axes': parking_axes, 'all_axes': all_axes, 'press_10': press_10,
            'press_11': press_11, 'press_12': press_12, 'press_13': press_13,
            'press_35': press_35, 'press_45': press_45, 'press_50': press_50,
            'press_55': press_55, 'press_60': press_60, 'press_65': press_65,
            'press_70': press_70, 'press_75': press_75, 'press_80': press_80,
            'press_85': press_85, 'press_90': press_90}


class Container(MDGridLayout):

    def data_input(self):
        try:
            weight = int(self.weight_text.text)
            axes = int(self.axes_text.text)
            axes_35 = int(self.axes_35.text)
            axes_45 = int(self.axes_45.text)
            axes_50 = int(self.axes_50.text)
            axes_55 = int(self.axes_55.text)
            axes_60 = int(self.axes_60.text)
            axes_65 = int(self.axes_65.text)
            axes_70 = int(self.axes_70.text)
            axes_75 = int(self.axes_75.text)
            axes_80 = int(self.axes_80.text)
            axes_85 = int(self.axes_85.text)
            axes_90 = int(self.axes_90.text)
            axes_10 = int(self.axes_10.text)
            axes_11 = int(self.axes_11.text)
            axes_12 = int(self.axes_12.text)
            axes_13 = int(self.axes_13.text)
        except:
            weight = 0
            axes = 0
            axes_35 = 0
            axes_45 = 0
            axes_50 = 0
            axes_55 = 0
            axes_60 = 0
            axes_65 = 0
            axes_70 = 0
            axes_75 = 0
            axes_80 = 0
            axes_85 = 0
            axes_90 = 0
            axes_10 = 0
            axes_11 = 0
            axes_12 = 0
            axes_13 = 0

        calculate = get_calculate(
            weight,
            axes,
            axes_35,
            axes_45,
            axes_50,
            axes_55,
            axes_60,
            axes_65,
            axes_70,
            axes_75,
            axes_80,
            axes_85,
            axes_90,
            axes_10,
            axes_11,
            axes_12,
            axes_13
        )

        self.parking_axes.text = calculate.get('parking_axes')
        self.all_axes.text = calculate.get('all_axes')
        self.press_10.text = calculate.get('press_10')
        self.press_11.text = calculate.get('press_11')
        self.press_12.text = calculate.get('press_12')
        self.press_13.text = calculate.get('press_13')
        self.press_35.text = calculate.get('press_35')
        self.press_45.text = calculate.get('press_45')
        self.press_50.text = calculate.get('press_50')
        self.press_55.text = calculate.get('press_55')
        self.press_60.text = calculate.get('press_60')
        self.press_65.text = calculate.get('press_65')
        self.press_70.text = calculate.get('press_70')
        self.press_75.text = calculate.get('press_75')
        self.press_80.text = calculate.get('press_80')
        self.press_85.text = calculate.get('press_85')
        self.press_90.text = calculate.get('press_90')


class CalculateApp(MDApp):
    def build(self):
        return Container()


if __name__ == '__main__':
    CalculateApp().run()
