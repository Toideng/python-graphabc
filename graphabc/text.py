from .text_h import *
from .text_h import _Font
from .colors import *
from .context import *
from .exports import *

@Export
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
@Export
def GetFont() -> Font:
	ctx = get_render_context()
	return ctx.font._usr

@UserFunc
@Export
def SetFont(f: Font):
	ctx = get_render_context()
	ctx.font = ctx.fonts[f]



@UserFunc
@Export
def GetFontName() -> str:
	ctx = get_render_context()
	return ctx.font.Name



@UserFunc
@Export
def SetFontColor(c: Color):
	ctx = get_render_context()
	ctx.font.Color = c

@UserFunc
@Export
def GetFontColor() -> Color:
	ctx = get_render_context()
	return ctx.font.Color



@UserFunc
@Export
def SetFontSize(size: int):
	ctx = get_render_context()
	ctx.font.Size = size

@UserFunc
@Export
def GetFontSize() -> int:
	ctx = get_render_context()
	return ctx.font.Size



@UserFunc
@Export
def SetFontStyle(fs: FontStyle):
	ctx = get_render_context()
	ctx.font.Style = fs

@UserFunc
@Export
def GetFontStyle() -> FontStyle:
	ctx = get_render_context()
	return ctx.font.Style



@UnimplementedFunc
@UserFunc
@Export
def TextWidth(s: str):
	pass

@UnimplementedFunc
@UserFunc
@Export
def TextHeight(s: str):
	pass

__all__ = get_local_exports()
