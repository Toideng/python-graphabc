from .colors_h import *
from .picture_h import _Picture

from typing import Optional

class _Window:
#{
	_usr: object
	Width: int
	Height: int
	IsFixedSize: bool
	Title: str

	smoothing: bool
	drawing_locked: bool
	bgColor: Color
	bgPicture: Optional[_Picture]

	def __init__(self):
	#{
		self.Width = 640
		self.Height = 480
		self.IsFixedSize = True
		self.Title = "GraphABC"

		self.smoothing = True
		self.drawing_locked = False
		#self.bgcolor = cl_DARKGRAY
		self.bgColor = cl_RAYWHITE
		self.bgPicture = None
	#}
#}
