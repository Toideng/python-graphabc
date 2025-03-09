import graphabc
import time

graphabc.SetBrushColor(graphabc.clMaroon)
graphabc.SetPenColor(graphabc.clMaroon)

for x in range(60):
	for y in range(44):
		graphabc.Circle(20 + x * 10, 20 + y * 10, 3)
		#time.sleep(.3)
