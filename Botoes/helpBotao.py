from gpiozero import LED, InputDevice
import time


def getEstado(gpio=21):
    botao = InputDevice(21)
    # led = LED(26)

    estado = "desligado"
    # while True:
    if not botao.is_active:
        if estado == "desligado":
            # led.on()
            estado = "ligado"
            return 1
        else:
            # led.off()
            estado = "desligado"
            return 0
