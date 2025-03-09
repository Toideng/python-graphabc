import pyray
import threading

from .context import main_context, _RenderFunc



@_RenderFunc
def run_user_cmds(timeout: float):
#{
	global main_context

	#if not threading.main_thread().is_alive():
	##{
	#	pyray.wait_time(timeout)
	#	return
	##}

	now = pyray.get_time()
	endtime = now + timeout

	while endtime > now:
	#{
		f = main_context.render_funnel.render_recv(endtime)
		if not f:
		#{
			now = pyray.get_time()
			continue
		#}

		try:
		#{
			res = f()
		#}
		except Exception as e:
		#{
			main_context.render_funnel.render_send(None, e)
		#}
		else:
		#{
			main_context.render_funnel.render_send(res, None)
		#}

		now = pyray.get_time()
	#}
#}
