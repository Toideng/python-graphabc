import random

from .colors_h import *
from .exports import *

@Export
def ARGB(a: int, r: int, g: int, b: int) -> Color:
	return (r, g, b, a)

@Export
def RGB(r: int, g: int, b: int) -> Color:
	return (r, g, b, 0xff)

@Export
def RedColor(r: int) -> Color:
	return (r, 0x00, 0x00, 0xff)

@Export
def GreenColor(g: int) -> Color:
	return (0x00, g, 0x00, 0xff)

@Export
def BlueColor(b: int) -> Color:
	return (0x00, 0x00, b, 0xff)

@Export
def clRandom() -> Color:
	return RGB(random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff))

@Export
def GetRed(c: Color) -> int:
	return c[0]

@Export
def GetGreen(c: Color) -> int:
	return c[1]

@Export
def GetBlue(c: Color) -> int:
	return c[2]

@Export
def GetAlpha(c: Color) -> int:
	return c[3]

__all__ = get_local_exports()
