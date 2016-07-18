#!/usr/bin/env python
# External module imports
import RPi.GPIO as GPIO
import time, sys
import max7219.led as led

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

matrix = led.matrix()

imprimeX()