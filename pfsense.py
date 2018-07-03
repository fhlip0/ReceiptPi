#!/usr/bin/python

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

printer.println("test")

printer.printLN("	"                               " ")
printer.printLN("	"                               " ")
printer.printLN("	"                               " ")
printer.printLN("	"                 ______        " ")
printer.printLN("	"                /      \       " ")
printer.printLN("	"          _____/    f   \      " ")
printer.printLN("	"         /     \        /      " ")
printer.printLN("	"        /   p   \______/  Sense" ")
printer.printLN("	"        \       /      \       " ")
printer.printLN("	"         \_____/        \      " ")
printer.printLN("	"               \        /      " ")
printer.printLN("	"                \______/       " ")
printer.printLN("	"                               " ")
printer.printLN("	"                               " ")
printer.printLN("	"                               " ")
