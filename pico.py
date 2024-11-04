from machine import I2C, Pin
from pca9685 import PCA9685
import time

#servos
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
pca = PCA9685(i2c)
pca.set_pwm_freq(50)
def move_servo(channel, angle):
    print(f"Moving servo on channel {channel} to {angle} degrees")
    pca.set_servo_angle(channel, angle)
   
#movements
def rest():
    move_servo(0,95)
    move_servo(1,90)
    move_servo(2,95)
    move_servo(3,90)
    move_servo(4,0)
    move_servo(5,170)
    move_servo(6,5)
    move_servo(7,170)
    
def stand():
    move_servo(4,40)
    move_servo(5,125)
    move_servo(6,45)
    move_servo(7,125)
    time.sleep(2)
    move_servo(0,40)
    move_servo(1,145)
    move_servo(2,45)
    move_servo(3,140)
    move_servo(4,105)
    move_servo(5,65)
    move_servo(6,110)
    move_servo(7,65)

def walk():
    move_servo(1,165)#145
    move_servo(5,85)#65
    move_servo(2,25)#45
    move_servo(6,90)#110 
    
def head():
    move_servo(15,99)
    


#main
while True:
    dowhat = input("what")
    if dowhat == "r":
        rest()
    elif dowhat == "s":
        stand()
    elif dowhat == "w":
        walk()

    
