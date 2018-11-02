#!/usr/bin/python

import time
from Effect import Effect
from enum import Enum
from Color import Color

class FadeType(Enum):
	NONE = 0
	FADE_IN = 1
	FADE_IN_AND_OUT = 2

class RotateAllService(Effect):
	
	def __init__(self, hardWareController):
		super().__init__(lightList)
		self.degrees
		self.OldDegrees
				
	def step(self):
		if(self.currentStep!=1):
			for pixel in self.lightList:
				pixel.setColor(self.color)
			canRemove = True
		super.step()
		pass
		
	
	def reset(self):
		temp = float(self.endTime - self.startTime)
		self.startTime = float(time.time())
		self.endTime = float(self.startTime + temp)
		self.currentStep = int(0)
		pass
		
	def __del__(self):
		print ("Set Removed")