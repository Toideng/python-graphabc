import pyray
import threading
import queue

from .render_funnel_h import *
from .colors_h import *
from .keys_h import *
from .mouse_h import *
from .events_h import _EventsCtx, _Event
from .brush_h import _Brush
from .pen_h import _Pen
from .picture_h import _Picture
from .text_h import _Font
from .window_h import _Window

from collections.abc import Callable
from typing import Any
from typing import Optional
from typing import Union

class Main_Context:
#{
	tls: threading.local
	crashed: threading.Event  # Main thread has crashed, stop execution
	started: threading.Event  # Render thread has started, proceed with main code

	event_queue: queue.Queue[_Event]

	render_funnel: RenderFunnel

	def __init__(self):
	#{
		self.tls = threading.local()
		self.crashed = threading.Event()
		self.started = threading.Event()
		self.event_queue = queue.Queue()
		self.render_funnel = RenderFunnel()
	#}
#}

main_context = Main_Context()

class _Render_Context:
#{
	fbo: pyray.RenderTexture
	fbo_back: pyray.RenderTexture # For locked drawing

	events_ctx: _EventsCtx

	brushes:  dict[object, _Brush]
	pens:     dict[object, _Pen]
	fonts:    dict[object, _Font]
	pictures: dict[object, _Picture]

	fonts_cache: dict[str, Any]
	image_cache: dict[Union[str, object], pyray.Image] # Picture might be taken from screen,
	                                                   # in which case it doesn't have a source

	brush: _Brush
	pen: _Pen
	font: _Font
	window: _Window

	def __init__(self):
	#{
		self.events_ctx = _EventsCtx()

		self.brushes = dict()
		self.pens = dict()
		self.pictures = dict()
		self.fonts = dict()

		self.fonts_cache = dict()
		self.image_cache = dict()

		self.window = _Window()
	#}
#}

def get_render_context() -> _Render_Context:
#{
	global main_context
	tls = main_context.tls
	assert hasattr(tls, 'GraphABC_ctx')
	ctx = getattr(tls, 'GraphABC_ctx')
	assert type(ctx) is _Render_Context
	return ctx
#}



def UnimplementedFunc(f: Callable):
#{
	def closure_static(*args, **kwargs):
		raise Exception('Not implemented:', f.__name__)
	return closure_static;
#}



def _RenderFunc(f: Callable):
#{
	def closure_static(*args, **kwargs):
	#{
		get_render_context()
		return f(*args, **kwargs)
	#}
	return closure_static;
#}



def UserFunc(f: Callable):
#{
	global main_context
	def closure_static(*args, **kwargs):
	#{
		assert not hasattr(main_context.tls, 'GraphABC_ctx');

		@_RenderFunc
		def closure_dynamic():
			return f(*args, **kwargs);

		res = main_context.render_funnel.user_send(closure_dynamic);
		return res;
	#}
	return closure_static;
#}



class UserObject:
#{
	_attributes: list[str]
	_index_name: str
	_parent: type

	def __init__(self):
	#{
		global main_context
		assert type(self) is not UserObject   # abstract class
		assert not hasattr(main_context.tls, 'GraphABC_ctx')

		def closure():
		#{
			ctx = get_render_context()

			index = getattr(ctx, self._index_name)
			assert self not in index

			index[self] = self._parent()
			index[self]._usr = self
		#}

		main_context.render_funnel.user_send(closure)
	#}

	def __getattr__(self, name):
	#{
		global main_context
		assert name in self._attributes_get
		assert not hasattr(main_context.tls, 'GraphABC_ctx')

		def closure():
		#{
			ctx = get_render_context()

			index = getattr(ctx, self._index_name)
			assert self in index

			tgt = index[self]
			assert type(tgt) is self._parent

			res = getattr(tgt, name)
			if hasattr(res, '_usr'):
				res = res._usr
			return res
		#}

		return main_context.render_funnel.user_send(closure)
	#}

	def __setattr__(self, name, val):
	#{
		global main_context
		assert name in self._attributes_set
		assert not hasattr(main_context.tls, 'GraphABC_ctx')

		def closure():
		#{
			ctx = get_render_context()

			index = getattr(ctx, self._index_name)
			assert self in index

			tgt = index[self]
			assert type(tgt) is self._parent

			if hasattr(val, '_parent'):
				val = getattr(ctx, val._index)[val]

			setattr(tgt, name, val)
		#}

		main_context.render_funnel.user_send(closure)
	#}
#}
