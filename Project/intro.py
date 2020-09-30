from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
Screen:

    MDIconButton:
        icon: "power"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        user_font_size: "150sp"
        
    MDIconButton:
        icon: "help"
        pos_hint: {"center_x": .9, "center_y": 0.05}
        user_font_size: "25sp"
    MDFlatButton:
        text: "HISTORY"
        text_color: 1, 1, 1, 1
        pos_hint: {"center_x" : 0.5, "center_y" : 0.5}
        md_bg_color: .5,.7,1,.9
    MDFlatButton:
        text: "About Us"
        text_color: 1, 1, 1, 1
        pos_hint: {"center_x" : .09, "center_y" : .05}
        md_bg_color: .2,.7,.7,.3   
'''


class FoodDrier(MDApp):
    def build(self):
        return Builder.load_string(KV)


FoodDrier().run()