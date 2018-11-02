#!/usr/bin/python

import time
from Effect import Effect
from enum import Enum
from Color import Color

#enum if possible
class Direction(Enum):
	LEFT = 0
	RIGHT = 1
	BOTH = 2
	BOTH_NO_CENTER = 3

# TODO: IMPLEMENT ACITONS ON COLLIDING
#class onCollide(Enum):
#	BOUCE = 0
#	DIE_ON_FIRST = 1
#	DIE_ON_LAST = 2
#	DIE_ON_EDIT_COLLISION_FIRST = 3 HARD TO DO
#	DIE_ON_EDIT_COLLISION_LAST = 4 HARD TO DO
#	BOUCE_ON_EDIT_COLLISION = 5 HARD TO DO


class Wave(Effect):
	
	def __init__(self, lightList, currentPixel, direction, color):
		super(Wave, self).__init__()
		self.udid = time.time()		
		self.color = color;
		self.currentPixel = currentPixel
		self.opositeDirecitonPixel = currentPixel
		self.startAtPixel = 0
		self.endAtPixel = len(lightList)
		self.direction = direction
		self.lightList = lightList


	def setStartPixel(self, pixelNo):
		if(pixelNo > len(lightList) - 1 ):
			self.currentPixel = len(lightList) - 1
		elif(pixelNo < 0):
			self.currentPixel = 0
		else: 
			self.currentPixel = pixelNo
		
		
		self.opositeDirecitonPixel = self.currentPixel
		
	def right(self):
		if(self.currentPixel < self.endAtPixel):
			self.lightList[self.currentPixel].setColor(self.color,self.udid)
			self.currentPixel = self.currentPixel + 1
	def left(self):
		if(self.opositeDirecitonPixel != -1):
			self.lightList[self.opositeDirecitonPixel].setColor(self.color,self.udid)
			self.opositeDirecitonPixel = self.opositeDirecitonPixel - 1
	def both(self):
		self.right()
		self.left()
	
	def step(self):
		if(self.direction == Direction.LEFT):
			self.left()
			
		elif(self.direction == Direction.RIGHT):
			self.right()
			
		elif(self.direction == Direction.BOTH):
			if(self.step == 0): # start in the middle.
				self.right()
				self.opositeDirecitonPixel = self.opositeDirecitonPixel - 1
			else:
				self.both()
					
		elif(self.direction == Direction.BOTH_NO_CENTER):
			self.both()
				
		super(Wave, self).step() 
		pass
		
	
	def reset(self):
		temp = float(self.endTime - self.startTime)
		self.startTime = float(time.time())
		self.endTime = float(self.startTime + temp)
		self.currentStep = int(0)
		self.endAtPixel = len(lightList)
		pass
		
	def __del__(self):
		print('Wave Removed')
