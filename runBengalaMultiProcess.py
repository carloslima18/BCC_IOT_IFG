import multiprocessing 
import time 
  
def func(number): 
    from gpiozero import LED
    led = LED(17)
    import time
    for i in range(5):
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)
  
# list of all processes
all_processes = [] 
  

process = multiprocessing.Process(target=func, args=(1,)) 
process.start() 
all_processes.append(process) 
  
while(True):
    time.sleep(10) 
    process.terminate()
    process = multiprocessing.Process(target=func, args=(1,)) 
