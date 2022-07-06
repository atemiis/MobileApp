from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
import random

#classes
class Timer():
    __time = 0 # храним тут исходное время

    def __init__(self, time):
        self.__time = time

    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time

    def calculate_time(self):
        pass



class Card():
    name = 'artem'
    description = ''
    sound = ''

    __timer = Timer()


#фоны
mainBox = BoxLayout(padding=10)
backLayout = FloatLayout()
frontLayout = FloatLayout()
#фоны

#Размер окна
Window.size = (540, 900)
#Размер окна

#Функции для работы приложения
def someone(self):
    print("test")

def convector(value, parent_value):
  return value/parent_value

def create_card(instance):
    rand = random.randint(1,100)
    print('create card with id ' + str(rand) + str(instance.__sizeof__()))

    new_card = Button(
        text='+',
        font_size=72,
        size_hint=[convector(400, Window.width), convector(600, Window.height)],
        pos_hint={'center_x': .5, 'center_y': .5},
        background_color='#949494',
        background_normal='',
    )

    frontLayout.add_widget(new_card)


#Функции для работы приложения


#Массивы цветов
light_gray = [217,217,217,1]
#Массивы цветов

class MainApp(App):

    def build(self):
        background = Image(
            source='',
            allow_stretch = True,
            keep_ratio = False
        )

        back = Button(
            background_color = '#D9D9D9',
            background_disabled_normal = '',
            disabled = True
        )

        plus_button = Button(
            text='+',
            font_size=72,
            size_hint = [convector(50, Window.width), convector(50, Window.height)],
            pos_hint = {'center_x': 0.92, 'center_y': 0.045},
            background_color='#949494',
            background_normal='',
        )

        plus_button.bind(on_press=create_card)

        frontLayout.add_widget(plus_button)
        backLayout.add_widget(background)
        mainBox.add_widget(back)
        backLayout.add_widget(mainBox)
        backLayout.add_widget(frontLayout)

        return backLayout

if __name__ == '__main__':
    app = MainApp()
    app.run()
