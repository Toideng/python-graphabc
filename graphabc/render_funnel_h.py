import pyray
import threading
from collections.abc import Callable
from typing import Optional

class RenderFunnel:
#{
	lock: threading.Lock

	render_closed: threading.Event
	render_ready: bool
	render_done: bool

	cv_render_recv: threading.Condition
	cv_user_send: threading.Condition
	cv_user_recv: threading.Condition

	f: Optional[Callable[[None], None]]
	res: Optional
	e: Optional[Exception]

	def __init__(self):
	#{
		self.lock = threading.Lock()

		self.render_closed = threading.Event()
		self.render_ready = False
		self.render_done = False

		self.cv_user_send = threading.Condition(self.lock)
		self.cv_user_recv = threading.Condition(self.lock)
		self.cv_render_recv = threading.Condition(self.lock)

		self.f = None
		self.e = None
	#}

	def user_send(self, f: Callable[[None], Optional]) -> Optional:
	#{
		with self.lock:
		#{
			while not self.render_ready:
			#{
				if self.render_closed.is_set():
					raise Exception('Render closed')
				self.cv_user_send.wait()
			#}

			self.render_ready = False
			self.f = f
			self.cv_render_recv.notify();
		#}

		with self.lock:
		#{
			while not self.render_done:
				self.cv_user_recv.wait()

			res = self.res
			e = self.e

			self.f = None
			self.res = None
			self.e = None
			self.render_done = False

			if e:
				raise e
			return res
		#}
	#}

	def render_recv(self, endtime: float) -> Optional[Callable[[None], None]]:
	#{
		with self.lock:
		#{
			self.render_ready = True
			self.cv_user_send.notify()

			while self.render_ready:
			#{
				now = pyray.get_time()
				if not self.cv_render_recv.wait(endtime - now):
					break
			#}

			if self.render_ready:
			#{
				self.render_ready = False
				return None
			#}

			assert self.f != None
			return self.f
		#}
	#}

	def render_send(self, res: Optional, e: Optional[Exception]) -> None:
	#{
		with self.lock:
		#{
			self.render_done = True
			self.res = res
			self.e = e
			self.cv_user_recv.notify()
		#}
	#}
#}
