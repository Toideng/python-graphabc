from .pen_h import *
from .pen_h import _Pen
from .context import *
from .exports import *

@Export
class Pen(UserObject):
#{
	_attributes_get = ['Color', 'Style', 'Width', 'X', 'Y']
	_attributes_set = ['Color', 'Style', 'Width', 'X', 'Y']
	_index_name = 'pens'
	_parent = _Pen
#}

@UserFunc
@Export
def GetPen() -> Pen:
	ctx = get_render_context()
	p = ctx.pen._usr
	assert type(p) is Pen
	return p

@UserFunc
@Export
def SetPen(p: Pen):
	ctx = get_render_context()
	_p = ctx.pens[p]
	ctx.pen = _p



@UserFunc
@Export
def GetPenColor() -> Color:
	ctx = get_render_context()
	return ctx.pen.Color

@UserFunc
@Export
def SetPenColor(c: Color):
	ctx = get_render_context()
	ctx.pen.Color = c



@UserFunc
@Export
def GetPenStyle() -> PenStyle:
	ctx = get_render_context()
	return ctx.pen.Style

@UnimplementedFunc
@UserFunc
@Export
def SetPenStyle(s: PenStyle):
	ctx = get_render_context()
	ctx.pen.Style = s



@UserFunc
@Export
def GetPenWidth() -> int:
	ctx = get_render_context()
	return int(ctx.pen.Width)

@UnimplementedFunc
@UserFunc
@Export
def SetPenWidth(w: int):
	ctx = get_render_context()
	ctx.pen.Width = w



@UserFunc
@Export
def PenX() -> int:
	ctx = get_render_context()
	return int(ctx.pen.X)

@UserFunc
@Export
def PenY() -> int:
	ctx = get_render_context()
	return int(ctx.pen.Y)



@UserFunc
@Export
def MoveTo(x: int, y: int):
	ctx = get_render_context()
	ctx.pen.X = x
	ctx.pen.Y = y

__all__ = get_local_exports()
