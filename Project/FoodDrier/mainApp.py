from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from helpers import screen_helper
import sys

# import pyrebase
#
# firebaseConfig = {
#     "apiKey": "AIzaSyBnMYP_Qrp3n0hm7Mg3LQPhWpJ_XXuX6WE",
#     "authDomain": "fooddrier.firebaseapp.com",
#     "databaseURL": "https://fooddrier.firebaseio.com",
#     "projectId": "fooddrier",
#     "storageBucket": "fooddrier.appspot.com",
#     "messagingSenderId": "140086005841",
#     "appId": "1:140086005841:web:af467326aaa3bf761c2870",
#     "measurementId": "G-ZKYHQPJBEW"}
#
# firebase = pyrebase.initialize_app(firebaseConfig)
#
# db = firebase.database()

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


class History(Screen):
    pass


class Done(Screen):
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
sm.add_widget(History(name='history'))
sm.add_widget(Done(name='done'))


class FoodDrier(MDApp):
    dialog = None
    id = None

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    data = {
        'account-heart': '',
        'send': '',
        'settings': '',

    }

    def popup(self):
        if not self.dialog:
            self.dialog = MDDialog(text=" ! Please Restart The Application And Check Your Internet Connection",
                                   buttons=[MDFlatButton(text='Ok', text_color=self.theme_cls.primary_color,

                                                         )],
                                   size_hint=(None, None),
                                   # pos_hint={'y': 0.82},
                                   size=(250, 0))

        self.dialog.open()

    # def popup2(self):
    #     if not self.dialog:
    #         self.dialog = MDDialog(text=" ",
    #                                buttons=[MDFlatButton(text='Done', text_color=self.theme_cls.primary_color,
    #                                                      on_press=self.start_stop(),
    #
    #                                                      )],
    #                                size_hint=(None, None),
    #                                # pos_hint={'y': 0.82},
    #                                size=(250, 0))
    #
    #     self.dialog.open()

    def close_app(self):

        sys.exit('Connection')

    def err_handling(self):
        try:
            self.power_on()

        except:
            self.popup()


# def power_on(self):
#     # db.child("food_drier").child("function").child("drying").update({"dry": 1})
#     db.child("food_drier").child("status").update({"power_on": 1})
#
# # updating the data base after pressing a button
# # thus for intergration of the android app and the raspberry pi
#
# # updating the power on value by pressing a power on button on the android app
# def power_off(self):
#     # db.child("food_drier").child("function").child("drying").update({"dry": 0})
#     db.child("food_drier").child("status").update({"power_on": 0})
#
# # updating the dry value by pressing a dry button on the android app
# # setting the drier ready for the drying process
# def dry(self):
#     db.child("food_drier").child("function").child("drying").update({"dry": 1})
#
# # updating the dry value by pressing a dry button on the android app
# # removing the drier from the ready mode
# def dry_off(self):
#     db.child("food_drier").child("function").child("drying").update({"dry": 0})
#
# # updating the fruits value by pressing a fruit button on the android app
# # telling the drier that the food we are trying to dry are fruits
# # calling the fruit function in the pi
#
# def fruits(self):
#     db.child("food_drier").child("status").update({"fruits": 1})
#
# # updating the vegies value by pressing a vegies button on the android app
# # telling the drier that the food we are trying to dry are vegies
# # calling the vegies function in the pi
# def vegies(self):
#     db.child("food_drier").child("status").update({"vegies": 1})
#
# # updating the meat value by pressing a meat button on the android app
# # telling the drier that the food we are trying to dry are meat
# # calling the meat function in the pi
# def nyama(self):
#     db.child("food_drier").child("status").update({"meat": 1})
#
# # updating the fish value by pressing a fish button on the android app
# # telling the drier that the food we are trying to dry are fish
# # calling the fish function in the pi
# def fish(self):
#     db.child("food_drier").child("status").update({"fish": 1})
#
# # on clicking the back button on the select food window, all the selected foods should be deactivated
# # no function of a food should be called in the pi
# def back_on_select(self):
#     db.child("food_drier").child("status").update({"fruits": 0})
#     db.child("food_drier").child("status").update({"vegies": 0})
#     db.child("food_drier").child("status").update({"meat": 0})
#     db.child("food_drier").child("status").update({"fish": 0})
#
# # start the drying after selecting the specified food and clicking the start button
# def start_stop(self):
#     db.child("food_drier").child("status").update({"start": 1})
#
# # stop the ongoing drying process
# # resume the stopped drying process
# def start_stop_stop(self):
#     db.child("food_drier").child("status").update({"start": 0})


FoodDrier().run()
