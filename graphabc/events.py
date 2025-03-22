from .keys_h import *
from .mouse_h import *
from .context import *
from collections.abc import Callable

from typing import Optional

@UserFunc
def SetOnKeyDown(cb: Optional[Callable[[KeyboardKey], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnKeyDown = cb

@UserFunc
def SetOnKeyUp(cb: Optional[Callable[[KeyboardKey], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnKeyUp = cb



@UserFunc
def SetOnMouseDown(cb: Optional[Callable[[int, int, MouseButton], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnMouseDown = cb

@UserFunc
def SetOnMouseUp(cb: Optional[Callable[[int, int, MouseButton], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnMouseUp = cb

@UserFunc
def SetOnMouseMove(cb: Optional[Callable[[int, int, MouseButtonMap], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnMouseMove = cb



@UnimplementedFunc
@UserFunc
def SetOnResize(cb: Optional[Callable[[None], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnResize = cb

@UserFunc
def SetOnClose(cb: Optional[Callable[[None], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnClose = cb
