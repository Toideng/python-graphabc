import pyray
import sys
from typing import Optional
from typing import Any
from .colors_h import *
from .colors import *
from .exports import *

ExportNames('FontStyle')
if sys.version_info >= (3, 12):
	exec('type FontStyle = int')
else:
	class FontStyle(int):
		pass

ExportNames('fsNormal', 'fsBold', 'fsItalic', 'fsUnderline', 'fsBoldItalic', 'fsBoldUnderline',
	'fsItalicUnderline', 'fsBoldItalicUnderline')

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

__all__ = get_local_exports()
