import pyray

from .keys_h import *
from .mouse_h import *

from typing import Optional
from collections.abc import Callable

class _Event:
#{
	to: Optional[float]
	f: Optional[Callable]
	close_cmd: bool

	def __init__(self, f: Optional[Callable], timeout: Optional[float] = 0, close: bool = False):
	#{
		if timeout is None:
			self.to = None;
		else:
			self.to = pyray.get_time() + (timeout or .1);
		self.f = f;
		self.close_cmd = close;
	#}
#}

class _EventsCtx:
#{
	OnKeyDown: Optional[Callable[[KeyboardKey], None]] = None
	OnKeyUp: Optional[Callable[[KeyboardKey], None]] = None

	OnMouseDown: Optional[Callable[[int, int, MouseButton], None]]
	OnMouseUp: Optional[Callable[[int, int, MouseButton], None]]
	OnMouseMove: Optional[Callable[[int, int, MouseButtonMap], None]]

	OnResize: Optional[Callable[[None], None]]
	OnClose: Optional[Callable[[None], None]]

	_mouse_pos: tuple[int, int]
	_mouse: MouseButtonMap
	_keys: set[KeyboardKey]

	def __init__(self):
	#{
		self._mouse = 0
		self._keys = set()
		self.OnKeyDown = None
		self.OnKeyUp = None

		self.OnMouseDown = None
		self.OnMouseUp = None
		self.OnMouseMove = None

		self.OnResize = None
		self.OnClose = None
	#}
#}
