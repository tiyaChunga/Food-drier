screen_helper = """


ScreenManager:
    MenuScreen:
    HomeWithPowerOn:
    SelectItemWindow:
    DryingWindow:
    Drying:
    ResumeDrying:
  
<ResumeDrying>:
    name : "resume"
    
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 1.4}
        color: "black"
    
        
     
        MDToolbar:
            title: 'Resume'
           
            left_action_items: [["menu", lambda x: app.navigation_draw()]]

    MDRectangleFlatButton:
        text: 'RESUME'
        pos_hint: {'center_x':.5,'center_y':0.5}
        on_press: root.manager.current = 'drying'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':.5,'center_y':0.3}
        on_press: root.manager.current = 'select'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"


<Drying>:
    name: "drying"
    
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 1.4}
        color: "black"
    
        
     
        MDToolbar:
            title: 'Drying'
           
            # left_action_items: [["menu", lambda x: app.navigation_draw()]]

    MDRectangleFlatButton:
        text: 'STOP'
        pos_hint: {'center_x':.5,'center_y':0.5}
        on_press: root.manager.current = 'resume'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':.5,'center_y':0.3}
        text_color: 0, 0, 0, 1
        md_bg_color: .76,.73,.73,1
        font_weight: "bold"

<MenuScreen>:
    name: 'menu'
    
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 1.4}
    
        MDToolbar:
            title: 'Food Drier Off'
           
            # left_action_items: [["menu", lambda x: app.navigation_draw()]]
        
          
           
    MDFlatButton:
        text: "Power On"
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        text_size: 8
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        user_font_size: "25sp"
        on_release: root.manager.current = 'power on'
                 
    # MDIconButton:
    #     icon: "power"
    #     pos_hint: {"center_x": 0.5, "center_y": 0.65}
    #     user_font_size: "150sp"
    #     on_release: root.manager.current = 'power on'

    MDFlatButton:
        text: "Help"
        text_color: 1, 1, 1, 1
        md_bg_color: .76,.73,.73,1
        text_size: 8
        pos_hint: {"center_x": .9, "center_y": 0.05}
        user_font_size: "25sp"
    MDFlatButton:
        text: "HISTORY"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x" : 0.5, "center_y" : 0.35}
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"
    MDFlatButton:
        text: "About Us"
        text_color: 1, 1, 1, 1
        md_bg_color: .76,.73,.73,1
        text_size: 8
        pos_hint: {"center_x" : .09, "center_y" : .05}



<HomeWithPowerOn>:

    name: 'power on'
    
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 1.4}
        color: "black"
    
        
     
        MDToolbar:
            title: 'On'
           
            # left_action_items: [["menu", lambda x: app.navigation_draw()]]
    
    # MDIconButton:
    #     icon: "on"
    #     pos_hint: {"center_x": 0.5, "center_y": 0.65}
    #     user_font_size: "150sp"
    #     on_release: root.manager.current = 'menu'
        
    MDFlatButton:
        text: "Turn Off "
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        text_size: 8
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        user_font_size: "25sp"
        on_release:
            root.manager.current = 'menu' 
            root.manager.transition = "left"  

    MDRectangleFlatButton:
        text: "DRY"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x" : 0.5, "center_y" : 0.35}
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"
        on_press: root.manager.current = 'select'

<SelectItemWindow>:
    name: 'select'

    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 1.4}
        color: "black"
     
        MDToolbar:
            title: 'Select Food'
           
            # left_action_items: [["menu", lambda x: app.navigation_draw()]]
   

    MDRectangleFlatButton:
        text: 'FRUITS'
        pos_hint: {'center_x':1/3,'center_y':0.7}
        on_press: root.manager.current = 'dry'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"

    MDRectangleFlatButton:
        text: 'VEGIES'
        pos_hint: {'center_x':.7,'center_y':0.7}
        on_press: root.manager.current = 'dry'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"

    MDRectangleFlatButton:
        text: 'MEAT'
        pos_hint: {'center_x':1/3,'center_y':0.5}
        on_press: root.manager.current = 'dry'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"

    MDRectangleFlatButton:
        text: 'FISH'
        pos_hint: {'center_x':.7,'center_y':0.5}
        on_press: root.manager.current = 'dry'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':.5,'center_y':0.3}
        on_press: root.manager.current = 'power on'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"

<DryingWindow>:
    name: "dry"
    
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 1.4}
        color: "black"
    
        
     
        MDToolbar:
            title: 'Dry'
           
            # left_action_items: [["menu", lambda x: app.navigation_draw()]]

    MDRectangleFlatButton:
        text: 'START'
        pos_hint: {'center_x':.5,'center_y':0.5}
        on_press: root.manager.current = 'drying'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"

    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {'center_x':.5,'center_y':0.3}
        on_press: root.manager.current = 'select'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"






"""