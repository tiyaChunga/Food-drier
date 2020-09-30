from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from helpers import screen_helper
from kivy.core.window import Window
# from kivy.uix.boxlayout import BoxLayout
# from kivymd.theming import ThemableBehavior
# from kivymd.uix.list import MDList


Window.size = (300, 500)


class MenuScreen(Screen):
    pass


class HomeWithPowerOn(Screen):
    pass


class SelectItemWindow(Screen):
    pass

class DryingWindow(Screen):
    pass

class Drying(Screen):
    pass

class ResumeDrying(Screen):
    pass


# class ContentNavigationDrawer(BoxLayout):
#     pass
#
# class DrawerList(ThemableBehavior, MDList):
#     pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(HomeWithPowerOn(name='power on'))
sm.add_widget(SelectItemWindow(name='select'))
sm.add_widget(DryingWindow(name='dry'))
sm.add_widget(ResumeDrying(name='resume'))




class FoodDrier(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.primary_palette =  'BlueGray'
        return screen


FoodDrier().run()
