import socket
import keyboard	
import time

UDP_ID = "10.42.0.1"
UDP_PORT=5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    key=""
    if keyboard.is_pressed('w'):
       key += "w"
    if keyboard.is_pressed('s'):
       key += "s"
    if keyboard.is_pressed('a'):
       key += "a"
    if keyboard.is_pressed('d'):
       key += "d"
    if keyboard.is_pressed('i'):
       key += "i"
    if keyboard.is_pressed('k'):
       key += "k"
    if keyboard.is_pressed('l'):
       key += "l"
    sock.sendto(key.encode('utf-8'),(UDP_ID,UDP_PORT))
    print("Sent: "+key)
    time.sleep(0.1)
    