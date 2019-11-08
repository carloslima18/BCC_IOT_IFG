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

    def getAngleVertical(self):
        (x, y, z) = self.sensor.get_magnet_raw()
        return self.getAngle(z, y)

    def getAngleHorizontal(self):
        (x, y, z) = self.sensor.get_magnet_raw()
        return self.getAngle(x, y)

    def getAngle(self, var1, var2):
        angle = None
        if var1 is not None and var2 is not None:
            # Angle on the var2*var1 plane from magnetic sensor.
            angle = math.atan2(var2, var1)
            if angle < 0:
                angle += 2 * math.pi
            angle = (angle / math.pi) * 180
        return angle

