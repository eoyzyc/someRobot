from machine import I2C, Pin
from pca9685 import PCA9685
import time

# Initialize I2C
i2c = I2C(1, scl=Pin(3), sda=Pin(2))

# Initialize PCA9685
pca = PCA9685(i2c)
pca.frequency = 50  # 50Hz for servos/motors

# Control motor on channel 0
motor_channel = pca.channels[0]

# Define motor speed function (duty cycle 0-100%)
def set_motor_speed(speed):
    if speed > 100:
        speed = 100
    elif speed < 0:
        speed = 0
    duty_cycle = int(speed * 65535 / 100)
    motor_channel.duty_cycle = duty_cycle

# Example usage
while True:
    set_motor_speed(50)  # Set motor to 50% speed
    time.sleep(2)
    set_motor_speed(100)  # Set motor to 100% speed
    time.sleep(2)
    set_motor_speed(0)  # Stop motor
    time.sleep(2)