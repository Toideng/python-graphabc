from graphabc import *
import math
import time

from collections.abc import Callable

def PlotFunc(f: Callable[[float], float], xmin: float, xmax: float, ymin: float, ymax: float):
#{
	W = GetWindowWidth()
	H = GetWindowHeight()
	for X in range(W):
	#{
		arg = xmin + (xmax - xmin) * (X+.5)/W
		Y = H * (ymax - f(arg))/(ymax - ymin)
		SetPixel(X, int(Y), clBlue)
		time.sleep(.01)
	#}
#}

PlotFunc(lambda x : math.sin(x),  -math.pi,  math.pi,  -1,  1)
