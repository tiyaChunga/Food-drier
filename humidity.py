import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import pyrebase
from datetime import datetime
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(32, GPIO.OUT)#BULB 
GPIO.setup(36, GPIO.OUT)#element and circulation fan
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)#exhaustion fan

GPIO.output(32, GPIO.LOW)
GPIO.output(36, GPIO.LOW)
GPIO.output(38, GPIO.LOW)
GPIO.output(40, GPIO.LOW)
GPIO.output(32, GPIO.HIGH)
GPIO.output(36, GPIO.HIGH)
GPIO.output(38, GPIO.HIGH)
GPIO.output(40, GPIO.HIGH)
firebaseConfig = {
    "apiKey": "AIzaSyBnMYP_Qrp3n0hm7Mg3LQPhWpJ_XXuX6WE",
    "authDomain": "fooddrier.firebaseapp.com",
    "databaseURL": "https://fooddrier.firebaseio.com",
    "projectId": "fooddrier",
    "storageBucket": "fooddrier.appspot.com",
    "messagingSenderId": "140086005841",
    "appId": "1:140086005841:web:af467326aaa3bf761c2870",
    "measurementId": "G-ZKYHQPJBEW"}

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

DHT_SENSOR = Adafruit_DHT.AM2302
DHT_PIN = 4
DHT_SENSOR2 = Adafruit_DHT.AM2302
DHT_PIN2 = 17


class Drier:
    def __init__(self):
        self.power_on()
            
    
    def power_on(self):
        
        while True:
            now = datetime.now()
            dt = now.strftime("%d/%m/%Y   %H:%M:%S")
            avghumid, avgtemp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            if avghumid is not None and avgtemp is not None:
                print("Time = ", dt +  "   Temperature = {0:0.1f}*C  Humidity = {1:0.1f}%".format(avgtemp, avghumid))
                
#                 print("chunga")
# 
#                 #print("Time = ", dt +  "   Temperature1 = {0:0.1f}*C  Humidity1 = {1:0.1f}%".format(temperature1, humidity1))  
#                 humidity2, temperature2 = Adafruit_DHT.read_retry(DHT_SENSOR1, DHT_PIN1)
#                 if humidity2 is not None and temperature2 is not None:
#                     avgtemp = (temperature1 + temperature2)/2
#                     avghumid = (humidity1 + humidity2)/2
#                     print("Time = ", dt +  "   Temperature = {0:0.1f}*C  Humidity = {1:0.1f}%".format(avgtemp, avghumid))
#             
#                     
#                 else:
#                     print("failed")
#                     
            
            
                 
                
            
            
               
                
#                     avgtemp = (temperature1 + temperature2)/2
#                     avghumid = (humidity1 + humidity2)/2
                
                 
#                     print("Time = ", dt +  "   Temperature = {0:0.1f}*C  Humidity = {1:0.1f}%".format(avgtemp, avghumid))                      
                          
                         
            else:
                print("check connections")
                time.sleep(5)
                self.power_on()
            
            
            food = db.child("food_drier").child("status").get()
            status = food.val()["power_on"]
            fruit = food.val()["fruits"]
            fish = food.val()["fish"]
            meat = food.val()["meat"]
            vegitable = food.val()["vegies"]
            start = food.val()["start"]
            
            

            if status == 1:
                GPIO.output(32, GPIO.LOW)
            
                
                
                if fruit == 1:
                    if start == 1:
                        db.child("food_drier").child("status").update({"done": 0})
                        
                        if avgtemp < 50 and avghumid > 20:
                            
                            GPIO.output(36, GPIO.LOW)
                            GPIO.output(40, GPIO.HIGH)
                            
                            if avghumid <= 20:
                                db.child("food_drier").child("status").update({"fruits": 0})
                                db.child("food_drier").child("status").update({"start": 0})
                                db.child("food_drier").child("status").update({"done": 1})
                            else:
                                self.power_on()
                        else:
                            GPIO.output(36, GPIO.HIGH)
                            GPIO.output(40, GPIO.LOW)
                            
                                
                    else:
                        GPIO.output(36, GPIO.HIGH)
#                         GPIO.output(40, GPIO.LOW)
#                         print("ononon")
                        
                        
                elif fish == 1:
                    if start == 1:
                        db.child("food_drier").child("status").update({"done": 0})
                        
                        if avgtemp  < 68 and avghumid > 15:
                        
                            GPIO.output(36, GPIO.LOW)
                            GPIO.output(40, GPIO.HIGH)
                            if avghumid <= 15:
                                db.child("food_drier").child("status").update({"fish": 0})
                                db.child("food_drier").child("status").update({"start": 0})
                                db.child("food_drier").child("status").update({"done": 1})
                            else:
                                self.power_on()
                        else:
                            GPIO.output(36, GPIO.HIGH)
                            GPIO.output(40, GPIO.LOW)
                    else:
                        GPIO.output(36, GPIO.HIGH)
                        #GPIO.output(40, GPIO.LOW)
                        
                    
                elif vegitable == 1:
                    if start == 1:
                        db.child("food_drier").child("status").update({"done": 0})
                        
                        if avgtemp  < 52:
                    
                            GPIO.output(36, GPIO.LOW)
                            GPIO.output(40, GPIO.HIGH)
                            if avghumid <= 20:
                                db.child("food_drier").child("status").update({"vegies": 0})
                                db.child("food_drier").child("status").update({"start": 0})
                                db.child("food_drier").child("status").update({"done": 1})
                            else:
                                self.power_on()
                        else:
                            GPIO.output(36, GPIO.HIGH)
                            GPIO.output(40, GPIO.LOW)
                    else:
                        GPIO.output(36, GPIO.HIGH)
#                         GPIO.output(40, GPIO.LOW)
                        
                elif meat == 1:
                    if start == 1:
                        db.child("food_drier").child("status").update({"done": 0})
                        
                        if avgtemp  < 37 and avghumid > 12:
                        
                            GPIO.output(36, GPIO.LOW)
                            GPIO.output(40, GPIO.HIGH)
                            if avghumid <= 20:
                                db.child("food_drier").child("status").update({"meat": 0})
                                db.child("food_drier").child("status").update({"start": 0})
                                db.child("food_drier").child("status").update({"done": 1})
                            else:
                                self.power_on()
                        else:
                            GPIO.output(36, GPIO.HIGH)
                            GPIO.output(40, GPIO.LOW)
                    else:
                        GPIO.output(36, GPIO.HIGH)
#                         GPIO.output(40, GPIO.LOW)
                        
                else:
                    GPIO.output(36, GPIO.HIGH)
                    GPIO.output(40, GPIO.HIGH)
                                    
            else:
                GPIO.output(32, GPIO.HIGH)
                GPIO.output(36, GPIO.HIGH)
                GPIO.output(38, GPIO.HIGH)
                GPIO.output(40, GPIO.HIGH)
           
        
                
                                    
Drier()
    
                
           
            

