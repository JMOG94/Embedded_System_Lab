import grovepi
import time

#Global Variable Declaration
touch_sensor = 4        #Digital 4
button = 3              #Digital 3
sound_sensor = 1        #Analog 1
light_sensor = 2        #Analog 2
pot = 0                 #Analog 0



#I/O Declaration
grovepi.pinMode(touch_sensor, "INPUT")
grovepi.pinMode(button, "INPUT")
grovepi.pinMode(pot, "INPUT")
grovepi.pinMode(sound_sensor, "INPUT")
grovepi.pinMode(light_sensor, "INPUT")

print "***********************************************\n"
print "************Welcome to your system*************\n"
print "Please press:\n"
print "1. Check if touch sensor is pressed"
print "2. To get rotation measurement"
print "3. To get sound measure"
print "4. To get ligth measure"
print "5. To get button info"
print "************************************************"

a = raw_input("Write your desired command!\n")
print "Your input was : ", a

a = int(a)
if (a == 1):
        try:
                while True:
                        n = raw_input("Please click enter to get touch sensor information or stop to  stop!")
                        if(n  == 'stop'):
                                break
                        else:
                                x = grovepi.digitalRead(touch_sensor)
                                if (x == 1):
                                        print "the sensor is pressed"
                                else:
                                        print "the sensor is not pressed"
        except IOError:
                print "Error"
if (a == 2):
        try:
                while True:
                        n = raw_input("Please click enter to get the angle (degrees) or stop to stop!")
                        if(n  == 'stop'):
                                break
                        else:
                                x = grovepi.analogRead(pot)
                                x = (float)(x) * 5/1023
                                degrees = round(x*300/5,2)
                                print('The position is {0} degrees'.format(degrees))
        except IOError:
                print "Error"
if (a == 3):
        try:
                while True:
                        n = raw_input("Please click enter to get sound sensor information or stop to stop!")
                        x = grovepi.digitalRead(touch_sensor)
                        if(n == 'stop'):
                                break
                        else:
                                x = grovepi.analogRead(sound_sensor)
                                x = (float)(x) * 5/1023
                                m = round(x,2)
                                print('The measure is {} volts!'.format(m))
        except IOError:
                print "Error"                                
if (a == 4):
        try:
                while True:
                        n = raw_input("Please click enter to get light sensor information or stop to stop!")
                        if(n  == 'stop'):
                                break
                        else:
                                x = grovepi.analogRead(light_sensor)
                                resistance = round((float)(1023 - x) * 10,2) / x #This is KOhm
                                print('The sensor value is {0} and the resistance value is {1}k'.format(x,resistance))
        except IOError:
                print "Error"
if (a == 5):
        try:
                while True:
                        n = raw_input("Please click enter to get button information or stop to stop!")
                        if(n == 'stop'):
                                break
                        else:
                                x = grovepi.digitalRead(button)
                                if (x == 1):
                                        print "the button is pressed"
                                else:
                                        print "the button is not pressed"
        except IOError:
                print "Error"
