from graphabc import *

def click_cb(x, y, mb):
	if mb != MB_Left:
		return
	SetColor(clRandom())
	MoveTo(x, y)
	Circle(x, y, 30)

def move_cb(x, y, mbm):
	if not mbm & MBM_Left:
		return
	SetColor(clRandom())
	LineTo(x, y)
	Circle(x, y, 12)

SetOnMouseDown(click_cb)
SetOnMouseMove(move_cb)
