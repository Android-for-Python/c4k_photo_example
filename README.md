Camera4Kivy Photo Example
=========================

*Just Basic Camera Stuff, but you gotta start somewhere.*

# Overview

Four screens showing camera orientation, aspect ratio, and image capture. On Android `orientation = all` is available, on the desktop change the window size to change the window from landscape to portrait to simulate rotating a mobile device.

Available on most of the [usual platforms](https://github.com/Android-for-Python/Camera4Kivy/#tested-platforms).

The example demonstrates Preview Widget layout: orientation, aspect ratio, and letterbox handling. Also switching between cameras, image capture, and screenshot capture. On Android only it demonstrates video with audio capture, pinch/spread zoom, and tap focus/exposure. 

# Install

This example depends on Camera4Kivy. **[Read about Camera4Kivy](https://github.com/Android-for-Python/Camera4Kivy#camera4kivy)** because, depending on the platform you may need to install a [camera provider](https://github.com/Android-for-Python/Camera4Kivy#dependencies).


## Windows, MacOS, Linux

`pip3 install camera4kivy`

## Android

Camera4Kivy depends on the 'master' version of Buildozer. Currently `1.2.0.dev0`

`pip3 install git+https://github.com/kivy/buildozer.git`

The example includes a [camera provider](https://github.com/Android-for-Python/camera4kivy#android-camera-provider) and a [buildozer.spec](https://github.com/Android-for-Python/camera4kivy#buildozerspec).


