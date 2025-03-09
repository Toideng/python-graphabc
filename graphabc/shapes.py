import pyray
from typing import Optional
from .colors import *

from .point_h import *
from .pen import *
from .brush import *
from .context import *



# --- Pixels --- #

@UserFunc
def SetPixel(x: int, y: int, c: Color):
#{
	pyray.draw_pixel(x, y, c)

	ctx = get_render_context()
	ctx.pen.X = x
	ctx.pen.Y = y
#}

@UnimplementedFunc
@UserFunc
def GetPixel(x: int, y: int) -> Color:
#{
	pass
#}



# --- Lines --- #

@UserFunc
def LineTo(x: int, y: int, c: Optional[Color] = None):
#{
	ctx = get_render_context()
	if ctx.pen.Style == psClear:
		return

	assert ctx.pen.Style == psSolid and ctx.pen.Width == 1
	if c == None:
		c = ctx.pen.Color

	outline = [
		Point(ctx.pen.X, ctx.pen.Y),
		Point(x, y),
	]

	pyray.draw_line_ex(
		pyray.Vector(outline[0]),
		pyray.Vector(outline[1]),
		ctx.pen.Width,
		c,
	)

	ctx.pen.X = x
	ctx.pen.Y = y
#}

@UserFunc
def Line(x1: int, y1: int, x2: int, y2: int, c: Optional[Color] = None):
#{
	ctx = get_render_context()
	if ctx.pen.Style == psClear:
		return

	assert ctx.pen.Style == psSolid and ctx.pen.Width == 1
	if c == None:
		c = ctx.pen.Color

	outline = [
		Point(x1, y1),
		Point(x2, y2),
	]

	pyray.draw_line_ex(
		pyray.Vector(outline[0]),
		pyray.Vector(outline[1]),
		ctx.pen.Width,
		c,
	)

	ctx.pen.X = x2
	ctx.pen.Y = y2
#}



# --- Circles --- #

@UserFunc
def FillCircle(x: int, y: int, r: int):
#{
	ctx = get_render_context()
	if ctx.brush.Style == bsClear:
		return

	assert ctx.brush.Style == bsSolid

	pyray.draw_circle(x, y, r, ctx.brush.Color)
#}

@UserFunc
def DrawCircle(x: int, y: int, r: int):
#{
	ctx = get_render_context()
	if ctx.pen.Style == psClear:
		return

	assert ctx.pen.Style == psSolid and ctx.pen.Width == 1

	pyray.draw_circle_lines(x, y, r, ctx.pen.Color)
#}

def Circle(x: int, y: int, r: int):
	FillCircle(x, y, r)
	DrawCircle(x, y, r)

@UnimplementedFunc
@UserFunc
def Arc(x: int, y: int, r: int, a1: int, a2: int):
	pass



@UnimplementedFunc
@UserFunc
def FillPie(x: int, y: int, r: int, a1: int, a2: int):
	pass

@UnimplementedFunc
@UserFunc
def DrawPie(x: int, y: int, r: int, a1: int, a2: int):
	pass

def Pie(x: int, y: int, r: int, a1: int, a2: int):
	FillPie(x, y, r, a1, a2)
	DrawPie(x, y, r, a1, a2)



# --- Ellipses --- #

@UnimplementedFunc
@UserFunc
def FillEllipse(x1: int, y1: int, x2: int, y2: int):
	pass

@UnimplementedFunc
@UserFunc
def DrawEllipse(x1: int, y1: int, x2: int, y2: int):
	pass

def Ellipse(x1: int, y1: int, x2: int, y2: int):
	FillEllipse(x1, y1, x2, y2)
	DrawEllipse(x1, y1, x2, y2)



# --- Rectangles --- #

@UnimplementedFunc
@UserFunc
def FillRectangle(x1: int, y1: int, x2: int, y2: int):
	pass

@UnimplementedFunc
@UserFunc
def DrawRectangle(x1: int, y1: int, x2: int, y2: int):
	pass

def Rectangle(x1: int, y1: int, x2: int, y2: int):
	FillRectangle(x1, y1, x2, y2)
	DrawRectangle(x1, y1, x2, y2)



@UnimplementedFunc
@UserFunc
def FillRoundRect(x1: int, y1: int, x2: int, y2: int, w: int, h: int):
	pass

@UnimplementedFunc
@UserFunc
def DrawRoundRect(x1: int, y1: int, x2: int, y2: int, w: int, h: int):
	pass

def RoundRect(x1: int, y1: int, x2: int, y2: int, w: int, h: int):
	FillRoundRect(x1, y1, x2, y2)
	DrawRoundRect(x1, y1, x2, y2)



# --- Generic shapes --- #

@UnimplementedFunc
@UserFunc
def FillClosedCurve(points: list[Point]):
	pass

@UnimplementedFunc
@UserFunc
def DrawClosedCurve(points: list[Point]):
	pass

def ClosedCurve(points: list[Point]):
	FillClosedCurve(points)
	DrawClosedCurve(points)

@UnimplementedFunc
@UserFunc
def Curve(points: list[Point]):
	pass



@UnimplementedFunc
@UserFunc
def FillPolygon(points: list[Point]):
	pass

@UnimplementedFunc
@UserFunc
def DrawPolygon(points: list[Point]):
	pass

def Polygon(points: list[Point]):
	FillPolygon(points)
	DrawPolygon(points)

@UnimplementedFunc
@UserFunc
def Polyline(points: list[Point]):
	pass



# --- Flood fill --- #

@UnimplementedFunc
@UserFunc
def FloodFill(x: int, y: int, c: Color):
	pass



# --- Text drawing --- #

@UnimplementedFunc
@UserFunc
def TextOut(x: int, y: int, s: str):
	pass

@UnimplementedFunc
def DrawTextCentered(x1: int, y1: int, x2: int, y2: int, s: str):
	pass
