#!/usr/bin/env python
# External module imports
import RPi.GPIO as GPIO
import time, sys, json, requests
import max7219.led as led

pin1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(pin1, GPIO.OUT)


def limpaTela():
        for j in range(8):
                for k in range(8):
                        matrix.pixel(k,j,0,False)


def imprimeX():
	limpaTela()
	l = 7;
	for i in range(8):
		matrix.pixel(i,i,1,False)
		if(i < 7):
			matrix.pixel(l,i,1,False)
		else:
			matrix.pixel(l,i,1)
		l = l-1


matrix = led.matrix()
retorno = requests.get("http://10.1.2.30/almoco/CRT/ajax/travaCatraca.php")

if retorno.status_code == 200 :
	retornoJSON = json.loads(retorno.content)
	if retornoJSON["catracaBloqueada"] == 1:
		GPIO.output(pin1, GPIO.LOW)
		if retornoJSON["isX"] == 1:
			imprimeX()
	else:
		GPIO.output(pin1, GPIO.HIGH)
		limpaTela()
else:
	GPIO.output(pin1, GPIO.HIGH)
