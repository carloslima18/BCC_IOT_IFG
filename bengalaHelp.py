from Bussola.bussola import CommandsBussola
from Ultrassom.UltraSonic import UltraSonic
from SensorVibracao.vibracaoMotor import Vibration
from gpiozero import PWMOutputDevice
import time


class Helps(object):
    def __init__(self, gpioMotor=4, tolerancia=8):
        self.gpioMotor = gpioMotor
        self.motor = PWMOutputDevice(self.gpioMotor)
        self.tolerancia = tolerancia
        self.stopped = True
        self.commands = CommandsBussola()

    def getVariation(self, anguloInicial):

        angle = self.commands.getAngleHorizontal()

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

    def run(self):
        ultrassom = UltraSonic()
        respostaTatil = Vibration()
        botaoPressionado = True

        while True:
            distancia = ultrassom.getDist()
            if botaoPressionado:
                anguloInicial = self.commands.getAngleHorizontal()
                vibrationValue = self.getVariation(anguloInicial)
                respostaTatil.emite_vibracao_linha_reta(vibrationValue)
            respostaTatil.olhando_frente(distancia)
            # anguloVertical = self.commands.getAngleVertical()
            time.sleep(0.1)
