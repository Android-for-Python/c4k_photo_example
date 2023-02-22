from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform
from camera4kivy import Preview, CameraProviderInfo
from applayout.swipescreen import SwipeScreen
from applayout.toast import Toast

VS5 = """
<VideoScreen5>:
    video_preview: video_layout.ids.preview
    video_button: video_layout.video_button
    VideoLayout5:
        id:video_layout
"""

class VideoScreen5(SwipeScreen):
    video_preview = ObjectProperty(None)
    video_button = ObjectProperty(None)

    def __init__(self, **args):
        Builder.load_string(VS5)
        super().__init__(**args)        

    def on_enter(self):
        self.video_preview.connect_camera(filepath_callback= self.capture_path,
                                          sensor_rotation = 90)

    def on_pre_leave(self):
        self.video_preview.disconnect_camera()

    def capture_path(self,file_path):
        # Reset button in cases where camera terminates video recording.
        self.video_button.state = 'normal' 
        Toast().show(file_path)

VL5 = """
<VideoLayout5>:
    video_button: buttons.ids.video
    Background5:
        id: pad_end
    Preview:
        id: preview
        orientation: 'portrait'
        letterbox_color: 'darkgrey'
    ButtonsLayout5:
        id: buttons

<Background5@Label>:
    color: 'darkgrey'
    canvas:
        Color: 
            rgba: self.color
        Rectangle:
            pos: self.pos
            size: self.size
"""

class VideoLayout5(BoxLayout):

    def __init__(self, **args):
        Builder.load_string(VL5)
        super().__init__(**args)        

    def on_size(self, layout, size):
        if Window.width < Window.height:
            self.orientation = 'vertical'
            self.ids.preview.size_hint = (1, .3)
            self.ids.buttons.size_hint = (1, .2)
            self.ids.pad_end.size_hint = (1, .1)
        else:
            self.orientation = 'horizontal'
            self.ids.preview.size_hint = (.3, 1)
            self.ids.buttons.size_hint = (.2, 1)
            self.ids.pad_end.size_hint = (.1, 1)

BL5 = """
<ButtonsLayout5>:
    normal:
    down:
    txt:
    Background5:
    Label:
        text: root.txt
    Button:
        id:other
        on_press: root.photo()
        height: self.width
        width: self.height
        background_normal: 'icons/camera_white.png'
        background_down:   'icons/camera_red.png'
    ToggleButton:      
        id:video
        on_press: root.video_action(self.state)
        height: self.width
        width: self.height
        background_normal: root.normal
        background_down: root.down
"""

class ButtonsLayout5(RelativeLayout):

    normal = StringProperty()
    down = StringProperty()
    txt = StringProperty()

    def __init__(self, **kwargs):
        Builder.load_string(BL5)
        super().__init__(**kwargs)
        self.provider = CameraProviderInfo().get_name()
        if self.provider in ['picamera2','opencv']:
            self.normal = 'icons/video_white.png'
            self.down   = 'icons/video_red.png' 
        else:
            self.normal = 'icons/video-off.png'
            self.down   = 'icons/video-off.png'
        if self.provider in ['picamera2']:
            self.txt = 'Physically rotate the\ncamera by 90 deg to\na portrait orientation.'
            

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

    def photo(self):
        self.parent.ids.preview.capture_photo()
        
    def video_action(self, state):
        if self.provider in ['picamera2', 'opencv']:
            if state == 'down':
                self.parent.ids.preview.capture_video()
            else:
                self.parent.ids.preview.stop_capture_video()



        

    

