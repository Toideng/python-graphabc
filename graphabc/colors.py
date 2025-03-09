import random

from .colors_h import *

def ARGB(a: int, r: int, g: int, b: int) -> Color:
	return (r, g, b, a)

def RGB(r: int, g: int, b: int) -> Color:
	return (r, g, b, 0xff)

def RedColor(r: int) -> Color:
	return (r, 0x00, 0x00, 0xff)

def GreenColor(g: int) -> Color:
	return (0x00, g, 0x00, 0xff)

def BlueColor(b: int) -> Color:
	return (0x00, 0x00, b, 0xff)

def clRandom() -> Color:
	return RGB(random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff))

def GetRed(c: Color) -> int:
	return c[0]

def GetGreen(c: Color) -> int:
	return c[1]

def GetBlue(c: Color) -> int:
	return c[2]

def GetAlpha(c: Color) -> int:
	return c[3]
