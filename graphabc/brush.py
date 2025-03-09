from .brush_h import *
from .brush_h import _Brush
from .context import *

class Brush(UserObject):
#{
	_attributes_get = ['Color', 'Style', 'Hatch', 'HatchBackgroundColor', 'GradientSecondColor', 'Picture', 'PictureStyle']
	_attributes_set = ['Color', 'Style', 'Hatch', 'HatchBackgroundColor', 'GradientSecondColor', 'Picture', 'PictureStyle']
	_index_name = 'brushes'
	_parent = _Brush
#}



@UserFunc
def GetBrush() -> Brush:
	ctx = get_render_context()
	b = ctx.brush._usr
	assert type(b) is Brush
	return b

@UserFunc
def SetBrush(b: Brush):
	ctx = get_render_context()
	_b = ctx.brushes[b]
	ctx.brush = _b



@UserFunc
def GetBrushColor() -> Color:
	ctx = get_render_context()
	return ctx.brush.Color

@UserFunc
def SetBrushColor(c: Color):
	ctx = get_render_context()
	ctx.brush.Color = c



@UnimplementedFunc
@UserFunc
def GetBrushStyle() -> BrushStyle:
	ctx = get_render_context()
	return ctx.brush.Style

@UnimplementedFunc
@UserFunc
def SetBrushStyle(s: BrushStyle):
	ctx = get_render_context()
	ctx.brush.Style = s



@UnimplementedFunc
@UserFunc
def GetBrushHatch() -> HatchStyle:
	ctx = get_render_context()
	return ctx.brush.Hatch

@UnimplementedFunc
@UserFunc
def SetBrushHatch(h: HatchStyle):
	ctx = get_render_context()
	ctx.brush.Hatch = h



@UnimplementedFunc
@UserFunc
def GetHatchBrushBackgroundColor() -> Color:
	ctx = get_render_context()
	return ctx.brush.HatchBackgroundColor

@UnimplementedFunc
@UserFunc
def SetHatchBrushBackgroundColor(c: Color):
	ctx = get_render_context()
	ctx.brush.HatchBackgroundColor = c



@UnimplementedFunc
@UserFunc
def GetGradientBrushSecondColor() -> Color:
	ctx = get_render_context()
	return ctx.brush.GradientSecondColor

@UnimplementedFunc
@UserFunc
def SetGradientBrushSecondColor(c: Color):
	ctx = get_render_context()
	ctx.brush.GradientSecondColor = c



@UnimplementedFunc
@UserFunc
def GetBrushPicture():
	ctx = get_render_context()
	p = ctx.brush.Picture
	if p == None:
		return p
	return p._usr

@UnimplementedFunc
@UserFunc
def SetBrushPicture(p):
	ctx = get_render_context()
	if p != None:
		p = ctx.pictures[p]
	ctx.brush.Picture = p



@UnimplementedFunc
@UserFunc
def GetBrushPictureStyle() -> BrushPictureStyle:
	ctx = get_render_context()
	return ctx.brush.PictureStyle

@UnimplementedFunc
@UserFunc
def SetBrushPictureStyle(bps: BrushPictureStyle):
	ctx = get_render_context()
	ctx.brush.PictureStyle = bps
