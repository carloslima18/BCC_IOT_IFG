import py_qmc5883l
import time
import math
from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
sensor = py_qmc5883l.QMC5883L()
motor = PWMOutputDevice(4)

#sensor.calibration = [[1.030, 0.026, -227.799],
#                     [0.0255, 1.021, 1016.442],
#                     [0.0, 0.0, 1.0]]

def getGrau():
    (x, y, z) = sensor.get_magnet_raw()
    if x is not None and y is not None:
        # Angle on the XY plane from magnetic sensor.
        angle = math.atan2(y, x)
        if angle < 0:
            angle += 2 * math.pi
        angle = (angle/math.pi)*180
    return angle


sensor.declination = 21.3
angulo_inicial = getGrau()
tol = 5

while True:
    angle = getGrau()
    if angulo_inicial - tol <= angle <= angulo_inicial + tol:
        print("VIVINHO")
        motor.value = 0.001
    else:
        motor.value = 0.9
        print("ATROPELADINHO")
        
    #print(angle)
    time.sleep(0.1)

#sensor.get_bearing()
## 87.20
#sensor.declination = 10.02
#sensor.get_bearing()
#
#
#sensor.calibration = [[1.030, 0.026, -227.799],
#                      [0.0255, 1.021, 1016.442],
#                      [0.0, 0.0, 1.0]]
#sensor.get_bearing()