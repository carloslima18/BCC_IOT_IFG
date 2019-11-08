from Bussola import py_qmc5883l
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
        #Se o ângulo inicial for 350 e a tolerancia for de 15, então o limite é de 335 a 360, e 0 a 5, 
        #porque ao completar a volta o ângulo passa de 360 para 0 -> elif abaixo
        print("VIVINHO")
        motor.value = 0.001
    elif angulo_inicial + tol > 360 or angulo_inicial - tol < 0:
        if angulo_inicial + tol > 360:
            if angle + 360 > angulo_inicial + tol:
                motor.value = 0.9
                print("ATROPELADINHO")
        elif angulo_inicial - tol < 0:
            if angle - 360 < angulo_inicial - tol:
                motor.value = 0.9
                print("ATROPELADINHO")
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
