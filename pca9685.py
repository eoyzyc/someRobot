from machine import I2C
import time

class PCA9685:
    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self.reset()

    def reset(self):
        self.write_reg(0x00, 0x00)

    def write_reg(self, reg, value):
        self.i2c.writeto_mem(self.address, reg, bytes([value]))

    def set_pwm_freq(self, freq):
        prescale_val = int(25000000.0 / (4096.0 * freq) - 1)
        old_mode = int.from_bytes(self.i2c.readfrom_mem(self.address, 0x00, 1), 'big')
        new_mode = (old_mode & 0x7F) | 0x10
        self.write_reg(0x00, new_mode)
        self.write_reg(0xFE, prescale_val)
        self.write_reg(0x00, old_mode)
        time.sleep_ms(5)
        self.write_reg(0x00, old_mode | 0xa1)

    def set_pwm(self, channel, on, off):
        self.i2c.writeto_mem(self.address, 0x06 + 4 * channel, bytes([on & 0xFF, on >> 8, off & 0xFF, off >> 8]))

    def set_servo_angle(self, channel, angle):
        pulse_width = int((angle * 2.2755) + 102)
        self.set_pwm(channel, 0, pulse_width)
