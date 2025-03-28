import pyray
from typing import Optional
from .colors import *

from .point_h import *
from .pen_h import *
from .pen import *
from .brush_h import *
from .brush import *
from .context import *
from .exports import *



# Combined SetPenColor + SetBrushColor

@Export
def SetColor(c: Color):
	SetPenColor(c)
	SetBrushColor(c)



# --- Pixels --- #

@UserFunc
@Export
def SetPixel(x: int, y: int, c: Color):
#{
	pyray.draw_pixel(x, y, c)

	ctx = get_render_context()
	ctx.pen.X = x
	ctx.pen.Y = y
#}

@UnimplementedFunc
@UserFunc
@Export
def GetPixel(x: int, y: int) -> Color:
#{
	pass
#}



# --- Lines --- #

@UserFunc
@Export
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
		outline[0],
		outline[1],
		ctx.pen.Width,
		c,
	)

	ctx.pen.X = x
	ctx.pen.Y = y
#}

@UserFunc
@Export
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
		outline[0],
		outline[1],
		ctx.pen.Width,
		c,
	)

	ctx.pen.X = x2
	ctx.pen.Y = y2
#}



# --- Circles --- #

@UserFunc
@Export
def FillCircle(x: int, y: int, r: int):
#{
	ctx = get_render_context()
	if ctx.brush.Style == bsClear:
		return

	assert ctx.brush.Style == bsSolid

	pyray.draw_circle(x, y, r, ctx.brush.Color)
#}

@UserFunc
@Export
def DrawCircle(x: int, y: int, r: int):
#{
	ctx = get_render_context()
	if ctx.pen.Style == psClear:
		return

	assert ctx.pen.Style == psSolid and ctx.pen.Width == 1

	pyray.draw_circle_lines(x, y, r, ctx.pen.Color)
#}

@Export
def Circle(x: int, y: int, r: int):
	FillCircle(x, y, r)
	DrawCircle(x, y, r)

@UnimplementedFunc
@UserFunc
@Export
def Arc(x: int, y: int, r: int, a1: int, a2: int):
	pass



@UnimplementedFunc
@UserFunc
@Export
def FillPie(x: int, y: int, r: int, a1: int, a2: int):
	pass

@UnimplementedFunc
@UserFunc
@Export
def DrawPie(x: int, y: int, r: int, a1: int, a2: int):
	pass

@Export
def Pie(x: int, y: int, r: int, a1: int, a2: int):
	FillPie(x, y, r, a1, a2)
	DrawPie(x, y, r, a1, a2)



# --- Ellipses --- #

@UnimplementedFunc
@UserFunc
@Export
def FillEllipse(x1: int, y1: int, x2: int, y2: int):
	pass

@UnimplementedFunc
@UserFunc
@Export
def DrawEllipse(x1: int, y1: int, x2: int, y2: int):
	pass

@Export
def Ellipse(x1: int, y1: int, x2: int, y2: int):
	FillEllipse(x1, y1, x2, y2)
	DrawEllipse(x1, y1, x2, y2)



# --- Rectangles --- #

@UserFunc
@Export
def FillRectangle(x1: int, y1: int, x2: int, y2: int):
#{
	ctx = get_render_context()
	if ctx.brush.Style == bsClear:
		return

	assert ctx.brush.Style == bsSolid

	pyray.draw_rectangle(x1, y1, x2 - x1, y2 - y1, ctx.brush.Color)
#}

@UserFunc
@Export
def DrawRectangle(x1: int, y1: int, x2: int, y2: int):
#{
	ctx = get_render_context()
	if ctx.pen.Style == psClear:
		return

	assert ctx.pen.Style == psSolid and ctx.pen.Width == 1

	pyray.draw_rectangle_lines(x1, y1, x2 - x1, y2 - y1, ctx.pen.Color)
#}

@Export
def Rectangle(x1: int, y1: int, x2: int, y2: int):
	FillRectangle(x1, y1, x2, y2)
	DrawRectangle(x1, y1, x2, y2)



@UnimplementedFunc
@UserFunc
@Export
def FillRoundRect(x1: int, y1: int, x2: int, y2: int, w: int, h: int):
	pass

@UnimplementedFunc
@UserFunc
@Export
def DrawRoundRect(x1: int, y1: int, x2: int, y2: int, w: int, h: int):
	pass

@Export
def RoundRect(x1: int, y1: int, x2: int, y2: int, w: int, h: int):
	FillRoundRect(x1, y1, x2, y2)
	DrawRoundRect(x1, y1, x2, y2)



# --- Generic shapes --- #

@UserFunc
@Export
def FillTriangle(p1: Point, p2: Point, p3: Point):
#{
	ctx = get_render_context()
	if ctx.brush.Style == bsClear:
		return

	assert ctx.brush.Style == bsSolid

	dx1, dy1 = p2.x - p1.x, p2.y - p1.y
	dx2, dy2 = p3.x - p1.x, p3.y - p1.y
	if dx1 * dy2 - dy1 * dx2 > 0:
		# Raylib requires points of a triangle to be in the counter-clockwise order
		p2, p3 = p3, p2

	pyray.draw_triangle(p1, p2, p3, ctx.brush.Color)
#}

@UserFunc
@Export
def DrawTriangle(p1: Point, p2: Point, p3: Point):
#{
	ctx = get_render_context()
	if ctx.pen.Style == psClear:
		return

	assert ctx.pen.Style == psSolid and ctx.pen.Width == 1

	pyray.draw_triangle_lines(p1, p2, p3, ctx.pen.Color)
#}

@Export
def Triangle(p1: Point, p2: Point, p3: Point):
	FillTriangle(p1, p2, p3)
	DrawTriangle(p1, p2, p3)



@UnimplementedFunc
@UserFunc
@Export
def FillClosedCurve(points: list[Point]):
	pass

@UnimplementedFunc
@UserFunc
@Export
def DrawClosedCurve(points: list[Point]):
	pass

@Export
def ClosedCurve(points: list[Point]):
	FillClosedCurve(points)
	DrawClosedCurve(points)

@UnimplementedFunc
@UserFunc
@Export
def Curve(points: list[Point]):
	pass



@UnimplementedFunc
@UserFunc
@Export
def FillPolygon(points: list[Point]):
	pass

@UnimplementedFunc
@UserFunc
@Export
def DrawPolygon(points: list[Point]):
	pass

@Export
def Polygon(points: list[Point]):
	FillPolygon(points)
	DrawPolygon(points)

@UnimplementedFunc
@UserFunc
@Export
def Polyline(points: list[Point]):
	pass



# --- Flood fill --- #

@UnimplementedFunc
@UserFunc
@Export
def FloodFill(x: int, y: int, c: Color):
	pass



# --- Text drawing --- #

@UnimplementedFunc
@UserFunc
@Export
def TextOut(x: int, y: int, s: str):
	pass

@UnimplementedFunc
@Export
def DrawTextCentered(x1: int, y1: int, x2: int, y2: int, s: str):
	pass

__all__ = get_local_exports()
