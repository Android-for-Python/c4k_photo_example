from kivy.uix.label import Label
from kivy.utils import platform
from textwrap import fill
from applayout.swipescreen import SwipeScreen

class HomeScreen0(SwipeScreen):
    
    def __init__(self, **args):
        super().__init__(**args)
        self.label = Label()
        self.add_widget(self.label)

    def on_size(self, *args):
        if self.width > self.height:
            COLS = 80
        else:
            COLS = 40

        if platform == 'macosx':
            text='HOME SCREEN.\n\n' +\
                fill('Two finger Swipe left or right to see 4 other screens,'+\
                     'showing ' +\
                     'photo, screenshot, and video camera layout examples.',
                     COLS) + '\n\n'
        elif platform == 'win':
            text='HOME SCREEN.\n\n' +\
                fill('Swipe left or right to see 4 other screens, showing ' +\
                     'photo, screenshot, and video camera layout examples.' +\
                     'Swipe is left mouse button with fast mouse move, on ' +\
                     'pad use one and a half taps and fast move or ' +\
                     '(experimental) two finger swipe',
                     COLS) + '\n\n'
        elif platform == 'linux':
            text='HOME SCREEN.\n\n' +\
                fill('Swipe left or right to see 4 other screens, showing ' +\
                     'photo, screenshot, and video camera layout examples.' +\
                     'Swipe is left mouse button with fast move.', 
                     COLS) + '\n\n'
        else:
            text='HOME SCREEN.\n\n' +\
                fill('Swipe left or right to see 4 other screens, showing ' +\
                     'photo, screenshot, and video camera layout examples.',
                     COLS) + '\n\n'
            
        if platform == 'android':
            text+=\
                fill('Rotate the device to see an alternative layout. Use ' +\
                     'the buttons to switch between front and back cameras, '+\
                     'or capture. Touch using pinch/spread gesture for ' +\
                     'zoom, or tap for focus.' ,COLS) + '\n\n' +\
                fill('Photo, screen, and video captures are saved to ' +\
                     'DCIM/<appname>/<date>/<time>, as shown in a toast.',COLS)
        else:
            text+=\
                fill('To simulate the action of rotating a mobile device, ' +\
                     'change the Window size so that the aspect changes ' +\
                     'from landscape to portrait',COLS) + '\n\n' +\
                fill('Photo and screen captures are saved to ' +\
                     './<date>/<time>, as shown in a popup.',COLS) + '\n\n' +\
                fill('Video recording and zoom are on Android only.',COLS)
            pass
            
        self.label.text = text
