#!/usr/bin/python

from tkinter import *
from enum import Enum
import threading
#import fcntl, array, RPi.GPIO as GPIO
FONT="Helvetica 8"

class DebugWindow():
	def __init__(self, DEBUG, LED_LIST, tkWindow, window):
		self.DEBUG = DEBUG

		if(DEBUG):
			self.tkWindow = tkWindow
			print(self.tkWindow)
			self.window = window
			self.test = 0
			self.LED_LIST = LED_LIST
			self.NUM_LEDS = len(LED_LIST)

			#open the SPI device for writing
			n = 0
			while(n<self.NUM_LEDS):
				pos = (n+1)
				x1 = 7
				y1 = 7
				self.window.create_rectangle((x1*pos), 10, (y1*pos)+10, 300, fill="yellow", tags ="Light_"+str(pos))
				self.window.create_text((x1*pos)+5, y1+10 , text=str(pos), fill="purple", font=FONT, tags = "Text_"+str(pos))
				n = n+1
				self.window.pack(side="top", fill="both", expand=True)
				self.tkwindow.mainloop()
	
	def run(self):
		if (self.DEBUG):
			self.window.pack(side="top", fill="both", expand=True)
			self.tkwindow.mainloop()
	