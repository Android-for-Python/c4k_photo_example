from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from camera4kivy import Preview
from applayout.swipescreen import SwipeScreen
from applayout.toast import Toast

SS3 = """
<Screenshot3>:
    screen_preview: screen_layout.ids.preview
    ScreenLayout3:
        id:screen_layout
"""

class ScreenShot3(SwipeScreen):
    screen_preview = ObjectProperty(None)

    def __init__(self, **args):
        Builder.load_string(SS3)
        super().__init__(**args)    

    def on_enter(self):
        self.screen_preview.connect_camera(filepath_callback= self.capture_path)

    def on_pre_leave(self):
        self.screen_preview.disconnect_camera()
    
    def capture_path(self,file_path):
        Toast().show(file_path)

SL3 = """
<ScreenLayout3>:
    Background3:
        id: pad_end
    Preview:
        id: preview
        letterbox_color: 'orchid'
    ButtonsLayout3:
        id: buttons

<Background3@Label>:
    color: 'orchid'
    canvas:
        Color:
            rgba : self.color
        Rectangle:
            pos: self.pos
            size: self.size
"""

class ScreenLayout3(BoxLayout):

    def __init__(self, **args):
        Builder.load_string(SL3)
        super().__init__(**args)    

    def on_size(self, layout, size):
        if Window.width < Window.height:
            self.orientation = 'vertical'
            self.ids.preview.size_hint = (1, .8)
            self.ids.buttons.size_hint = (1, .2)
            self.ids.pad_end.size_hint = (1, .1)
        else:
            self.orientation = 'horizontal'
            self.ids.preview.size_hint = (.8, 1)
            self.ids.buttons.size_hint = (.2, 1)
            self.ids.pad_end.size_hint = (.1, 1)

BL3 = """
<ButtonsLayout3>:
    normal:
    down:
    Background3:
    Button:
        id:other
        on_press: root.select_camera('toggle')
        height: self.width
        width: self.height
        background_normal: 'icons/camera-flip-outline.png'
        background_down:   'icons/camera-flip-outline.png'
    Button:
        id:screen
        on_press: root.screenshot()
        height: self.width
        width: self.height
        background_normal: root.normal
        background_down: root.down
"""

class ButtonsLayout3(RelativeLayout):

    normal = StringProperty()
    down = StringProperty()

    def __init__(self, **kwargs):
        Builder.load_string(BL3)
        super().__init__(**kwargs)
        if platform == 'android':
            self.normal = 'icons/cellphone-screenshot_white.png'
            self.down   = 'icons/cellphone-screenshot_red.png'
        else:
            self.normal = 'icons/monitor-screenshot_white.png'
            self.down   = 'icons/monitor-screenshot_red.png'
  
    def on_size(self, layout, size):
        if platform == 'android': 
            self.ids.screen.min_state_time = 0.3 
        else:
            self.ids.screen.min_state_time = 1
        if Window.width < Window.height:
            self.ids.other.pos_hint  = {'center_x':.3,'center_y':.5}
            self.ids.other.size_hint = (.2, None)
            self.ids.screen.pos_hint  = {'center_x':.7,'center_y':.5}
            self.ids.screen.size_hint = (.2, None)
        else:
            self.ids.other.pos_hint  = {'center_x':.5,'center_y':.7}
            self.ids.other.size_hint = (None, .2)
            self.ids.screen.pos_hint  = {'center_x':.5,'center_y':.3}
            self.ids.screen.size_hint = (None, .2)

    def screenshot(self):
        self.parent.ids.preview.capture_screenshot()

    def select_camera(self, facing):
        self.parent.ids.preview.select_camera(facing)



            
