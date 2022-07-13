from faulthandler import disable
from turtle import pos
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader
import random
import time


#Размер окна
Window.size = (540, 900)
#Размер окна

#переменные
card_open = False
un_id = 0
#переменные

#массивы
theme_colors = {
    "white": "#FFFFFF",
    "black": "#222222",
    "light": "#BAD9F1",
    "base": "#A3CAFF",
    "dark": "#699BE0",
    "accept": "#78E289",
    "denied": "#E27878"
}

cards_list = []
#массивы

#классы
class Timer():
    __time = 0 # храним тут исходное время
    __pause = 0 # остановка времени
    min = 0
    sec = 0
    hour = 0

    def __init__(self, sec, min, hour):
        self.__time = ((hour * 60)*60) + min * 60 + sec # poebat perevod v seki

        self.sec = sec
        self.min = min
        self.hour = hour

    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time

    def stop_timer(self):
        pass

    def start_timer(self):
        pass

    def calculate_time(self, variable):
        time = time.time() # время нажатия на кнопку начала действия таймера

        while(True):
            some = time.time()
            if((some - self.__time) >= time+self.__time): return True

        #Функции для работы приложения
    def add_timer(self, name, desc): # заменится классом
        return [
        Button(
            text = f'{name} : {desc} - {self.hour}:{self.min}:{self.sec}',
            size_hint_y=None, height=40,
            background_color = theme_colors["dark"],
            disabled_color = theme_colors['white'],
            background_disabled_normal='',
            disabled = True
        ), 
        Button(
            text = f'',
            size_hint_y=None, height=40,
            background_color = theme_colors["accept"],
            background_normal='',
            size_hint_x=None,
            width = 40
            ),
        Button(
            text = f'',
            size_hint_y=None, height=40,
            background_color = theme_colors["denied"],
            background_normal='',
            size_hint_x=None,
            width = 40
            )
        ]

class Card():
    __id = 0
    sec = 0
    min = 0
    hour = 0
    name = 'SimpleCard'
    desc = 'Desc of SimpleCard'
    path_sound = 'sound.mp3' # save path sound
    timer = None

    def __init__(self, id, data):
        self.id = id

        try: self.sec = int(data[0])
        except: pass
        try: self.min = int(data[1])
        except: pass
        try: self.hour = int(data[2])
        except: pass

        self.name = str(data[3])
        self.desc = str(data[4])

        self.timer = Timer(self.sec, self.min, self.hour)

    def play_sound(self, volume):
        sound = SoundLoader.load(self.path_sound)
        sound.volume = float(volume)
        sound.play()

#class Timer(Card): 
# Наверное нужен отдельный класс для карточки таймера
        
#классы

#фоны
mainBox = BoxLayout(padding=10)
backLayout = FloatLayout()
frontLayout = FloatLayout()
cardLayout = FloatLayout()
timerLayout = GridLayout(cols=3, spacing=10, size_hint_y=None, padding=[20, 40])
scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height/1.1), pos = [0, Window.height - Window.height/1.1])
scroll.add_widget(timerLayout)
frontLayout.add_widget(scroll)
frontLayout.add_widget(cardLayout)
#фоны

def close_card(self = None):
    global card_open
    if(len(cards_list) >= 5): print([item.id for item in cards_list])

    cardLayout.clear_widgets()
    widget_list.clear()

    card_open = False

def register_data(self):
    card_data = []
    
    for widget in widget_list:
        if(type(widget).__name__ == 'TextInput'):
            card_data.append(widget.text)
    global un_id

    un_id += 1

    card = Card(un_id, card_data) 
    print(f"""
    DEBUG of CARD:
    unic_id: {card.id}
    sec: {card.sec}
    min: {card.min}
    hour: {card.hour}
    name: {card.name}
    desc: {card.desc}
    """)
    card.play_sound(.1)

    cards_list.append(card)

    add_widlist(timerLayout,card.timer.add_timer(card.name, card.desc))

    close_card()

def convector(value, parent_value):
  return value/parent_value

def add_widlist(parent, list):
    for widget in list:
        parent.add_widget(widget)

def create_card(instance):
    global card_open
    if card_open: return

    global widget_list
    widget_list = [
        Button(
            size_hint=[convector(500, Window.width), convector(300, Window.height)],
            pos_hint={'center_x': .5, 'center_y': .5},
            background_color = theme_colors["dark"],
            background_disabled_normal = '',
            disabled = True
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

        TextInput(text='Название', font_size = 25,
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

    widget_list[1].bind(on_press=register_data)
    widget_list[2].bind(on_press=close_card)

    add_widlist(cardLayout, widget_list)

    card_open = True

#Функции для работы приложения

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