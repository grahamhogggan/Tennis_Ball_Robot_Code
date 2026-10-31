Code to run a custom designed robot via a raspberry pi  

About the project:
The tennis ball root is a personal project I made that picks up tennis balls and shoots them using a drum shooter. It was Designed by me in Onshape, and built using primarily goBilda components and roboclaw motor controllers. 

Setup Instructions:
* Setup raspberry pi as a Wifi access point
* Install roboclaw_3 python library from basicmicro
* Upload file main.py to the raspberry pi
* Used basicmicro motion studio to set up roboclaw units in packet serial mode with two distinct addresses.

Running Instructions:
* Establish ssh connection with raspberry pi
* run main.py on the raspberry pi
* run inpuBlaster.py on your computer. For myself, I created a batch file to make it even faster to do this step.
* Use WASD on your keyboard to move the robot, and I, K, and L for the intake, kicker, and launcher, respectively.

How the code was made:
* communicates with the two Roboclaw units in packet serial mode
* used a UDP socket to send keyboard input to the raspberry pi, which takes that input and controls the motors accordingly
* Communicates with kicker bar motor controller using GPIO pins
