#!/usr/bin/python
	
class Color:	
	
	def __init__(self):
		self.r = 0
		self.g = 0
		self.b = 0
		self.w = 0
		
		self.previousR = 0
		self.previousG = 0
		self.previousB = 0
		self.previousW = 0
		pass

	def saveOldColors(self):
		self.previousR = self.r
		self.previousG = self.g
		self.previousB = self.b
		self.previousW = self.w
	
	def setColorRBGW(self, r, g, b, w):
		self.saveOldColors()
		if(r>255):
			self.r = 255
		elif(r<0):
			self.r = 0
		else:
			self.r = r
			
		if(g>255):
			self.g = 255
		elif(g<0):
			self.g = 0
		else:
			self.g = g
			
		if(b>255):
			self.b = 255
		elif(b<0):
			self.b = 0
		else:
			self.b = b
			
		if(w>255):
			self.w = 255
		elif(w<0):
			self.w = 0
		else:
			self.w = w
	
	def getRGBW(self):
		return [self.r,self.g,self.b,self.w]
		
	def invert(self):
		self.r = 255 - self.r
		self.g = 255 - self.g
		self.b = 255 - self.b
		self.w = 255 - self.w
			
	def getInvertedRGBW(self):
		return [255 - self.r, 255 - self.g, 255 - self.b, 255 - self.w]
	
	def getPreviousRGBW(self):
		return [self.previousR,self.previousG,self.previousB,self.previousW]
		
		
	def printDebug(self):
		print("r: "+str(self.r))
		print("g: "+str(self.g))
		print("b: "+str(self.b))
		print("w: "+str(self.w))
		print("\n")
		pass
	
#	TODO: colors in hsl
#	def setColorHLS(h,l,s):
#		saveOldColors()
#		self.r = r
#		self.g = g
#		self.b = b
#		self.w = w
#
#	def setColorHLSW(h,l,s,w):
#		saveOldColors()
#		self.r = r
#		self.g = g
#		self.b = b
#		self.w = w
#	
#	def getPreviousHSL():
#		return [r,g,b,w]
#	
#	def getPreviousHSLW():
#		return [r,g,b,w]
#	
#	def getBitString():
#		return Bitstring
#

def encodeColor(self):
	# Takes 8 bits of each color (0-255) and packs it into the four bytes
	# needed by the LED controller

	rv = bytearray(4)
	rv[0] = 0b11111111 & self.r
	rv[1] = 0b11111111 & self.g
	rv[2] = 0b11111111 & self.b
	rv[3] = 0b11111111 & self.w

	return rv