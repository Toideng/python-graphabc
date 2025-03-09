import pyray
from typing import Optional
from typing import Any
from .colors import *

type FontStyle = int

fsNormal    : FontStyle = 0
fsBold      : FontStyle = 1 << 0
fsItalic    : FontStyle = 1 << 1
fsUnderline : FontStyle = 1 << 2

fsBoldItalic          : FontStyle = fsBold | fsItalic
fsBoldUnderline       : FontStyle = fsBold | fsUnderline
fsItalicUnderline     : FontStyle = fsItalic | fsUnderline
fsBoldItalicUnderline : FontStyle = fsBold | fsItalic | fsUnderline

class _Font:
#{
	_usr: object
	Color: Color
	Size: int
	Style: FontStyle
	Name: str
	Font: pyray.Font

	def __init__(self):
	#{
		self.Color = clNONE
		self.Size = 0
		self.Style = fsNormal
		self.Name = '<none>'
		self.Font = None
	#}
#}
