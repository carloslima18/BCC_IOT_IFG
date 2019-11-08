from Bussola import py_qmc5883l
import time
import math
from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
from Bussola.py_qmc5883l import QMC5883L


class CommandsBussola(QMC5883L):
    def __init__(self):
        self.sensor = py_qmc5883l.QMC5883L()
        self.setInclination()

    def setInclination(self, inclination=21.3):
        self.sensor.declination = inclination

    def getAngle(self):
        (x, y, z) = self.sensor.get_magnet_raw()
        angle = None
        if x is not None and y is not None:
            # Angle on the XY plane from magnetic sensor.
            angle = math.atan2(y, x)
            if angle < 0:
                angle += 2 * math.pi
            angle = (angle / math.pi) * 180
        return angle
