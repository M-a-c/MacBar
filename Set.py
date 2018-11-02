#!/usr/bin/python

import time
from Effect import Effect
from enum import Enum
from Color import Color


class Set(Effect):
	
	def __init__(self, lightList, color, start, stop):
		super().__init__(lightList)
		self.color = color
		self.start = start
		self.stop = stop

				
	def step(self):
		if(self.currentStep!=1):
			for pixel in self.lightList:
				pixel.setColor(self.color)
			self.canRemove = True
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