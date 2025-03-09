import graphabc

def click_cb(x, y, mb):
	graphabc.Circle(x, y, 10)

graphabc.SetOnMouseDown(click_cb)
