from graphabc import *
import random
import time

_Triangle = tuple[Point, Point, Point]

def random_triangle() -> _Triangle:
#{
	w = GetWindowWidth()
	h = GetWindowHeight()
	return (
		Point(random.randint(0, w-1), random.randint(0, h-1)),
		Point(random.randint(0, w-1), random.randint(0, h-1)),
		Point(random.randint(0, w-1), random.randint(0, h-1)),
	)
#}

for i in range(20):
#{
	SetPenColor(clRandom())
	SetBrushColor(clRandom())
	p1, p2, p3 = random_triangle()
	Triangle(p1, p2, p3)
	time.sleep(.2)
#}
