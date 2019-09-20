#!/usr/bin/python3

import smbus
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
map = plt.figure()
map_ax = Axes3D(map)
map_ax.autoscale(enable=True, axis='both', tight=True)


# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, 0x19, 7)
bus.write_byte_data(address, 0x6B, 1)
bus.write_byte_data(address, 0x1A, 0)
bus.write_byte_data(address, 0x1B, 24)
bus.write_byte_data(address, 0x38, 1)
xs = []
ys = []
zs = []
# # # Setting the axes properties
map_ax.set_xlim3d([-1000.0, 1000.0])
map_ax.set_ylim3d([-1000.0, 1000.0])
map_ax.set_zlim3d([-1000.0, 1000.0])
hl, = map_ax.plot3D([0], [0], [0])

def update_line(hl,gyro_xout,gyro_yout,gyro_zout):
    xdata, ydata, zdata = hl._verts3d
    hl.set_xdata(list(np.append(xdata, gyro_xout)))
    hl.set_ydata(list(np.append(ydata, gyro_yout)))
    hl.set_3d_properties(list(np.append(zdata, gyro_zout)))
    plt.draw()

while True:
    time.sleep(0.1)
    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

    print ("gyro_xout : ", gyro_xout, " scaled: ", (gyro_xout / 131))
    print ("gyro_yout : ", gyro_yout, " scaled: ", (gyro_yout / 131))
    print ("gyro_zout : ", gyro_zout, " scaled: ", (gyro_zout / 131))
    xs.append(gyro_xout)
    ys.append(gyro_xout)
    xs.append(gyro_xout)
    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    accel_xout_scaled = accel_xout / 16384.0
    accel_yout_scaled = accel_yout / 16384.0
    accel_zout_scaled = accel_zout / 16384.0

    print ("accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled)
    print ("accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled)
    print ("accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled)

    print ("x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
    print ("y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
    update_line(hl,gyro_xout, gyro_yout, gyro_zout)
    plt.show(block=False)
    plt.pause(1)

    time.sleep(0.2)
