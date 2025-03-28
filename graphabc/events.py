from .keys_h import *
from .mouse_h import *
from .context import *
from .exports import *
from collections.abc import Callable

from typing import Optional

@UserFunc
@Export
def SetOnMouseDown(cb: Optional[Callable[[int, int, MouseButton], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnMouseDown = cb

@UserFunc
@Export
def SetOnMouseUp(cb: Optional[Callable[[int, int, MouseButton], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnMouseUp = cb

@UserFunc
@Export
def SetOnMouseMove(cb: Optional[Callable[[int, int, MouseButtonMap], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnMouseMove = cb



@UserFunc
@Export
def SetOnKeyDown(cb: Optional[Callable[[KeyboardKey], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnKeyDown = cb

@UserFunc
@Export
def SetOnKeyUp(cb: Optional[Callable[[KeyboardKey], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnKeyUp = cb



@UnimplementedFunc
@UserFunc
@Export
def SetOnResize(cb: Optional[Callable[[None], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnResize = cb

@UserFunc
@Export
def SetOnClose(cb: Optional[Callable[[None], None]]):
	ctx = get_render_context()
	ctx.events_ctx.OnClose = cb

__all__ = get_local_exports()
