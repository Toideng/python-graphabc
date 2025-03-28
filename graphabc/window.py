from .window_h import _Window
from .context import *
from .exports import *

@UserFunc
@Export
def GetWindowTitle() -> int:
	ctx = get_render_context()
	return ctx.window.Title

@UserFunc
@Export
def GetWindowWidth() -> int:
	ctx = get_render_context()
	return ctx.window.Width

@UserFunc
@Export
def GetWindowHeight() -> int:
	ctx = get_render_context()
	return ctx.window.Height



@UnimplementedFunc
@UserFunc
@Export
def Redraw():
#{
	ctx = get_render_context()
	win = ctx.window
	if not win.drawing_locked:
		return

	pyray.end_texture_mode()
	pyray.begin_texture_mode(ctx.fbo)
	pyray.draw_texture(ctx.fbo_back.texture, 0, 0, clWhite)
	pyray.end_texture_mode()
	pyray.begin_texture_mode(ctx.fbo_back)
#}

@UnimplementedFunc
@UserFunc
@Export
def LockDrawing():
#{
	ctx = get_render_context()
	win = ctx.window
	if win.drawing_locked:
		return
	win.drawing_locked = True

	pyray.end_texture_mode()
	pyray.begin_texture_mode(ctx.fbo_back)
	pyray.draw_texture(ctx.fbo.texture, 0, 0, clWhite)
#}

@UnimplementedFunc
@UserFunc
@Export
def UnlockDrawing():
#{
	ctx = get_render_context()
	win = ctx.window
	if not win.drawing_locked:
		return
	win.drawing_locked = False

	pyray.end_texture_mode()
	pyray.begin_texture_mode(ctx.fbo)
	pyray.draw_texture(ctx.fbo_back.texture, 0, 0, clWhite)
#}



@UnimplementedFunc
@UserFunc
@Export
def SetSmoothing(on: bool):
#{
	ctx = get_render_context()
	ctx.win.smoothing = on
#}

@Export
def SetSmoothingOn():
	SetSmoothing(True)

@Export
def SetSmoothingOff():
	SetSmoothing(False)

@UserFunc
@Export
def SmoothingIsOn() -> bool:
#{
	ctx = get_render_context()
	return ctx.win.smoothing
#}

__all__ = get_local_exports()
