from .window_h import _Window
from .context import *

@UnimplementedFunc
@UserFunc
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
def SetSmoothing(on: bool):
#{
	ctx = get_render_context()
	ctx.win.smoothing = on
#}

def SetSmoothingOn():
	SetSmoothing(True)

def SetSmoothingOff():
	SetSmoothing(False)

@UserFunc
def SmoothingIsOn() -> bool:
#{
	ctx = get_render_context()
	return ctx.win.smoothing
#}



@UserFunc
def GetWindowTitle() -> int:
	ctx = get_render_context()
	return ctx.window.Title

@UserFunc
def GetWindowWidth() -> int:
	ctx = get_render_context()
	return ctx.window.Width

@UserFunc
def GetWindowHeight() -> int:
	ctx = get_render_context()
	return ctx.window.Height
