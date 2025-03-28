import inspect

_exports = []
_local_exports = []
_current_file = None

def _export_names(f: str, *args):
#{
	global _current_file
	global _local_exports

	if f != _current_file:
	#{
		_current_file = f
		_local_exports = []
	#}

	for name in args:
	#{
		assert not name in _exports
		_exports.append(name)
		_local_exports.append(name)
	#}
#}

def ExportNames(*args):
#{
	f = inspect.getfile(inspect.stack()[1][0])
	_export_names(f, *args)
#}

def Export(x):
#{
	assert hasattr(x, '__name__')
	f = inspect.getfile(inspect.stack()[1][0])
	_export_names(f, x.__name__)
	return x
#}

def get_exports():
	return _exports

def get_local_exports():
	return _local_exports

__all__ = ['ExportNames', 'Export', 'get_exports', 'get_local_exports']
