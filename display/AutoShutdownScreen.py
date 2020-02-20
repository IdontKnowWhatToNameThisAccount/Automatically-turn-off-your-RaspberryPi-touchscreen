import RPi.GPIO as GPIO
import os

timeTilSleep = 0 # controls the time until the screen turns off.
amt = 0 # just an internal variable, leave it alone please.

GPIO.setmode(GPIO.BOARD)

inputPin = 11 # here you can control which GPIO pin is used for input. The numbering starts in the top left and goes to the right, then into the next row. Example: Pin 11 is the 6th pin from top in the left row. Pin 4 is the 2nd pin in the right row.

GPIO.setup(inputPin,GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 

import time

while True:
    if(GPIO.input(inputPin)): # This if-loop is triggered when the pin is activated.
        amt = 0
        os.system("bash -c \"/home/pi/display/display_on\"")
        print("The action was triggered")
        time.sleep(1)
        
    if not(GPIO.input(inputPin)) and amt < timeTilSleep + 1: # This loop count up as soon as the GPIO-pin is no longer active and counts up to the desired sleep time.
        amt += 1
        print("The action was not performed for" ,amt, " seconds.")
        time.sleep(1)
		
    if amt > timeTilSleep: # This loop turns off the screen until the action is performed again.
        os.system("bash -c \"/home/pi/display/display_off\"")
        print("off")
        time.sleep(1)
