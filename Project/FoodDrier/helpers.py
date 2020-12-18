screen_helper = """


ScreenManager:
    MenuScreen:
    HomeWithPowerOn:
    SelectItemWindow:
    DryingWindow:
    Drying:
    History:
    Done:
    
<MenuScreen>:
    name: 'menu'
                
    MDFloatingActionButton:
        icon: "Images/white.png"
        size_hint: 1, 0.9
        #pos_hint: {"center_x": 0.52}       
   
         
    MDFloatingActionButton:
        icon: "Images/btnpower.png"
        elevation_normal: 12
        size_hint: .4, .3
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        elevation_normal: 30
        on_release:
            root.manager.current = 'power on'
            root.manager.transition.direction = 'left'
            app.power_on()
            
    MDTextButton:
        text: 'Tap To Power On'
        pos_hint: {"center_x": 0.5, "center_y": 0.26}
            
    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: False
         
        
    NavigationLayout:

        ScreenManager:
            Screen:

                BoxLayout:
                    orientation: 'vertical'
                    pos_hint: {"center_x": 0.5, "center_y": 1.4}
                       
                    
                    

                    MDToolbar:
                        title: "Food Drier Off"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                        md_bg_color: .752,.514,.18,1

                    #Widget:
                    
    

        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                
                Image:
                    source: 'Images/food.jpg'
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'History'
                            
                            on_release:
                                root.manager.current = 'history'
                                root.manager.transition.direction = 'left'
                            
                            IconLeftWidget:
                                icon: 'poll'
                        OneLineIconListItem:
                            text: 'About Us'
                            IconLeftWidget:
                                icon: 'account-group'
                            
                        OneLineIconListItem:
                            text: 'Help'
                            IconLeftWidget:
                                icon: 'help-circle-outline'
                                
    MDFloatingActionButton:
        icon: "Images/delete-icon.png"
        pos_hint: {"x" : 0.86, "y" : 0.91}
        size_hint: .1, .08
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"
        on_press: 
            app.close_app()
                    
       


<HomeWithPowerOn>:

    name: 'power on'
    
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 1.4}
        color: "black"
         
        MDToolbar:
            md_bg_color: .752,.514,.18,1
            title: 'On'  
            
    MDFloatingActionButton:
        icon: "Images/white.png"
        size_hint: 1, 0.9
        #pos_hint: {"center_x": 0.52} 
                      
        
    MDFloatingActionButton:
        icon: "Images/poweroff2.png"
        size_hint: .4, .3
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        user_font_size: "25sp"
        elevation_normal: 30
        on_release:
            app.power_off()
            app.back_on_select()
            app.dry_off()
            root.manager.current = 'menu' 
            root.manager.transition.direction = 'right' 
            
    MDTextButton:
        text: 'Tap To Power Off'
        pos_hint: {"center_x": 0.5, "center_y": 0.26}        

    
                    
    MDRaisedButton:
        text: "DRY"
        text_color: 0, 0, 0, 1
        pos_hint: {"center_x" : 0.5, "y" : 0.1}
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"
        on_press: 
            root.manager.current = 'select'
            app.dry()
                  

<SelectItemWindow>:
    name: 'select'

    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 1.4}
        #color: "8,.898,.1,1"
     
        MDToolbar:
            title: 'Select Food'           
            md_bg_color: .752, .514, .18, 1
            elevation: 50
            
    MDIconButton:
        icon: "backspace-outline"
        pos_hint: {"x" : 0.8, "y" : 0.9}
        #size_hint: .1, .1
        md_bg_color: .752,.514,.18,1
        #elevation_normal: 20
        opacity: 0.9
        on_press: 
            root.manager.current = 'power on'
                    
                
            
   
    MDFloatingActionButton:
        icon: "Images/white.png"
        size_hint: 1, 0.9
       
    # FRUITS
    MDFloatingActionButton:
        id: zipatso
        icon: "Images/apppl.jpg"
        pos_hint: {"x": .1, "y": .51}
        on_press: 
            root.manager.current = 'dry'
            root.manager.transition.direction = 'down'
            app.fruits() 
        size_hint: .35, .3
        md_bg_color: .952,.952,.952, 0
        #user_font_size: "150sp"
        
    MDRaisedButton:
        text: 'Fruits'
        pos_hint: {'x':.1,'center_y':0.48}
        on_press: 
            root.manager.current = 'dry'
            root.manager.transition.direction = 'down'
            app.fruits()
        text_color: 0, 0, 0, 1
        md_bg_color: 1, 1, 1, 1
        font_weight: "bold"
        size_hint: .35, .06
        
    # MEAT
    MDFloatingActionButton:
        icon: "Images/meat.jpg"
        pos_hint: {"x": .52, "y": .51}
        on_press: 
            root.manager.current = 'dry'
            root.manager.transition.direction = 'up'
            app.nyama()
        size_hint: .35, .3
        md_bg_color: .952,.952,.952, 0
        #user_font_size: "150sp"
    
    MDFlatButton:
        text: 'Meat'
        pos_hint: {'x':0.52,'center_y':0.48}
        on_press: 
            root.manager.current = 'dry'
            root.manager.transition.direction = 'up'
            app.nyama()
        text_color: 0, 0, 0, 1
        md_bg_color: 1, 1, 1, 1
        font_weight: "bold"
        size_hint: .35, .06
        
    # VEGIES
    MDFloatingActionButton:
        icon: "Images/veges.jpg"
        pos_hint: {"x": .1, "y": .1}
        on_press: 
            root.manager.current = 'dry'
            root.manager.transition.direction = 'up'
            app.vegies()
        size_hint: .35, .3
        md_bg_color: .952,.952,.952, 0
        #user_font_size: "150sp"
    
    MDFlatButton:
        text: 'Vegies'
        pos_hint: {'x':0.1,'y':0.04}
        on_press: 
            root.manager.current = 'dry'
            root.manager.transition.direction = 'up'
            app.vegies()
        text_color: 0, 0, 0, 1
        md_bg_color: 1, 1, 1, 1
        font_weight: "bold"
        size_hint: .35, .06
        
    # FISH
    MDFloatingActionButton:
        icon: "Images/fish.png"
        pos_hint: {"x": .52, "y": .1}
        on_press: 
            root.manager.current = 'dry'
            root.manager.transition.direction = 'down'
            app.fish()
        size_hint: .35, .3
        md_bg_color: .952,.952,.952, 0
        #user_font_size: "150sp"
    
    MDFlatButton:
        text: 'Fish'
        pos_hint: {'x':0.52,'y':0.04}
        on_press: 
            root.manager.current = 'dry'
            root.manager.transition.direction = 'down'
            app.fish()
        text_color: 0, 0, 0, 1
        md_bg_color: 1, 1, 1, 1
        font_weight: "bold"
        size_hint: .35, .06
        

<DryingWindow>:
    name: "dry"

    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 1.4}
        color: "black"



        MDToolbar:
            title: 'Dry'
            md_bg_color: .752,.514,.18,1

    MDFloatingActionButton:
        icon: "Images/white.png"
        size_hint: 1, 0.9

    MDIconButton:
        icon: "backspace-outline"
        pos_hint: {"x" : 0.8, "y" : 0.9}
        #size_hint: .1, .1
        md_bg_color: .752,.514,.18,1
        #elevation_normal: 20
        opacity: 0.9
        #font_weight: "bold"
        on_press: 
            root.manager.current = 'select'

    MDRaisedButton:
        text: 'START'
        pos_hint: {'center_x':.5,'center_y':0.5}
        on_press: 
            root.manager.current = 'drying'
            root.manager.transition.direction = 'left'
            app.start_stop()
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
            md_bg_color: .752,.514,.18,1
            
    MDFloatingActionButton:
        icon: "Images/white.png"
        size_hint: 1, 0.9

    MDRaisedButton:
        text: 'STOP'
        pos_hint: {'center_x':.5,'center_y':0.5}
        on_press: 
            root.manager.current = 'done'
            root.manager.transition.direction = 'up'
            app.start_stop_stop()
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"
    
<History>

    name: "history"
    
    text: 'Hello' 
        
    MDRaisedButton:
        text: '<'
        pos_hint: {'x': .01, 'y': .01}
        on_press: root.manager.current = 'menu'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"
       
    MDRaisedButton:
        text: 'CLEAR HISTORY'
        pos_hint: {'x': .53, 'y': .01}
        # on_press: root.manager.current = 'history'
        text_color: 0, 0, 0, 1
        md_bg_color: .752,.514,.18,1
        font_weight: "bold"             
       
<Done>:
    name: 'done'
    
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {"center_x": 0.5, "center_y": 1.4}
        color: "black"
         
        MDToolbar:
            md_bg_color: .752,.514,.18,1
            title: 'Done'  
    MDFloatingActionButton:
        icon: 'Images/check.png'
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint: .4, .3
        
        # on_press: root.manager.current = 'history'
        #text_color: 0,1, 0, 1
        #md_bg_color: .752,.514,.18,1
        #font_weight: "bold" 
        on_press: 
            root.manager.current = 'select'
                   
"""
