import pyray
import queue

from .context import *

def event_loop_is_running():
#{
	global main_context
	if main_context.crashed.is_set():
		return False;
	#if main_context.render_funnel.render_closed.is_set():
	#	return False;
	return True;
#}

def event_loop():
#{
	global main_context
	while event_loop_is_running():
	#{
		try:
			e = main_context.event_queue.get(timeout=1);
		except queue.Empty:
			continue;

		if e.close_cmd:
			break;

		if e.to is not None and e.to < pyray.get_time():
			continue;

		if e.f is None:
			continue

		assert callable(e.f);
		e.f();
	#}
#}
