from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
from time import os, sleep, time


class Vibration(object):
	def __init__(self):
		self.motor0 = PWMOutputDevice(6)
		self.motor1 = PWMOutputDevice(24)
		self.motor2 = PWMOutputDevice(19)
		self.motor3 = PWMOutputDevice(26)
		self.vibracao_total = 0.9
		self.vibracao_total = 0.5
		self.obstaculo_proximo = 0.2 # ~0.5 metros 
		self.distancia_media = 0.5 # ~2 metros
		self.distancia_longa = 0.7 # ~3 metros


	def olhando_frente(self, distancia_corrente):
		#objeto esta proximo, realiza vibração forte continua no motor 0 por 2 segundo 
		if(distancia_corrente <= obstaculo_proximo):
			motor0.value = vibracao_total
			time.sleep(200)
		#objeto esta a uma distancia média, fara 2 vibrações fortes(por meio segundo cada) em intervalos de 0.05 segundo entre ambas. 
		elif(distancia_corrente <= distancia_media and distancia_corrente > obstaculo_proximo):
			motor0.value = vibracao_total
			time.sleep(500)
			motor0.value = 0
			time.sleep(50)
			motor0.value = vibracao_total
			time.sleep(500)
			motor0.value = 0
		#se o objeto esta a uma distancia longa, realizará uma vibração(média) no motor 3, de modo continuo
		elif(distancia_corrente >= distancia_longa):
			motor0.value = vibracao_media
		# se não tiver nada em frente.
		elif
			motor0.value = 0
	
	#entre 0 e 1,, onde 0 esta em linha, reta... e de acordo que se aproxima de 1! esta se desviando da linha reta.
	def emite_vibracao_linha_reta(self, distancia):
		motor1.value = round(distancia,2)
	
	#entre 0 e 1 (1 é pq tem um buraco grande)
	def olhando_chao(self, distancia):
		motor2.value = round(distancia,2)

		


        