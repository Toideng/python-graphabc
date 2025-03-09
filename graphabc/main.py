import pyray
import queue
import sys
import threading

from .colors import *

from .context import *
from .context import _Render_Context

from .window_h import _Window

from .brush import Brush
from .pen import Pen
from .text import Font

from .keys_h import *
from .mouse_h import *

from .render_funnel import run_user_cmds

from .events_h import _Event
from .event_loop import event_loop

def __GraphABC_Start():
#{
	global main_context

	threading.Thread(target=main_thread_f).start()
	threading.Thread(target=event_loop).start()

	main_context.started.wait()

	def halt_exc_hook(etype, evalue, traceback):
		main_context.crashed.set()
		sys.__excepthook__(etype, evalue, traceback)
	sys.excepthook = halt_exc_hook
#}



def init_render_context(ctx: _Render_Context):
#{
	global main_context

	ctx.fbo = pyray.load_render_texture(
		pyray.get_screen_width(),
		pyray.get_screen_height(),
	)
	ctx.fbo_back = pyray.load_render_texture(
		pyray.get_screen_width(),
		pyray.get_screen_height(),
	)

	bk_initUO = UserObject.__init__
	def initUO(self):
	#{
		index = getattr(ctx, self._index_name)
		index[self] = self._parent()
		index[self]._usr = self
	#}
	UserObject.__init__ = initUO

	bk_initFont = Font.__init__
	def initFont(self):
		super(Font, self).__init__()
	Font.__init__ = initFont

	ctx.brush = ctx.brushes[Brush()]
	ctx.pen = ctx.pens[Pen()]
	ctx.font = ctx.fonts[Font()]

	UserObject.__init__ = bk_initUO
	Font.__init__ = bk_initFont

	ctx.window = _Window()

	ctx.events_ctx._mouse_pos = pyray.get_mouse_x(), pyray.get_mouse_y()

	setattr(main_context.tls, 'GraphABC_ctx', ctx)
#}



def process_events():
#{
	global main_context
	ctx = get_render_context()

	# Key presses
	key = pyray.get_key_pressed()
	keys = list(ctx.events_ctx._keys)
	while key != VK_Null:
	#{
		if key in keys:
			key = pyray.get_key_pressed()
			continue
		ctx.events_ctx._keys.add(key)

		cb = ctx.events_ctx.OnKeyDown
		if cb is None:
			key = pyray.get_key_pressed()
			continue

		def ff(cb, key):
			def f():
				cb(key)
			main_context.event_queue.put(_Event(f))
		ff(cb, key)

		key = pyray.get_key_pressed()
	#}

	# Key releases
	keys = list(ctx.events_ctx._keys)
	for key in keys:
	#{
		if pyray.is_key_down(key):
			continue

		ctx.events_ctx._keys.remove(key)
		cb = ctx.events_ctx.OnKeyUp
		if cb is None:
			continue

		def ff(cb, key):
			def f():
				cb(key)
			main_context.event_queue.put(_Event(f))
		ff(cb, key)
	#}

	mouse_keys = [
		MB_Left,
		MB_Right,
		MB_Middle,
		#MB_Side,
		#MB_Extra,
		#MB_Forward,
		#MB_Back,
	]

	old_mouse = ctx.events_ctx._mouse
	old_x, old_y = ctx.events_ctx._mouse_pos
	new_x = pyray.get_mouse_x()
	new_y = pyray.get_mouse_y()

	# Mouse presses
	for key in mouse_keys:
	#{
		mbm = MB_to_MBM(key)
		was_pressed = ctx.events_ctx._mouse & mbm
		if was_pressed:
			continue

		pressed = pyray.is_mouse_button_pressed(key)
		if not pressed:
			continue

		ctx.events_ctx._mouse |= mbm

		cb = ctx.events_ctx.OnMouseDown
		if cb is None:
			continue

		def ff(cb, key):
			def f():
				cb(old_x, old_y, key)
			main_context.event_queue.put(_Event(f))
		ff(cb, key)
	#}

	# Mouse releases
	if ctx.events_ctx._mouse:
	#{
		for key in mouse_keys:
		#{
			mbm = MB_to_MBM(key)
			was_pressed = ctx.events_ctx._mouse & mbm
			if not was_pressed:
				continue

			pressed = pyray.is_mouse_button_down(key)
			if pressed:
				continue

			ctx.events_ctx._mouse ^= mbm

			cb = ctx.events_ctx.OnMouseUp
			if cb is None:
				continue

			def ff(cb, key):
				def f():
					cb(old_x, old_y, key)
				main_context.event_queue.put(_Event(f))
			ff(cb, key)
		#}
	#}

	# Mouse moves
	if old_x != new_x or old_y != new_y:
	#{
		ctx.events_ctx._mouse_pos = new_x, new_y

		cb = ctx.events_ctx.OnMouseMove
		if cb is not None:
		#{
			def ff(cb):
				def f():
					cb(old_x, old_y, old_mouse)
				main_context.event_queue.put(_Event(f))
			ff(cb)
		#}
	#}
#}



def main_loop_body():
#{
	ctx = get_render_context()

	time_end = pyray.get_time() + 1/24;

	process_events()

	if ctx.window.drawing_locked:
		pyray.begin_texture_mode(ctx.fbo_back)
	else:
		pyray.begin_texture_mode(ctx.fbo)

	run_user_cmds(time_end - pyray.get_time())

	pyray.end_texture_mode()

	pyray.begin_drawing()

	pyray.clear_background(ctx.window.bgColor)
	pyray.draw_texture_rec(
		ctx.fbo.texture,
		pyray.Rectangle(0, 0, float(ctx.fbo.texture.width), float(-ctx.fbo.texture.height)),
		pyray.Vector2(0, 0),
		clWhite,
	)

	#pyray.draw_fps(10, 10);

	pyray.end_drawing()
#}



def is_running():
#{
	global main_context
	if main_context.crashed.is_set():
		return False
	return not pyray.window_should_close()
#}



def main_thread_f():
#{
	global main_context

	pyray.set_trace_log_level(pyray.LOG_ERROR)
	#pyray.set_trace_log_level(pyray.LOG_ALL)

	ctx = _Render_Context()

	if ctx.window.smoothing:
		pyray.set_config_flags(pyray.ConfigFlags.FLAG_MSAA_4X_HINT)

	pyray.init_window(
		ctx.window.Width,
		ctx.window.Height,
		ctx.window.Title,
	)
	pyray.set_target_fps(0)

	init_render_context(ctx)

	main_context.started.set()

	while is_running():
		main_loop_body()

	pyray.close_window()

	# Close render funnel
	main_context.render_funnel.render_closed.set()
	with main_context.render_funnel.lock:
		main_context.render_funnel.cv_user_send.notify()

	# Close event loop
	main_context.event_queue.put(_Event(ctx.events_ctx.OnClose, None))
	main_context.event_queue.put(_Event(None, None, True))
#}
