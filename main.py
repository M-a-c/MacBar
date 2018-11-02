# Python 2.7.15
#!/usr/bin/env python

# You must have /dev/spidev* devices / bcm2708_spi driver for this to work.
# solid(x1,x2,list, )
# Flickers(x1,x2, color, number-of-pixels-to-randomly-assign, , diration-of-flash, diraiton-of-off, fade-on, fade-off)
# Strobe (x1, x2, color, diration-of-flash, diraiton-of-off, fade-on, fade-off)
# Rotate(LEFT, RIGHT, BOTH) (Sides to do a roate on) happens on the hardware thread just before output so all inputs are ok.

##------- Enable --------#
#from tkinter import *
#DEBUG = True
##-----------------------#

#------- Disable --------#
#import fcntl, array, RPi.GPIO as GPIO
#DEBUG = False
#-----------------------#



#
#   ^   ENABLE THE SCRIPT ABOVE ^
import tornado.websocket
#from tornado.ioloop import IOLoop
#from tornado.locks import Condition
import threading
import tornado.ioloop
import tornado.web
from tornado import gen

import asyncio
import threading
import colorsys
import time #import time, sleep #time libraries 
import math
from enum import Enum

from RotateAllService import RotateAllService

from random import randint
from HardwareController import HardwareController
from DebugWindow import DebugWindow
from Effect import Effect
from Wave import Wave, Direction
from Color import Color
from Light import Light
from util import delay

import sys
if sys.version_info[2] == 5:
    #import realdeal.
    DEBUG = False
else:
    from tkinter import *
    DEBUG = True

### /Configuration ###
## Diagram by Mac Carter
## Here is your pi interface
# with the pins layed out on the board
# =======================================
# |                             o  5v   |
# |                             o  o    |
# |         ---------           o  gnd  |
# |                             o  o    |
# |                             o  o    |
# |                             o  o    |
# |                             o  o    |
# |                             o  o    |
# |                             o  o    |
# |                             Di o    |
# |                             o  o    |
# |                             Ci Ei   |
# |                             o  Li   |
# |                                     |
# |                                     |
# |                                     |
# |                                     |
# |                                     |
# |                                     |
# |                                     |
# |                                     |
# |  __________                         |
# |  |        |                         |
# |  |ETHERNET|                         |
# |  |        |                         |
# ===|--------|====|---------|===========
#                  |===USB===|

### /Configuration ###
 
NUM_LEDS = 144

FONT="Helvetica 8"
# In addition to the hardware SPI pins, we require two general GPIO pins for 
# the enable and latch pins.  It doesn't matter what pins you use
ENABLE_PIN = 8
LATCH_PIN  = 7



class EventLoop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.frame = 0
        self.effects = []
#        self.rotateAllService = RotateAllService(hardwareController)
#        hardwareController.set_hue_rotation(180)
    def run(self):
        delay(2000)
#        The enent loop
        print("here")
#        Runs at ~1.37k+ fps. DAMN. except in tkinter, cause tk sucks.
        while(True):
            for o in self.effects:
                o.step()
#            self.test.step()
            hardwareController.write()
#            delay(200)
#            ResetCalledLeds()
#            Last touched by UDID of init time of obj callee
#            Was Touched LastTickBy YES|NO set by reset or when has been called is boolean.
#            
            
            


class TornadoThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        delay(2000)
        leds[0].setColorRBGW(255,255,255,255)
        hardwareController.write()
        print("Start a tornado")
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.application = tornado.web.Application([(r"/", WebSocketHandler),])
        self.application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()
                
        
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    
#    @tornado.web.asynchronous
#    @gen.coroutine
    def check_origin(self, origin):
        return True

    @tornado.web.asynchronous
    @gen.coroutine
    def open(self):
        i=0

    @tornado.web.asynchronous
    @gen.coroutine
    def on_close(self):
        i=0
        print("connection closed")
        
    @tornado.web.asynchronous
    @gen.coroutine
    def on_message(self,message):
        print(message)
#        print ("message received: {}").format(message)

        messageHeader = message[0]
        
#        print("message header: {}").format(messageHeader)
        if messageHeader == "a":#done
            white = Color()
            white.setColorRBGW(255,255,255,255)
            eventLoop.effects.append(Wave(leds, 71, Direction.BOTH_NO_CENTER, white))
        if messageHeader == "s":#done
            white = Color()
            white.setColorRBGW(0,255,255,255)
            eventLoop.effects.append(Wave(leds, 71, Direction.BOTH_NO_CENTER, white))
        if messageHeader == "d":#done
            white = Color()
            white.setColorRBGW(255,0,255,255)
            eventLoop.effects.append(Wave(leds, 71, Direction.BOTH_NO_CENTER, white))
        if messageHeader == "f":#done
            white = Color()
            white.setColorRBGW(255,255,0,255)
            eventLoop.effects.append(Wave(leds, 71, Direction.BOTH_NO_CENTER, white))
        if messageHeader == "j":#done
            white = Color()
            white.setColorRBGW(0,0,255,255)
            eventLoop.effects.append(Wave(leds, 71, Direction.BOTH_NO_CENTER, white))
        if messageHeader == "k":#done
            white = Color()
            white.setColorRBGW(255,0,0,255)
            eventLoop.effects.append(Wave(leds, 71, Direction.BOTH_NO_CENTER, white))
        if messageHeader == "l":#done
#            white = Color()
#            white.setColorRBGW(0,255,0,255)
#            eventLoop.effects.append(Wave(leds, 71, Direction.BOTH_NO_CENTER, white))
            hardwareController.set_hue_rotation(90)
        if messageHeader == ";":#done
#            white = Color()
#            white.setColorRBGW(0,0,0,255)
#            eventLoop.effects.append(Wave(leds, 71, Direction.BOTH_NO_CENTER, white))
            hardwareController.set_hue_rotation(180)
#        if messageHeader == "000":#done
#            static(message)
#        if messageHeader == "100":#Enable threading
#            pass
#        if messageHeader == "200":#Still searching for a library
#            pass
#        if messageHeader == "300":#Enable threading
#            pass
#        if messageHeader == "400":#Enable threading
#            pass
#        if messageHeader == "500":#Search for a good distribution of light colors
#            pass
#        if messageHeader == "600":#search for a good distibution of random in and out clouds.
#            pass
        if message == "NumberOfLights()":#done
            self.write_message(str(NUM_LEDS))

            
        else:
            self.write_message(str("command not understood"))

#        FlashAllRedPattern();#incorrect command.


if __name__ == "__main__":
    global leds
    leds = [ Light() for i in range(NUM_LEDS)]
    global hardwareController
    global window
    global tkWindow
    global effectList
    global rotation
    
    if DEBUG:
        tkWindow = Tk()
        window = Canvas(tkWindow, width=1200, height=480)
    else:
        window=0
    
    hardwareController = HardwareController(leds,window)
    tornadoThread = TornadoThread()
    tornadoThread.start()
    eventLoop = EventLoop()
    eventLoop.start()

    #open the SPI device for writing
    if DEBUG:
        n = 0
        while(n<NUM_LEDS):
            pos = (n+1)
            x1 = 7
            y1 = 7
            window.create_rectangle((x1*pos), 10, (y1*pos)+10, 300, fill="yellow", tags ="Light_"+str(pos))
            window.create_text((x1*pos)+5, y1+10 , text=str(pos), fill="purple", font=FONT, tags = "Text_"+str(pos))
            n = n+1
        window.pack(side="top", fill="both", expand=True)
        tkWindow.mainloop()
