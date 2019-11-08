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

    def getVariation(self, anguloInicial):

        commands = CommandsBussola()
        angle = commands.getAngle()

        torelanciaAnterior = self.tolerancia
        vibracao = 0
        numVariacoes = 5
        variacaoVibracao = 1 / numVariacoes - 0.01
        variacaoTolerancia = 10
        for i in range(numVariacoes):
            if anguloInicial - self.tolerancia <= angle <= anguloInicial + self.tolerancia:
                self.tolerancia = torelanciaAnterior
                return vibracao
            elif anguloInicial + self.tolerancia > 360 or anguloInicial - self.tolerancia < 0:
                if anguloInicial + self.tolerancia > 360:
                    if angle + 360 > anguloInicial + self.tolerancia:
                        vibracao += variacaoVibracao
                        self.tolerancia += variacaoTolerancia
                elif anguloInicial - self.tolerancia < 0:
                    if angle - 360 < anguloInicial - self.tolerancia:
                        vibracao += variacaoVibracao
                        self.tolerancia += variacaoTolerancia
            else:
                vibracao += variacaoVibracao
                self.tolerancia += variacaoTolerancia

        self.tolerancia = torelanciaAnterior
        return vibracao

        # def andarLinhaReta(self):
        #     self.stopped = False
        #     commands = CommandsBussola()
        #     anguloInicial = commands.getAngle()
        #
        #     while not self.stopped:
        #         angle = commands.getAngle()
        #         print(angle)
        #         if anguloInicial - self.tolerancia <= angle <= anguloInicial + self.tolerancia:
        #             self.motor.value = 0.001
        #         elif anguloInicial + self.tolerancia > 360 or anguloInicial - self.tolerancia < 0:
        #             if anguloInicial + self.tolerancia > 360:
        #                 if angle + 360 > anguloInicial + self.tolerancia:
        #                     self.motor.value = 0.9
        #             elif anguloInicial - self.tolerancia < 0:
        #                 if angle - 360 < anguloInicial - self.tolerancia:
        #                     self.motor.value = 0.9
        #         else:
        #             self.motor.value = 0.9
        #
        #         # print(angle)
        #         time.sleep(0.1)

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
