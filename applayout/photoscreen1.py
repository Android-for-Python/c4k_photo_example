from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from camera4kivy import Preview
from applayout.swipescreen import SwipeScreen
from applayout.toast import Toast

PS1 = """
<PhotoScreen1>:
    photo_preview: photo_layout.ids.preview
    PhotoLayout1:
        id:photo_layout
"""

class PhotoScreen1(SwipeScreen):
    photo_preview = ObjectProperty(None)

    def __init__(self, **args):
        Builder.load_string(PS1)
        super().__init__(**args)
    
    def on_enter(self):
        self.photo_preview.connect_camera(filepath_callback= self.capture_path)

    def on_pre_leave(self):
        self.photo_preview.disconnect_camera()
    
    def capture_path(self,file_path):
        Toast().show(file_path)

PL1 = """
<PhotoLayout1>:
    Background1:
        id: pad_end
    Preview:
        id: preview
        letterbox_color: .8, .3, 1, .5
    ButtonsLayout1:
        id: buttons

<Background1@Label>:
    canvas:
        Color: 
            rgba: .8, .3, 1, .5
        Rectangle:
            pos: self.pos
            size: self.size
"""

class PhotoLayout1(BoxLayout):

    def __init__(self, **args):
        Builder.load_string(PL1)
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


BL1 = """
<ButtonsLayout1>:
    Background1:
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

class ButtonsLayout1(RelativeLayout):
    
    def __init__(self, **args):
        Builder.load_string(BL1)
        super().__init__(**args)
    
    def on_size(self, layout, size):
        if platform in ['android', 'ios']: 
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
            self.ids.flash.background_normal ='icons/flash.png'
            self.ids.flash.background_down   ='icons/flash.png'
        elif icon == 'auto':
            self.ids.flash.background_normal ='icons/flash-auto.png'
            self.ids.flash.background_down   ='icons/flash-auto.png'
        else:
            self.ids.flash.background_normal ='icons/flash-off.png'
            self.ids.flash.background_down   ='icons/flash-off.png'

    def select_camera(self, facing):
        self.parent.ids.preview.select_camera(facing)


