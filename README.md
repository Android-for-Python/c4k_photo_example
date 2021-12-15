Camera4Kivy Photo Example
=========================

*Just Basic Camera Stuff, but you gotta start somewhere.*

# Overview

Four screens showing camera orientation, aspect ratio, and image capture. On Android `orientation = all` is available, on the desktop change the window size to change the window from landscape to portrait to simulate rotating a mobile device. 

This example depends on Camera4Kivy. **[Read about Camera4Kivy](https://github.com/Android-for-Python/Camera4Kivy#camera4kivy)** because, depending on the platform you may need to install a [camera provider](https://github.com/Android-for-Python/Camera4Kivy#dependencies).

Available on the [usual platforms](https://github.com/Android-for-Python/Camera4Kivy/#tested-platforms).

# Install

Assuming you have installed a camera provider (if necessary):

## Windows, MacOS, Linux

`pip3 install camera4kivy`

## Android

Camera4Kivy depends on the 'master' version of Buildozer. Currently `1.2.0.dev0`

`pip3 install git+https://github.com/kivy/buildozer.git`

The example includes a camera provider and a buildozer.spec

For any other project, follow the [camerax_provider install instructions](https://github.com/Android-for-Python/Camera4Kivy#candroid-camerax_provider)

And the following **must** be in the buildozer.spec:

`requirements= python3, kivy, camera4kivy`

`android.permissions = CAMERA, RECORD_AUDIO`

`android.api = 30`  or greater (min 29)

`p4a.local_recipes = ./camerax_provider/recipes`

`p4a.hook = ./camerax_provider/gradle_options.py`   

# Other Stuff

The example demonstrates Preview Widget layout: orientation, aspect ratio, and letterbox handling. Also switching between cameras, image capture, and screenshot capture. On Android only it demonstrates video with audio capture, pinch/spread zoom, and tap focus/exposure. 

A prerequisite is a working camera is installed and seen as device '0'. Test this with the platform's camera app before proceeding. Optionally a second camera '1' may be selected in the app.

