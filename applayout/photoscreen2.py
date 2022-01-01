from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from camera4kivy import Preview
from applayout.swipescreen import SwipeScreen
from applayout.toast import Toast

PS2 = """
<PhotoScreen2>:
    photo_preview: photo_layout.ids.preview
    PhotoLayout2:
        id:photo_layout
"""

class PhotoScreen2(SwipeScreen):
    photo_preview = ObjectProperty(None)

    def __init__(self, **args):
        Builder.load_string(PS2)
        super().__init__(**args)
    
    def on_enter(self):
        self.photo_preview.connect_camera(filepath_callback= self.capture_path)

    def on_pre_leave(self):
        self.photo_preview.disconnect_camera()
    
    def capture_path(self,file_path):
        Toast().show(file_path)

PL2 = """
<PhotoLayout2>:
    Background2:
        id: pad_end
    Preview:
        id: preview
        orientation: 'opposite'
        letterbox_color: 1, .3, .8, .5
    ButtonsLayout2:
        id: buttons

<Background2@Label>:
    canvas:
        Color: 
            rgba: 1, .3, .8, .5
        Rectangle:
            pos: self.pos
            size: self.size
"""

class PhotoLayout2(BoxLayout):

    def __init__(self, **args):
        Builder.load_string(PL2)
        super().__init__(**args)    

    def on_size(self, layout, size):
        if Window.width < Window.height:
            self.orientation = 'vertical'
            self.ids.preview.size_hint  = (1, .3)
            self.ids.buttons.size_hint  = (1, .2)
            self.ids.pad_end.size_hint  = (1, .1)  
        else:
            self.orientation = 'horizontal'
            self.ids.preview.size_hint = (.3, 1)
            self.ids.buttons.size_hint = (.2, 1)
            self.ids.pad_end.size_hint = (.1, 1)

BL2 = """
<ButtonsLayout2>:
    Background2:
    Button:
        id:other
        on_press: root.select_camera('toggle')
        height: self.width
        width: self.height
        background_normal: 'icons/camera-flip-outline.png'
        background_down:   'icons/camera-flip-outline.png'
    Button:
        id:flash
        on_press: root.flash()
        height: self.width
        width: self.height
        background_normal: 'icons/flash-off.png'
        background_down:   'icons/flash-off.png'
    Button:
        id:photo
        on_press: root.photo()
        height: self.width
        width: self.height
        background_normal: 'icons/camera_white.png'
        background_down:   'icons/camera_red.png'
"""

class ButtonsLayout2(RelativeLayout):

    def __init__(self, **args):
        Builder.load_string(BL2)
        super().__init__(**args)    
    
    def on_size(self, layout, size):
        if platform == 'android': 
            self.ids.photo.min_state_time = 0.3 
        else:
            self.ids.photo.min_state_time = 1
        
        if Window.width < Window.height:
            self.ids.other.pos_hint  = {'center_x':.2,'center_y':.5}
            self.ids.other.size_hint = (.2, None)
            self.ids.photo.pos_hint  = {'center_x':.5,'center_y':.5}
            self.ids.photo.size_hint = (.24, None)
            self.ids.flash.pos_hint  = {'center_x':.8,'center_y':.5}
            self.ids.flash.size_hint = (.15, None)
        else:
            self.ids.other.pos_hint  = {'center_x':.5,'center_y':.8}
            self.ids.other.size_hint = (None, .2)
            self.ids.photo.pos_hint  = {'center_x':.5,'center_y':.5}
            self.ids.photo.size_hint = (None, .24)
            self.ids.flash.pos_hint  = {'center_x':.5,'center_y':.2}
            self.ids.flash.size_hint = (None, .15)

    def photo(self):
        self.parent.ids.preview.capture_photo()

    def flash(self):
        icon = self.parent.ids.preview.flash()
        if icon == 'on':
            self.ids.flash.background_normal= 'icons/flash.png'
            self.ids.flash.background_down  = 'icons/flash.png'
        elif icon == 'auto':
            self.ids.flash.background_normal= 'icons/flash-auto.png'
            self.ids.flash.background_down  = 'icons/flash-auto.png'
        else:
            self.ids.flash.background_normal= 'icons/flash-off.png'
            self.ids.flash.background_down  = 'icons/flash-off.png'

    def select_camera(self, facing):
        self.parent.ids.preview.select_camera(facing)


            
