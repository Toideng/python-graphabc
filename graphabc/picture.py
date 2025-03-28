import pyray

from .picture_h import *
from .picture_h import _Picture
from .context import *
from .exports import *

@Export
class Picture(UserObject):
#{
	_attributes_get = ['X', 'Y', 'Width', 'Height']
	_attributes_set = []
	_index_name = 'pictures'
	_parent = _Picture

	@UnimplementedFunc
	def __init__(self, path: str):
	#{
		super().__init__()

		@UserFunc
		def postinit():
		#{
			# Do the loading...
			ctx = get_render_context()
			pic = ctx.pictures[self]
			assert path
			...
			pic.image = pyray.image_copy(pic.image_orig)
		#}

		postinit()
	#}

	@UserFunc
	def Save(self, path: str):
	#{
		# image_from_image -> export_image
		ctx = get_render_context()
		pic = ctx.pictures[self]

		assert pyray.export_image(pic.image, path)
	#}

	@UserFunc
	def Crop(self, x: int, y: int, w: Optional[int] = None, h: Optional[int] = None):
	#{
		ctx = get_render_context()
		pic = ctx.pictures[self]
		W = pic.image.width
		H = pic.image.height

		assert x < W
		assert y < H

		if w == None:
			w = W - x
		if h == None:
			h = H - y

		assert x + w <= W
		assert y + h <= H

		pic.X = x
		pic.Y = y
		pic.Width = w
		pic.Height = h

		pyray.unload_image(pic.image)
		pic.image = pyray.image_from_image(pic.image_orig, (x, y, w, h))
	#}

	@UserFunc
	def Draw(self, x: int, y: int, w: Optional[int] = None, h: Optional[int] = None):
	#{
		ctx = get_render_context()
		pic = ctx.pictures[self]

		resize = False
		if w or h:
			resize = True

		if w == None:
			w = pic.Width
		if h == None:
			w = pic.Height

		tgt = pic.image
		if resize:
		#{
			tgt = pyray.image_copy(tgt)
			pyray.image_resize_nn(tgt, w, h)
		#}

		txt = load_texture_from_image(tgt)

		pyray.draw_texture(txt) # TODO: MXAA

		pyray.unload_texture(txt)
		if resize:
			pyray.unload_image(tgt)
	#}

	@UserFunc
	def FlipHorizontal(self):
	#{
		ctx = get_render_context()
		pic = ctx.pictures[self]
		pyray.image_flip_horizontal(pic.image)
	#}

	@UserFunc
	def FlipVertical(self):
	#{
		ctx = get_render_context()
		pic = ctx.pictures[self]
		pyray.image_flip_vertical(pic.image)
	#}

	@UserFunc
	def GetPixel(self, x: int, y: int) -> Color:
	#{
		ctx = get_render_context()
		pic = ctx.pictures[self]

		assert x < pic.Width
		assert y < pic.Height

		return pyray.get_image_color(pic.image, x, y)
	#}
#}

@UnimplementedFunc
@UserFunc
@Export
def PictureFromScreen() -> Picture:
	pass

__all__ = get_local_exports()
