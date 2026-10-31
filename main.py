import time
import socket
import RPi.GPIO as GPIO
from roboclaw_3 import Roboclaw

UDP_IP = "0.0.0.0"
UDP_PORT=5005

motorsRunning=False
motor1Speed = 0
motor2Speed = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

print("program started")
roboclaw = Roboclaw("/dev/serial0", 38400,timeout=0.01,retries = 3)
print("roboclaw object initialized")

roboclaw.Open()
print("roboclaw comms opened")

print("listening for keyboard input")

        
def STOP():
    SetMotorsBoth(0)
def SetMotorSpeed(motor, speed):
    if(motor == 1):
        global motor1Speed
        if(speed!=motor1Speed):
            motor1Speed = speed
            print("motor 1 set to "+str(speed))
            if(speed>=0):
                roboclaw.ForwardM1(0x80,speed)
                time.sleep(0.002)
            if(speed<0):
                roboclaw.BackwardM1(0x80,-speed)
                time.sleep(0.002)
    if(motor == 2):
        global motor2Speed
        if(speed!=motor2Speed):
            motor2Speed = speed
            print("motor 2 set to "+str(speed))
            if(speed>=0):
                roboclaw.ForwardM2(0x80,speed)
                time.sleep(0.002)
            if(speed<0):
                roboclaw.BackwardM2(0x80,-speed)
                time.sleep(0.002)
        
    
def SetMotorsBoth(speed):
    SetMotorSpeed(1,speed)
    SetMotorSpeed(2,speed)

STOP()
status,raw_voltage = roboclaw.ReadMainBatteryVoltage(0x80)
if status:
    print("Main Voltage: "+ (str)(raw_voltage/10.0))
else:
    print("No battery status received")
while True:

    data,addr = sock.recvfrom(1024)
    input = data.decode('utf-8', errors = 'ignore')
    leftAxis = 0
    rightAxis = 0
    if 'w' in input:
        leftAxis+=1
        rightAxis+=1
    if 'a' in input:
        leftAxis-=1
        rightAxis+=1
    if 's' in input:
        leftAxis-=1
        rightAxis-=1
    if 'd' in input:
        leftAxis+=1
        rightAxis-=1
    if(leftAxis>1):
        leftAxis = 1
    if(leftAxis<-1):
        leftAxis = -1
    if(rightAxis>1):
        rightAxis = 1
    if(rightAxis<-1):
        rightAxis = -1;
    SetMotorSpeed(2, leftAxis*-80)
    SetMotorSpeed(1,rightAxis*-80)
    if 'i' in input:
        roboclaw.ForwardM1(0x81,127)
    else:
        roboclaw.ForwardM1(0x81,0)
    if 'l' in input:
        roboclaw.BackwardM2(0x81,127)
    else:
        roboclaw.ForwardM2(0x81,0)
    if 'k' in input:
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.HIGH) 
    else:
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)    
    time.sleep(0.01)
