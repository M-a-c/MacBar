#!/usr/bin/python
from math import sqrt,cos,sin,radians
from tkinter import *
from enum import Enum
import colorsys
import time
from util import delay


import sys
if sys.version_info[2] == 5:
	import board
	import neopixel
	DEBUG = False
	# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
	# NeoPixels must be connected to D10, D12, D18 or D21 to work.
	pixel_pin = board.D18

	# The number of NeoPixels
	num_pixels = 144

	# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
	# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
	ORDER = neopixel.GRB

	pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False,
										pixel_order=ORDER)
else:
	from tkinter import *
	DEBUG = True

#import fcntl, array, RPi.GPIO as GPIO
FONT="Helvetica 8"

class HardwareController():
	def __init__(self, LED_LIST, window):
		self.window = window
		self.test = 0
		self.LED_LIST = LED_LIST
		self.NUM_LEDS = len(LED_LIST)
		self.rotation = 0
		
		self.matrix = [[1,0,0],[0,1,0],[0,0,1]]

		#open the SPI device for writing

		if(not DEBUG):
			pass
#			spidev = file("/dev/spidev0.0", "wb")
#
#			#set the speed of the SPI bus, 5000000 == 5mhz  
#			#Magic number below is from spidev.h SPI_IOC_WR_MAX_SPEED_HZ
#			#TODO: can I reference this as a constant from termios?
#			fcntl.ioctl(spidev, 0x40046b04, array.array('L', [6000000]))
#
#			#setup our GPIO
#			GPIO.setwarnings(False)
#			GPIO.setmode(GPIO.BCM)
#			GPIO.setup(ENABLE_PIN, GPIO.OUT)
#			GPIO.setup(LATCH_PIN, GPIO.OUT)
#
#			#both pins low to start
#			GPIO.output(LATCH_PIN, 0)
#			GPIO.output(ENABLE_PIN, 0)
	
	
	def clamp(self,v):
		if v < 0:
			return 0
		if v > 255:
			return 255
		return int(v + 0.5)

	def set_hue_rotation(self, degrees):
		self.rotation = degrees
		cosA = cos(radians(degrees))
		sinA = sin(radians(degrees))
		self.matrix[0][0] = cosA + (1.0 - cosA) / 3.0
		self.matrix[0][1] = 1./3. * (1.0 - cosA) - sqrt(1./3.) * sinA
		self.matrix[0][2] = 1./3. * (1.0 - cosA) + sqrt(1./3.) * sinA
		self.matrix[1][0] = 1./3. * (1.0 - cosA) + sqrt(1./3.) * sinA
		self.matrix[1][1] = cosA + 1./3.*(1.0 - cosA)
		self.matrix[1][2] = 1./3. * (1.0 - cosA) - sqrt(1./3.) * sinA
		self.matrix[2][0] = 1./3. * (1.0 - cosA) - sqrt(1./3.) * sinA
		self.matrix[2][1] = 1./3. * (1.0 - cosA) + sqrt(1./3.) * sinA
		self.matrix[2][2] = cosA + 1./3. * (1.0 - cosA)

	def apply(self, r, g, b):
		rx = r * self.matrix[0][0] + g * self.matrix[0][1] + b * self.matrix[0][2]
		gx = r * self.matrix[1][0] + g * self.matrix[1][1] + b * self.matrix[1][2]
		bx = r * self.matrix[2][0] + g * self.matrix[2][1] + b * self.matrix[2][2]
		return self.clamp(rx), self.clamp(gx), self.clamp(bx)

	def write(self):
		for index, light in enumerate(self.LED_LIST):
			num =  index + 1
			red8Bit = 0
			green8Bit = 0
			blue8Bit = 0
			white8Bit = light.w
			
			if(self.rotation == 0):
				red8Bit = light.r
				green8Bit = light.g
				blue8Bit = light.b
			else:
				red8Bit,green8Bit,blue8Bit = self.apply(light.r,light.g,light.b)
		
			if (DEBUG):
				red8BitInverse = 255 - red8Bit
				green8BitInverse = 255 - green8Bit
				blue8BitInverse = 255 - blue8Bit

				red8BitHex = "{:02x}".format(red8Bit)
				green8BitHex = "{:02x}".format(green8Bit)
				blue8BitHex = "{:02x}".format(blue8Bit)
				fillColor = "#" + str(red8BitHex) + str(green8BitHex) + str(blue8BitHex)
				
				red8BitInverse = "{:02x}".format(red8BitInverse)
				green8BitInverse = "{:02x}".format(green8BitInverse)
				blue8BitInverse = "{:02x}".format(blue8BitInverse)
				fillColorInverse = "#" + str(red8BitInverse) + str(green8BitInverse) + str(blue8BitInverse)

				string = "Light_" + str(num)
				stringTwo = "Text_" + str(num)
				self.window.itemconfig(string, fill=fillColor)
				self.window.itemconfig(stringTwo, fill=fillColorInverse)
			else:
				pixels[index] = (green8Bit, blue8Bit, red8Bit, white8Bit)
		if (not DEBUG):
			pixels.show()

		
	def set_led():
		pass
		# """helper function to quickly set an LED color
#		if DEBUG:
#			drawLed(num,r,g,b)
#			pass