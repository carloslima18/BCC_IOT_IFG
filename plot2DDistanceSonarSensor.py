



###############3


from __future__ import absolute_import, division, print_function, unicode_literals
from gpiozero import InputDevice, OutputDevice
from time import sleep, time
from math import sin, cos

trig = OutputDevice(4)
echo = InputDevice(17)

sleep(2)

def get_pulse_time():
    trig.on()
    sleep(0.0001)
    trig.off()
    
    pulse_start = 0
    pulse_end_time = 0
    
    while echo.is_active == False:
        pulse_start = time()
        
    while echo.is_active:
        pulse_end_time = time()

    sleep(0.06)
    return pulse_end_time - pulse_start

def calculate_distance(duration):
    velocidade = 343
    dist = velocidade * duration / 2
    # return dist * 100 # transform to meters
    return dist



#dist2 = round(calculate_distance(get_pulse_time()),2)
  
  
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange

x_data, y_data = [], []

figure = pyplot.figure()
line, = pyplot.plot_date(x_data, y_data, '-')


def update(frame):
    x_data.append(datetime.now())
    value = calculate_distance(get_pulse_time())
    if(value>2):
        value = sum(y_data)/len(y_data)
    y_data.append(value)
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,


animation = FuncAnimation(figure, update, interval=200)

pyplot.show()
