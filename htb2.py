#!/usr/bin/python

import os
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
os.system('./rank.sh')
printer.println("")
str = open('/home/pi/rank', 'r').read()
printer.println("*********************")
printer.println("HackTheBox: fhlipZero")
printer.println("Hacker")
printer.println(str)
printer.println("")