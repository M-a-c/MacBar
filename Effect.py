#!/usr/bin/python
import time
from abc import ABCMeta, abstractmethod

class Effect:
	__metaclass__ = ABCMeta
	
	def __init__(self):
		self.active = False
		self.canRemove = False
		self.startTime = 0.0
		self.endTime = 0.0
		self.currentStep = int(0)
		self.endAtStep = int(0)
		self.udid = time.time()
		
	def __del__(self):
		print('Effect Base Removed')
		
#	@abstractmethod
	def step(self):
		self.currentStep = self.currentStep + 1
		pass
	
	# default behavior resets the time to start NOW and have the same duration as it did last time.
	# default behavior resets steps to 0 and will have the same # of steps as the previous run.
	@abstractmethod
	def reset(self):
		temp = float(self.endTime - self.startTime)
		self.startTime = float(time.time())
		self.endTime = float(self.startTime + temp)
		self.currentStep = int(0)
		pass
	
	def getActive(self):
		return self.active
	
	def setActive(self, _active):
		self.active = _active	
		
	def setMsTillStartWithNoEnd(self, startIn):
		self.startTime = float(time.time() + float(startIn))

	def setMsTillStartAndRunTime(self, startIn, runTime):
		self.startTime = float(time.time() + float(startIn))
		self.endTime = float(time.time() + float(startIn) + float(runTime))
		
	def getMsTillStartAndEnd(self):
		return [self.startTime, self.endTime]
	
	def setStep(self, _currentStep):
		self.currentStep = _currentStep
		
	def getEndStep(self):
		return self.currentStep
	
	def setEndStep(self, endStep):
		self.endAtStep = endStep
		
	def getEndStep(self, endStep):
		return self.endAtStep
