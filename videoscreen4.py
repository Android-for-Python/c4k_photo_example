from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from camera4kivy import Preview
from swipescreen import SwipeScreen
from toast import Toast

class VideoScreen4(SwipeScreen):
    video_preview = ObjectProperty(None)
    video_button = ObjectProperty(None)

    def on_enter(self):
        self.video_preview.connect_camera(filepath_callback= self.capture_path)

    def on_pre_leave(self):
        self.video_preview.disconnect_camera()

    def capture_path(self,file_path):
        self.video_button.state = 'normal' 
        Toast().show(file_path)

class ButtonsLayout4(RelativeLayout):

    normal = StringProperty()
    down = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if platform == 'android':
            self.normal = 'icons/video_white.png'
            self.down   = 'icons/video_red.png' 
        else:
            self.normal = 'icons/video-off.png'
            self.down   = 'icons/video-off.png'

    def on_size(self, layout, size):
        if Window.width < Window.height:
            self.ids.other.pos_hint  = {'center_x':.3,'center_y':.5}
            self.ids.other.size_hint = (.2, None)
            self.ids.video.pos_hint  = {'center_x':.7,'center_y':.5}
            self.ids.video.size_hint = (.24, None)
        else:
            self.ids.other.pos_hint  = {'center_x':.5,'center_y':.7}
            self.ids.other.size_hint = (None, .2)
            self.ids.video.pos_hint  = {'center_x':.5,'center_y':.3}
            self.ids.video.size_hint = (None, .24)

    def video_action(self, state):
        if platform == 'android':
            if state == 'down':
                self.parent.ids.preview.capture_video()
            else:
                self.parent.ids.preview.stop_capture_video()

    def select_camera(self, facing):
        self.parent.ids.preview.select_camera(facing)

class VideoLayout4(BoxLayout):

    def on_size(self, layout, size):
        if Window.width < Window.height:
            self.orientation = 'vertical'
            self.ids.preview.size_hint = (1, .7)
            self.ids.buttons.size_hint = (1, .2)
            self.ids.pad_end.size_hint = (1, .1)
        else:
            self.orientation = 'horizontal'
            self.ids.preview.size_hint = (.7, 1)
            self.ids.buttons.size_hint = (.2, 1)
            self.ids.pad_end.size_hint = (.1, 1)

Builder.load_string("""
<VideoScreen4>:
    video_preview: video_layout.ids.preview
    video_button: video_layout.video_button
    VideoLayout4:
        id:video_layout

<VideoLayout4>:
    video_button: buttons.ids.video
    Background4:
        id: pad_end
    Preview:
        id: preview
        aspect_ratio: '16:9'
        letterbox_color: 'darkseagreen'
    ButtonsLayout4:
        id: buttons

<Background4@Label>:
    color: 'darkseagreen'
    canvas:
        Color: 
            rgba: self.color
        Rectangle:
            pos: self.pos
            size: self.size

<ButtonsLayout4>:
    normal:
    down:
    Background4:
    Button:
        id:other
        on_press: root.select_camera('toggle')
        height: self.width
        width: self.height
        background_normal: 'icons/camera-flip-outline.png'
        background_down:   'icons/camera-flip-outline.png'
    ToggleButton:      
        id:video
        on_press: root.video_action(self.state)
        height: self.width
        width: self.height
        background_normal: root.normal
        background_down: root.down
""")
    

