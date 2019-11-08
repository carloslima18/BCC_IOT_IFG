from Bussola.bussola import CommandsBussola
from threading import Thread
from gpiozero import PWMOutputDevice
import time

from Ultrassom.UltraSonic import UltraSonic


class Helps(object):
    def __init__(self, gpioMotor=4, tolerancia=8):
        self.gpioMotor = gpioMotor
        self.motor = PWMOutputDevice(self.gpioMotor)
        self.tolerancia = tolerancia
        self.stopped = True

    def andarLinhaReta(self):
        self.stopped = False
        commands = CommandsBussola()
        anguloInicial = commands.getAngle()

        while not self.stopped:
            angle = commands.getAngle()
            print(angle)
            if anguloInicial - self.tolerancia <= angle <= anguloInicial + self.tolerancia:
                self.motor.value = 0.001
            elif anguloInicial + self.tolerancia > 360 or anguloInicial - self.tolerancia < 0:
                if anguloInicial + self.tolerancia > 360:
                    if angle + 360 > anguloInicial + self.tolerancia:
                        self.motor.value = 0.9
                elif anguloInicial - self.tolerancia < 0:
                    if angle - 360 < anguloInicial - self.tolerancia:
                        self.motor.value = 0.9
            else:
                self.motor.value = 0.9

            # print(angle)
            time.sleep(0.1)


bussola = Helps()
ultrassom = UltraSonic()

while True:
    distancia = ultrassom.getDist()
    # TODO: vibra(distancia)

    # TODO: se o botão for pressionado:
    Helps.andarLinhaReta(bussola)
    # TODO: se o botão for pressionado de novo:
    #   Helps.stopped = True
