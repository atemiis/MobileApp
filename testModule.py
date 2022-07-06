from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader
import random

cards_list = []

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
    name = ''
    description = ''
    sound = ''

    #__timer = Timer()


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
    card = Card()

    rand = random.randint(1,100)
    print('create card with id ' + str(rand) + str(instance.__sizeof__()))
    
    sound = SoundLoader.load('sound.mp3')
    sound.play()

    new_card = Button(
        size_hint=[convector(500, Window.width), convector(300, Window.height)],
        pos_hint={'center_x': .5, 'center_y': .5},
        background_color='#949494',
        background_normal='',
    )

    card_accept = Button(
        size_hint=[convector(100, Window.width), convector(50, Window.height)],
        pos_hint={'center_x': convector(460, Window.width), 'center_y': convector(200, Window.width)},
        background_color='#97F170',
        background_normal='',
    )

    sec_input = TextInput(text='Секунды', font_size = 25,
        size_hint=[convector(150, Window.width), convector(50, Window.height)],
        pos_hint={'center_x': convector(435, Window.width), 'center_y': convector(340, Window.width)},
        multiline=False,
    )

    min_input = TextInput(text='Минуты', font_size = 25,
        size_hint=[convector(150, Window.width), convector(50, Window.height)],
        pos_hint={'center_x': convector(270, Window.width), 'center_y': convector(340, Window.width)},
        multiline=False,
    )

    hour_input = TextInput(text='Часы', font_size = 25,
        size_hint=[convector(150, Window.width), convector(50, Window.height)],
        pos_hint={'center_x': convector(105, Window.width), 'center_y': convector(340, Window.width)},
        multiline=False,
    )

    name_input = TextInput(text='Имя', font_size = 25,
        size_hint=[convector(480, Window.width), convector(50, Window.height)],
        pos_hint={'center_x': .5, 'center_y': convector(290, Window.width)},
        multiline=False,
    )

    desc_input = TextInput(text='Описание', font_size = 25,
        size_hint=[convector(480, Window.width), convector(80, Window.height)],
        pos_hint={'center_x': .5, 'center_y': convector(245, Window.width)},
        multiline=True,
    )

    frontLayout.add_widget(new_card)
    frontLayout.add_widget(card_accept)
    frontLayout.add_widget(sec_input)
    frontLayout.add_widget(min_input)
    frontLayout.add_widget(hour_input)
    frontLayout.add_widget(name_input)
    frontLayout.add_widget(desc_input)


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
