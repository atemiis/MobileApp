from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.audio import SoundLoader
import random

#массивы

theme_colors = {
    "white": "#FFD5B3",
    "black": "#241C16",
    "light": "#E5C379",
    "base": "#EBAC49",
    "dark": "#816335",
    "accept": "#5FB753",
    "denied": "#C54040"
}

cards_list = []

#классы
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

def add_widlist(parent, list):
    for widget in list:
        parent.add_widget(widget)

def create_card(instance):
    card = Card()

    rand = random.randint(1,100)
    print('create card with id ' + str(rand) + str(instance.__sizeof__()))

    cardLayout = FloatLayout()
    
    sound = SoundLoader.load('sound.mp3')
    sound.play()

    widget_list = [
        Button(
            size_hint=[convector(500, Window.width), convector(300, Window.height)],
            pos_hint={'center_x': .5, 'center_y': .5},
            background_color = theme_colors["dark"],
            background_normal='',
        ),

        Button(
            size_hint=[convector(100, Window.width), convector(50, Window.height)],
            pos_hint={'center_x': convector(460, Window.width), 'center_y': convector(200, Window.width)},
            background_color = theme_colors["accept"],
            background_normal='',
        ),

        Button(
            size_hint=[convector(100, Window.width), convector(50, Window.height)],
            pos_hint={'center_x': convector(340, Window.width), 'center_y': convector(200, Window.width)},
            background_color = theme_colors["denied"],
            background_normal='',
            outline_color = theme_colors["light"]
        ),

        TextInput(text='Секунды', font_size = 25,
            size_hint=[convector(150, Window.width), convector(50, Window.height)],
            pos_hint={'center_x': convector(435, Window.width), 'center_y': convector(340, Window.width)},
            multiline=False,
        ),

        TextInput(text='Минуты', font_size = 25,
            size_hint=[convector(150, Window.width), convector(50, Window.height)],
            pos_hint={'center_x': convector(270, Window.width), 'center_y': convector(340, Window.width)},
            multiline=False,
        ),

        TextInput(text='Часы', font_size = 25,
            size_hint=[convector(150, Window.width), convector(50, Window.height)],
            pos_hint={'center_x': convector(105, Window.width), 'center_y': convector(340, Window.width)},
            multiline=False,
        ),

        TextInput(text='Имя', font_size = 25,
            size_hint=[convector(480, Window.width), convector(50, Window.height)],
            pos_hint={'center_x': .5, 'center_y': convector(305, Window.width)},
            multiline=False,
        ),

        TextInput(text='Описание', font_size = 25,
            size_hint=[convector(480, Window.width), convector(100, Window.height)],
            pos_hint={'center_x': .5, 'center_y': convector(255, Window.width)},
            multiline=True,
        )
    ]

    add_widlist(cardLayout, widget_list)
    frontLayout.add_widget(cardLayout)


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
            background_color = theme_colors["light"],
            background_disabled_normal = '',
            disabled = True
        )

        plus_button = Button(
            text='+',
            font_size=72,
            size_hint = [convector(50, Window.width), convector(50, Window.height)],
            pos_hint = {'center_x': 0.92, 'center_y': 0.045},
            background_color = theme_colors["dark"],
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
