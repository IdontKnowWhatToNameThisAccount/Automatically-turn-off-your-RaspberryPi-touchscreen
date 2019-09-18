# Automatically-turn-off-your-RaspberryPi-touchscreen

A simple script to automatically turn off the official 7" RasPi touchscreen after a given amount of time. It can be turned on again by any device that can input through the GPIO pins ( e.g. a button or a motion sensor). Touching the screen to turn it on is not possible with this script, as the touch capabilities also get turned off.

Disclaimer: I am not responsible for bricked devices, dead SD cards, thermonuclear war or you getting fired because your Raspberry Pi died from connecting the wrong pins. Please do some research if you have any concerns about anything in this script or the How-To-Guide. YOU are choosing to use this script and following the guide, and if you point the finger at me for messing up your Pi, I will laugh at you. Hard & a lot.

If you dircetly connect a 5V GPIO-pin to any other pin, even through a button/switch, it will permanently fry your Raspberry Pi. Dont do that.

**How-To:**

What you'll need:
* A Raspberry Pi (any model should work, tested with 2B and 3B+) with a power supply and raspbian installed onto its SD Card
* The official Raspberry Pi touchscreen
* Some spare jumper wires and a toggle to activate the screen

In my case I used a cheap PIR motion sensor to activate the screen, so I can just walk by and take a look at whatever you want to display. There is planty of documentation about these on the internet.

If you want to use a button or a switch, you have to connect a 3.3V pin to a data pin (marked in green on the pinout iamge) and specify the data pin in the script. See the included GPIO pinout image for refrence.

**Step-by-step guide:**

0. Connect the touchscreen.
1. Download the files provided in this repository to your Pi.
2. Extract the folder "display" to /home/pi on your Raspberry Pi
3. Open the folder "display", right click on "script" --> "Properties" --> "Permissions" --> Change "Execute" from "Nobody" to "Anyone" --> OK
4. Execute the script, it doesnt matter if you choose to execute it in Terminal or not, it doesnt show anything either way.
5. After the next restart the script should be automatically executed.

**Configuration**

You can just open the script that turns your screen on and off. It's located in /home/pi/display/AutoShutdownScreen.py
It can be opened with the pre-installed Python IDE Thonny.
The following variables can be changed:
* input_pin : Change the pin that is used to turn the screen back on.
* timeTilSleep : Enter the amount of time until the screen should turn off in seconds. Note that a PIR motion sensor will also send for some time after doesnt detect anything anymore.

To test the script you an execute it in Thonny and look at the console output.


So, thats pretty much it. If you have any questions, ask away in the issues section, maybe ill be able to solve them.
