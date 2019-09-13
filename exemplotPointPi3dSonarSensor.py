from __future__ import absolute_import, division, print_function, unicode_literals
from gpiozero import InputDevice, OutputDevice
from time import sleep, time
from math import sin, cos
import pi3d

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

DISPLAY = pi3d.Display.create( frames_per_second=30)
DISPLAY.set_background(0,0,0,1)     # r,g,b,alpha
light = pi3d.Light(lightpos=(1.0, 0.0, 0.1))

mysphere = pi3d.Sphere(radius=0.10, slices=24, sides=24,
                  name="earth" , z=5.8)

#myPoint = pi3d.Points(material=(1.0, 1.0, 1.0),
#                      point_size=1, name="point",x=0.5, y=0.5, z=0.5)



mykeys = pi3d.Keyboard()

# Display scene

dist = round(calculate_distance(get_pulse_time()),2)
x = 0
y = 0

#while True:
while DISPLAY.loop_running():
  
  dist2 = round(calculate_distance(get_pulse_time()),2)
  
  print("DIST1:  " + str(dist) + " DIST2:  " + str(dist2))
  
  if dist2 == dist or abs(dist2-dist) <= 0.0:
    y = y # para fins didaticos
  elif(dist2 > dist):
    y = y + 0.10
  else:
    y = y - 0.10
    
  dist = round(calculate_distance(get_pulse_time()),2)
  mysphere.position(y,0,5.8)
  
  mysphere.draw()
  
  # print(calculate_distance(get_pulse_time()))

  x = x+ 0.01
  k = mykeys.read()
  if k >-1:
    if k==67:
      x =x + 0.8
    elif k==27:
      mykeys.close()
      DISPLAY.stop()
      break

    
    
