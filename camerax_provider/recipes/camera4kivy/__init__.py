from pythonforandroid.recipe import PythonRecipe, current_directory, \
    shprint, info
import sh
from os.path import join

class Camera4KivyRecipe(PythonRecipe):

    version = '0.0.0'
    url = 'https://github.com/Android-for-Python/Camera4Kivy/archive/refs/heads/main.zip'
    site_packages_name = 'camera4kivy'

    depends = ['setuptools']
    python_depends = ['gestures4kivy']
    call_hostpython_via_targetpython = False

    def postbuild_arch(self, arch):
        super().postbuild_arch(arch)
        info('Copying camera4kivy java class to classes build dir')
        with current_directory(self.get_build_dir(arch.arch)):
            shprint(sh.cp, '-a',
                    join('src', 'camera4kivy', 'src', 'org', 'kivy', 'camerax'),
                    self.ctx.javaclass_dir)

recipe = Camera4KivyRecipe()
