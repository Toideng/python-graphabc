from .pen_h import *
from .pen_h import _Pen
from .context import *

class Pen(UserObject):
#{
	_attributes_get = ['Color', 'Style', 'Width', 'X', 'Y']
	_attributes_set = ['Color', 'Style', 'Width', 'X', 'Y']
	_index_name = 'pens'
	_parent = _Pen
#}

@UserFunc
def GetPen() -> Pen:
	ctx = get_render_context()
	p = ctx.pen._usr
	assert type(p) is Pen
	return p

@UserFunc
def SetPen(p: Pen):
	ctx = get_render_context()
	_p = ctx.pens[p]
	ctx.pen = _p



@UserFunc
def GetPenColor() -> Color:
	ctx = get_render_context()
	return ctx.pen.Color

@UserFunc
def SetPenColor(c: Color):
	ctx = get_render_context()
	ctx.pen.Color = c



@UnimplementedFunc
@UserFunc
def GetPenStyle() -> PenStyle:
	ctx = get_render_context()
	return ctx.pen.Style

@UnimplementedFunc
@UserFunc
def SetPenStyle(s: PenStyle):
	ctx = get_render_context()
	ctx.pen.Style = s



@UnimplementedFunc
@UserFunc
def GetPenWidth() -> int:
	ctx = get_render_context()
	return int(ctx.pen.Width)

@UnimplementedFunc
@UserFunc
def SetPenWidth(w: int):
	ctx = get_render_context()
	ctx.pen.Width = w



@UserFunc
def PenX() -> int:
	ctx = get_render_context()
	return int(ctx.pen.X)

@UserFunc
def PenY() -> int:
	ctx = get_render_context()
	return int(ctx.pen.Y)



@UserFunc
def MoveTo(x: int, y: int):
	ctx = get_render_context()
	ctx.pen.X = x
	ctx.pen.Y = y
