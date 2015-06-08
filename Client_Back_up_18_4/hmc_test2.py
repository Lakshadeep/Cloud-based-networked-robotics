

import smbus
import time

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

DEVICE_ADDRESS = 0x1e      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE = 0x02
DEVICE_REG_CONFIG_A = 0x00
DEVICE_REG_CONFIG_B = 0x01

# initialisation
def initialisation():
	bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_CONFIG_A, 0x70)
	bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_CONFIG_B, 0x20)
	bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE, 0x00)


def bearing255():
        bear = bus.read_byte_data(DEVICE_ADDRESS, 1)
        return bear


def bearingx3599():
        bearx1 = bus.read_byte_data(DEVICE_ADDRESS, 0x02)
        bearx2 = bus.read_byte_data(DEVICE_ADDRESS, 0x03)
	bearx = (bearx1 << 8) + bearx2
	bearx = bearx/10.0
        return bearx

def bearingy3599():
	beary1 = bus.read_byte_data(DEVICE_ADDRESS, 0x02)
        beary2 = bus.read_byte_data(DEVICE_ADDRESS, 0x03)
	beary = (beary1 << 8) + beary2
	beary = beary/10.0
        return beary

def bearingz3599():
	bearz1 = bus.read_byte_data(DEVICE_ADDRESS, 0x02)
        bearz2 = bus.read_byte_data(DEVICE_ADDRESS, 0x03)
        bearz = (bearz1 << 8) + bearz2
        bearz = bearz/10.0
        return bearz


# Write an array of registers
# ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
# bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)


while True:
	initialisation()
	time.sleep(1)
        bearingx = bearingx3599()     #this returns the value to 1 decimal place in degrees. 
	bearingy = bearingy3599() 
	bearingz = bearingz3599() 
        #bear255 = bearing255()      #this returns the value as a byte between 0 and 255. 
        print bearingx
	print bearingy
	print bearingz
        #print bear255
        time.sleep(1)