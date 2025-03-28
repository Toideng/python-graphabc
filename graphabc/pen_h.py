from enum import IntEnum
from typing import Optional
from .colors_h import *
from .colors import *
from .exports import *

@Export
class PenStyle(IntEnum):
#{
	Clear      = 0
	Solid      = 1
	Dash       = 2
	Dot        = 3
	DashDot    = 4
	DashDotDot = 5
#}

ExportNames('psClear', 'psSolid', 'psDash', 'psDot', 'psDashDot', 'psDashDotDot')
psClear      = PenStyle.Clear
psSolid      = PenStyle.Solid
psDash       = PenStyle.Dash
psDot        = PenStyle.Dot
psDashDot    = PenStyle.DashDot
psDashDotDot = PenStyle.DashDotDot

class _Pen:
#{
	Color: Color
	Style: PenStyle
	Width: float
	X: float
	Y: float
	_advance: float

	def __init__(self,
			color: Color = clBlack,
			style: PenStyle = psSolid,
			width: float = 1,
			x: float = 0,
			y: float = 0,
		):
	#{
		self.Color = color
		self.Style = style
		self.Width = width
		self.X = x
		self.Y = y
		self._advance = 0
	#}
#}

__all__ = get_local_exports()
