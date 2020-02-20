# Automatically-turn-off-your-RaspberryPi-touchscreen

A simple script to automatically turn off the official 7" RasPi touchscreen after a given amount of time. It can be turned on again by any device that can input through the GPIO pins ( e.g. a button or a motion sensor). Touching the screen to turn it on is not possible with this script, as the touch capabilities also get turned off.

If you directly connect a 5V GPIO-pin to any other pin, even through a button/switch, it will permanently fry your Raspberry Pi. Don't do that.


**How-To:**

What you'll need:
* A Raspberry Pi (any model should work, tested with 2B and 3B+) with a power supply and Raspbian installed onto its SD Card
* The official Raspberry Pi touchscreen
* Some spare jumper wires and a toggle to activate the screen (Button/Motio Sensor)

In my case I used a cheap PIR motion sensor to activate the screen, so I can just walk by and take a look at the screen. There is plenty of documentation about these on the internet.

If you want to use a button or a switch, you have to connect a 3.3V pin to a data pin (marked in green on the pinout image) and specify the data pin in the script (See Configuration). See the included GPIO pinout image for reference.


**Step-by-step guide:**

0. Connect the touchscreen.
1. Download the files provided in this repository to your Pi.
2. Extract the folder "display" to /home/pi on your Raspberry Pi
3. Open the folder "display", right click on "script" --> "Properties" --> "Permissions" --> Change "Execute" from "Nobody" to "Anyone" --> OK
4. Execute the script, it doesn't matter if you choose to execute it in Terminal or not, it doesn't show anything either way.
5. After the next restart the script should be automatically executed.


**How-To-PIR-Sensor**

A PIR motion sensor has 3 pins:
* VCC: This is the + pin. COnnect it to a +5V pin on the Raspberry Pi
* GND: This is the Ground pin. It has to be connected to a black ground pin. See the included GPIO pinout image for reference
* OUT: This pin provides the ouput data. It can be connected to any of the pins that are marked green in the included GPIO pinout image, though this has to be Configured in the scrpipt itself.


**Configuration**

You can just open the script that turns your screen on and off. It's located in /home/pi/display/AutoShutdownScreen.py
It can be opened with the pre-installed Python IDE Thonny.
The following variables can be changed:
* inputPin : Change the pin that is used to turn the screen back on.
* timeTilSleep : Enter the amount of time until the screen should turn off in seconds. Note that a PIR motion sensor will also send for some time after doesn't detect anything anymore.

To test the script you can execute it in Thonny and look at the console output.


So, thats pretty much it. If you have any questions, ask away in the issues section, maybe ill be able to solve them.
