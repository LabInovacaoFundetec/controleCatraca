#!/usr/bin/env python
# External module imports
import RPi.GPIO as GPIO
import time, sys, json, requests

pin1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(pin1, GPIO.OUT)

retorno = requests.get("http://10.1.2.30/almoco/CRT/ajax/travaCatraca.php")

if retorno.status_code == 200 :
	retornoJSON = json.loads(retorno.content)
	if retornoJSON["catracaBloqueada"] == 1:
		GPIO.output(pin1, GPIO.LOW)
	else:
		GPIO.output(pin1, GPIO.HIGH)
else:
	GPIO.output(pin1, GPIO.HIGH)