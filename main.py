from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import platform

from android_permissions import AndroidPermissions

from applayout.homescreen0  import HomeScreen0
from applayout.photoscreen1 import PhotoScreen1
from applayout.photoscreen2 import PhotoScreen2
from applayout.screenshot3 import ScreenShot3
from applayout.videoscreen4 import VideoScreen4

if platform == 'android':
    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    from android import mActivity
    View = autoclass('android.view.View')

    @run_on_ui_thread
    def hide_landscape_status_bar(instance, width, height):
        # width,height gives false layout events, on pinch/spread 
        # so use Window.width and Window.height
        if Window.width > Window.height: 
            # Hide status bar
            option = View.SYSTEM_UI_FLAG_FULLSCREEN
        else:
            # Show status bar 
            option = View.SYSTEM_UI_FLAG_VISIBLE
        mActivity.getWindow().getDecorView().setSystemUiVisibility(option)
elif platform != 'ios':
    # Dispose of that nasty red dot, required for gestures4kivy.
    from kivy.config import Config 
    Config.set('input', 'mouse', 'mouse, disable_multitouch')

class MyApp(App):
    
    def build(self):
        self.enable_swipe = False
        self.sm = ScreenManager()
        self.screens = [HomeScreen0(name='0'),
                        PhotoScreen1(name='1'),
                        PhotoScreen2(name='2'),
                        ScreenShot3(name='3'),
                        VideoScreen4(name='4')]
        for s in self.screens:
            self.sm.add_widget(s)
        if platform == 'android':
            Window.bind(on_resize=hide_landscape_status_bar)
        return self.sm

    def on_start(self):
        self.dont_gc = AndroidPermissions(self.start_app)

    def start_app(self):
        self.dont_gc = None
        self.enable_swipe = True

    def swipe_screen(self, right):
        if self.enable_swipe:
            i = int(self.sm.current)
            if right:
                self.sm.transition.direction = 'right'
                self.sm.current = str((i-1) % len(self.screens))
            else:
                self.sm.transition.direction = 'left'
                self.sm.current = str((i+1) % len(self.screens))
                    

MyApp().run()

