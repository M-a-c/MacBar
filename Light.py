#!/usr/bin/python

import time
from enum import Enum
from Color import Color


class Light(Color):	
	
	def __init__(self):
		super().__init__()
		self.lastSetByUdid = 0
		self.touched = False
	
	def setColor(self, color, udid):
		if (self.written == False):
			self.setColorRBGW(color.r,color.g,color.b,color.w)
			self.touched = True;
			self.lastSetByUdid = udid
		
	def setColorNoUdid(self, color):
		if (self.written == False):
			self.setColorRBGW(color.r,color.g,color.b,color.w)
			self.touched = True;
	
	def resetTouched():
		self.touched = False
				
	def resetLastSetUdid():
		self.lastSetByUdid = 0
		
	def getWrittenStatus(self):
		return self.written	
	
	def invert(self):
		self.invert();
	
		