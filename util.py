#!/usr/bin/python
import time #import time, sleep #time libraries 
from Light import Light


def delay(number):
	time.time()
	time.sleep(float(number)/1000.0)#convert seconds to miliseconds
	pass

def reset(LightList):
	for light in LightList:
		light.resetTouched();