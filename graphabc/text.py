from .text_h import *
from .text_h import _Font
from .colors import *
from .context import *

class Font(UserObject):
#{
	_attributes_set = ['Color', 'Size', 'Style']
	_attributes_get = ['Color', 'Size', 'Style', 'Name']
	_index_name = 'fonts'
	_parent = _Font

	def __init__(self, name: str):
	#{
		super().__init__()

		@UserFunc
		def postinit():
		#{
			# Do the loading...
			ctx = get_render_context()
			font = ctx.fonts[self]
			assert name
		#}

		postinit()
	#}
#}



@UserFunc
def GetFont() -> Font:
	ctx = get_render_context()
	return ctx.font._usr

@UserFunc
def SetFont(f: Font):
	ctx = get_render_context()
	ctx.font = ctx.fonts[f]



@UserFunc
def GetFontName() -> str:
	ctx = get_render_context()
	return ctx.font.Name



@UserFunc
def SetFontColor(c: Color):
	ctx = get_render_context()
	ctx.font.Color = c

@UserFunc
def GetFontColor() -> Color:
	ctx = get_render_context()
	return ctx.font.Color



@UserFunc
def SetFontSize(size: int):
	ctx = get_render_context()
	ctx.font.Size = size

@UserFunc
def GetFontSize() -> int:
	ctx = get_render_context()
	return ctx.font.Size



@UserFunc
def SetFontStyle(fs: FontStyle):
	ctx = get_render_context()
	ctx.font.Style = fs

@UserFunc
def GetFontStyle() -> FontStyle:
	ctx = get_render_context()
	return ctx.font.Style



@UnimplementedFunc
@UserFunc
def TextWidth(s: str):
	pass

@UnimplementedFunc
@UserFunc
def TextHeight(s: str):
	pass
