import pyray

type MouseButton = pyray.MouseButton

MB_Left    : MouseButton = pyray.MouseButton.MOUSE_BUTTON_LEFT
MB_Right   : MouseButton = pyray.MouseButton.MOUSE_BUTTON_RIGHT
MB_Middle  : MouseButton = pyray.MouseButton.MOUSE_BUTTON_MIDDLE
MB_Side    : MouseButton = pyray.MouseButton.MOUSE_BUTTON_SIDE
MB_Extra   : MouseButton = pyray.MouseButton.MOUSE_BUTTON_EXTRA
MB_Forward : MouseButton = pyray.MouseButton.MOUSE_BUTTON_FORWARD
MB_Back    : MouseButton = pyray.MouseButton.MOUSE_BUTTON_BACK

def MB_name(x: MouseButton) -> str:
#{
	names = {
		MB_Left:    'Left',
		MB_Right:   'Right',
		MB_Middle:  'Middle',
		MB_Side:    'Side',
		MB_Extra:   'Extra',
		MB_Forward: 'Forward',
		MB_Back:    'Back',
	}
	return names[x]
#}

type MouseButtonMap = int

def MB_to_MBM(x: MouseButton) -> MouseButtonMap:
	return 1 << x

MBM_Left    : MouseButtonMap = MB_to_MBM(MB_Left)
MBM_Right   : MouseButtonMap = MB_to_MBM(MB_Right)
MBM_Middle  : MouseButtonMap = MB_to_MBM(MB_Middle)
MBM_Side    : MouseButtonMap = MB_to_MBM(MB_Side)
MBM_Extra   : MouseButtonMap = MB_to_MBM(MB_Extra)
MBM_Forward : MouseButtonMap = MB_to_MBM(MB_Forward)
MBM_Back    : MouseButtonMap = MB_to_MBM(MB_Back)

def MBM_name(x: MouseButtonMap) -> str:
#{
	res = []
	names = {
		MBM_Left:    'Left',
		MBM_Right:   'Right',
		MBM_Middle:  'Middle',
		MBM_Side:    'Side',
		MBM_Extra:   'Extra',
		MBM_Forward: 'Forward',
		MBM_Back:    'Back',
	}
	for k in names:
		if k & x:
			res.append(names[k])
	if not res:
		return '<none>'
	return '|'.join(res)
#}
