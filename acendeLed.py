from gpiozero import LED
print ('Alo mundo')
led = LED(17)
import time
for i in range(10):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
#led.off()
