#!/usr/bin/env python
 
import max7219.led as led
import max7219.canvas as canvas
import time
 
font5x3 = { # python data type dictionary for the pixelfont
    "0" : [0b01110, 0b10001, 0b01110], # "0"
    "1" : [0b10010, 0b11111, 0b10000], # "1"
    "2" : [0b11001, 0b10101, 0b10010], # "2"
    "3" : [0b10001, 0b10101, 0b01110], # "3"
    "4" : [0b01110, 0b01000, 0b11111], # "4"
    "5" : [0b10111, 0b10101, 0b01001], # "5"
    "6" : [0b01110, 0b10101, 0b01000], # "6"
    "7" : [0b10001, 0b01001, 0b00111], # "7"
    "8" : [0b01010, 0b10101, 0b01010], # "8"
    "9" : [0b00010, 0b10101, 0b01110], # "9"
    ":" : [0b01010], # ":"
    "-" : [0b00100, 0b00100, 0b00100], # "-"
    "|" : [      0], # one blank line
    " " : [      0,       0,       0] # space
    } # create additional letters
 
def creatematrix(text):
    text = str(text)
    matrix = []
    for i in range(len(text)): # write complete pixelmatrix in a buffer
        if text[i].upper() in font5x3: # check if dictionary entry exists
            matrix = matrix + font5x3[text[i].upper()] # add letter; upper()
            matrix = matrix + [0] # add separator/space
    return matrix
 
def drawmatrix(matrix, up=0, left=0):
    for i in range(8): # fill the 8x8 matrix buffer canvas.gfxbuf
        if up < 0:
        	canvas.gfxbuf[i] = matrix[(i + left) % len(matrix)] << abs(up) # move down
        else:
    		canvas.gfxbuf[i] = matrix[(i + left) % len(matrix)] >> abs(up)
 
led.init()
horz = 0
vert = -2
speed = 15
led.brightness(0) # 0, 3, 7, 15 seems to work
 
while True:
    m = creatematrix(time.strftime("%k:%M ")) # write temporary matrix m
    horz = (horz + 1) % len(m) # scroll left
    drawmatrix(m, vert, horz) # draw 8x8 frame into gfxbuf 
    canvas.render() # draw gfxbuf into matrix
    time.sleep( 1.0 / speed ) # pause