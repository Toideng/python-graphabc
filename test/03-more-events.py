from graphabc import *

R = 10.

def draw(x, y):
	global R
	R *= 1.05
	SetPenColor(clRandom())
	SetBrushColor(clRandom())
	Circle(x, y, int(R))

def click_cb(x, y, mb):
	if mb != MB_Left:
		return
	draw(x, y)

def move_cb(x, y, mbm):
	if not mbm & MBM_Left:
		return
	draw(x, y)

SetOnMouseDown(click_cb)
SetOnMouseMove(move_cb)
