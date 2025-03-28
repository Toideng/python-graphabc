from .brush_h import *
from .brush_h import _Brush
from .context import *
from .exports import *

@Export
class Brush(UserObject):
#{
	_attributes_get = ['Color', 'Style', 'Hatch', 'HatchBackgroundColor', 'GradientSecondColor', 'Picture', 'PictureStyle']
	_attributes_set = ['Color', 'Style', 'Hatch', 'HatchBackgroundColor', 'GradientSecondColor', 'Picture', 'PictureStyle']
	_index_name = 'brushes'
	_parent = _Brush
#}



@UserFunc
@Export
def GetBrush() -> Brush:
	ctx = get_render_context()
	b = ctx.brush._usr
	assert type(b) is Brush
	return b

@UserFunc
@Export
def SetBrush(b: Brush):
	ctx = get_render_context()
	_b = ctx.brushes[b]
	ctx.brush = _b



@UserFunc
@Export
def GetBrushColor() -> Color:
	ctx = get_render_context()
	return ctx.brush.Color

@UserFunc
@Export
def SetBrushColor(c: Color):
	ctx = get_render_context()
	ctx.brush.Color = c



@UnimplementedFunc
@UserFunc
@Export
def GetBrushStyle() -> BrushStyle:
	ctx = get_render_context()
	return ctx.brush.Style

@UnimplementedFunc
@UserFunc
@Export
def SetBrushStyle(s: BrushStyle):
	ctx = get_render_context()
	ctx.brush.Style = s



@UnimplementedFunc
@UserFunc
@Export
def GetBrushHatch() -> HatchStyle:
	ctx = get_render_context()
	return ctx.brush.Hatch

@UnimplementedFunc
@UserFunc
@Export
def SetBrushHatch(h: HatchStyle):
	ctx = get_render_context()
	ctx.brush.Hatch = h



@UnimplementedFunc
@UserFunc
@Export
def GetHatchBrushBackgroundColor() -> Color:
	ctx = get_render_context()
	return ctx.brush.HatchBackgroundColor

@UnimplementedFunc
@UserFunc
@Export
def SetHatchBrushBackgroundColor(c: Color):
	ctx = get_render_context()
	ctx.brush.HatchBackgroundColor = c



@UnimplementedFunc
@UserFunc
@Export
def GetGradientBrushSecondColor() -> Color:
	ctx = get_render_context()
	return ctx.brush.GradientSecondColor

@UnimplementedFunc
@UserFunc
@Export
def SetGradientBrushSecondColor(c: Color):
	ctx = get_render_context()
	ctx.brush.GradientSecondColor = c



@UnimplementedFunc
@UserFunc
@Export
def GetBrushPicture():
	ctx = get_render_context()
	p = ctx.brush.Picture
	if p == None:
		return p
	return p._usr

@UnimplementedFunc
@UserFunc
@Export
def SetBrushPicture(p):
	ctx = get_render_context()
	if p != None:
		p = ctx.pictures[p]
	ctx.brush.Picture = p



@UnimplementedFunc
@UserFunc
@Export
def GetBrushPictureStyle() -> BrushPictureStyle:
	ctx = get_render_context()
	return ctx.brush.PictureStyle

@UnimplementedFunc
@UserFunc
@Export
def SetBrushPictureStyle(bps: BrushPictureStyle):
	ctx = get_render_context()
	ctx.brush.PictureStyle = bps

__all__ = get_local_exports()
