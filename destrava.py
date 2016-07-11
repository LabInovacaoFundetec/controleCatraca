#!/usr/bin/env python
# External module imports
import RPi.GPIO as GPIO
import time, sys
import max7219.led as led

# Pin Definitons:
pin1 = 14 
pin2 = 15
pin3 = 18
pin4 = 17
in1 = 27
ledOk = 22

dDin = 22
dCS = 23
dCLK = 24

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

def limpaTela():
	for j in range(8):
		for k in range(8):
			matrix.pixel(k,j,0,False)

def imprimeSeta(momento = 14):
	limpaTela()
	#Neste vetor esta assim [y,x]
	#m = [[0,3],[0,4],[1,2],[1,3],[1,4],[1,5],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[4,3],[4,4],[5,3],[5,4],[6,3],[6,4],[7,3],[7,4]]
	m = [[3,0],[4,0],[2,1],[3,1],[4,1],[5,1],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[3,4],[4,4],[3,5],[4,5],[3,6],[4,6],[3,7],[4,7]]
	#m = [[3,7],[4,7],[2,6],[3,6],[4,6],[5,6],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[0,4],[1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[3,3],[4,3],[3,2],[4,2],[3,1],[4,1],[3,0],[4,0]]
	i = 0
	"""
	if momento == 0:
		for d in m:
			if i < 27:
				matrix.pixel(d[0],d[1],1, False)
			else:
				matrix.pixel(d[0],d[1],1)
	else:
		matrix.scroll_up(False)

	"""
	if momento == 0:
		for d in m:
			if i < 27:
				matrix.pixel(d[0],d[1],1, False)
			else:
				matrix.pixel(d[0],d[1],1)
			i = i + 1
	if momento >= 1 and momento <= 7:
		for d in m:
			if d[1] > momento - 1:
				if i < 27:
					matrix.pixel(d[0],d[1] - momento,1, False)
				else:
					matrix.pixel(d[0],d[1] - momento,1)
			i = i + 1
	if momento == 8:
		matrix.pixel(0,0,0)
	if momento == 9:
		for d in m:
			if d[1] < 1:
				if i < 1:
					matrix.pixel(d[0],d[1] + 7,1,False)
				else:
					matrix.pixel(d[0],d[1] + 7,1)
			i = i + 1
	if momento == 10:
		for d in m:
			if d[1] < 2:
				if i < 5:
					matrix.pixel(d[0],d[1] + 6,1,False)
				else:
					matrix.pixel(d[0],d[1] + 6,1)
			i = i + 1
	if momento == 11:
		for d in m:
			if d[1] < 3:
				if i < 11:
					matrix.pixel(d[0],d[1] + 5,1,False)
				else:
					matrix.pixel(d[0],d[1] + 5,1)
			i = i + 1
	if momento == 12:
		for d in m:
			if d[1] < 4:
				if i < 19:
					matrix.pixel(d[0],d[1] + 4,1,False)
				else:
					matrix.pixel(d[0],d[1] + 4,1)
			i = i + 1
	if momento == 13:
		for d in m:
			if d[1] < 5:
				if i < 21:
					matrix.pixel(d[0],d[1] + 3,1,False)
				else:
					matrix.pixel(d[0],d[1] + 3,1)
			i = i + 1
	if momento == 14:
		for d in m:
			if d[1] < 6:
				if i < 23:
					matrix.pixel(d[0],d[1] + 2,1,False)
				else:
					matrix.pixel(d[0],d[1] + 2,1)
			i = i + 1
	if momento == 15:
		for d in m:
			if d[1] < 7:
				if i < 25:
					matrix.pixel(d[0],d[1] + 1,1,False)
				else:
					matrix.pixel(d[0],d[1] + 1,1)
			i = i + 1
	



matrix = led.matrix()

GPIO.setwarnings(False)
# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT) 
GPIO.setup(ledOk, GPIO.OUT) 
GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.output(pin1, GPIO.LOW) # LED pin set as output
GPIO.output(pin2, GPIO.HIGH) # LED pin set as output
GPIO.output(pin3, GPIO.HIGH) # LED pin set as output
GPIO.output(pin4, GPIO.HIGH) # LED pin set as output
GPIO.output(ledOk, GPIO.LOW) # LED pin set as output


i = 0;

mo = 0;
while 1:
	if not GPIO.input(in1) or i == 200:
		GPIO.output(pin1, GPIO.HIGH) # LED pin set as output
		GPIO.output(ledOk, GPIO.HIGH) # LED pin set as output
		imprimeX()
		sys.exit(0)
	imprimeSeta(mo)
	if mo < 15:
		mo = mo + 1;
	else:
		mo = 0
	i = i + 1;
	time.sleep(0.07)
