# PascalABC::GraphABC for Python

![PyPI - Downloads](https://img.shields.io/pypi/dm/graphabc)

A simple, education-oriented graphics module for Python --- a wrapper around Raylib

Inspired by [GraphABC module from PascalABC.NET](https://www.pascalabc.net/downloads/pabcnethelp/topics/PABCUnits/GraphABC/index.html)

This package is neither performant nor feature-rich, nor is it supposed to be. Please consider
using [Raylib](https://www.raylib.com) if your requirements no longer fit this package. Or maybe
try [rlzero](https://github.com/electronstudio/rlzero) from the author of `raylib-python-cffi`.



## Installation

*Your IDE should have already set up `pip` and `python` for you. If not, try setting up `.venv` as shown below*

First make sure you have the latest pip installed:

    pip install --upgrade pip

Then install this package

    pip install graphabc

[raylib-python-cffi](https://pypi.org/project/raylib/) should be installed automatically as a
dependency. Please consult [raylib-python-cffi troubleshooting guide](https://github.com/electronstudio/raylib-python-cffi?tab=readme-ov-file#problems)
if you have problems with installation of raylib bindings.

#### Installation --- setting up `.venv`

```
python -m venv .venv
. ./.venv/bin/activate
```



## Example code

(Check out [/test](test) for more examples)

```python
from graphabc import *

R = 10.

def draw(x, y):
	global R
	R *= 1.05
	SetPenColor(clRandom())
	SetBrushColor(clRandom())
	Circle(x, y, int(R))

def click_cb(x, y, mb):
	if mb != MB_Left:
		return
	draw(x, y)

def move_cb(x, y, mbm):
	if not mbm & MBM_Left:
		return
	draw(x, y)

SetOnMouseDown(click_cb)
SetOnMouseMove(move_cb)
```



# Why does this exist?

There are already a plethora of well-known, production-quality graphics packages for Python:
- [raylib-python-cffi](https://github.com/electronstudio/raylib-python-cffi)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [turtle](https://docs.python.org/3/library/turtle.html)
- [pyglet](https://github.com/pyglet/pyglet)
- [arcade](https://github.com/pythonarcade/arcade)
- [pygame](https://github.com/pygame/pygame)
- [pillow](https://github.com/python-pillow/Pillow)
- [kivy](https://github.com/kivy/kivy)
- [wxPython](https://github.com/wxWidgets/Phoenix)
- [matplotlib](https://github.com/matplotlib/matplotlib)
- [graphics.py](https://mcsp.wartburg.edu/zelle/python/graphics.py) (apparently EoL)

These are all amazing projects with vast adoption, extensive featuresets, and/or good performace. Please
consider using them for your project if you need a robust graphics dependency. However, they might
not be the best choice for students just starting to learn Python for the following reasons:

- **Boilerplate**: Making a project in these libraries requires writing a varying amount of
  boilerplate code, which might make students anxious about not understanding the code they are
  writing.
- **Ease of debugging**: Some of these packages, especially `tkinter` and `turtle`, are not
  well-suited for debugging: in my experience, debugging `turtle` commands is pretty much
  impossible --- some technical difficulties inevitably arise.
- **Object orientation**: Object orientation is a somewhat advanced concept, not available for
  students just starting out their Python course.
- **Being a framework**: see "boilerplate" and "object orientation" above.

[PascalABC.NET](https://www.pascalabc.net/), an educational programming environment originating in
[Russia](https://en.wikipedia.org/wiki/Russia) and widely used in Russian schools, is a wonderful
choice as the first programming language of a student. This environment provides
the [GraphABC](https://www.pascalabc.net/downloads/pabcnethelp/topics/PABCUnits/GraphABC/index.html) module,
which is simple, easy to understand, and debuggable. Thus this project was created as an adaptation
of GraphABC for the more popular Python programming language.

### Target audience

This package is meant for students and tutors of entry-level CompSci/"Informatics"



# API differences

API is closely resembling that of [GraphABC unit of PascalABC programming language/runtime environment](https://pascalabc.net/downloads/pabcnethelp/topics/PABCUnits/GraphABC/index.html)

API alterations wrt the original library:

- `GraphABCException` exception type dropped
- `RedrawProc` callback dropped
- `DrawInBuffer` mode dropped --- buffer is always used

- `PutPixel` dropped (alias)
- `FillRect` dropped (alias)
- `TextOut` of `int`/`float` types not supported, use type casting / string interpolation
- `DrawTextCentered` of `int`/`float` types not supported, use type casting / string interpolation

- Global function `Pen` renamed to `GetPen`. `Pen` now refers to the type.
- New function `SetPen` allows to setup and use a number of presets
- Functions `PenColor`, `PenWidth`, and `PenStyle` are renamed to `GetPenColor`, `GetPenWidth`, and `GetPenStyle` respectively
- `Pen::NETPen` and `Pen::Mode` dropped

- Global function `Brush` renamed to `GetBrush`. `Brush` now refers to the type.
- New function `SetBrush` allows to setup and use a number of presets
- Functions `BrushColor`, `BrushStyle`, `BrushHatch`, `HatchBrushBackgroundColor`, and `GradientBrushSecondColor` are renamed to `GetBrushColor`, `GetBrushStyle`, `GetBrushHatch`, `GetHatchBrushBackgroundColor`, and `GetGradientBrushSecondColor` respectively
- `Brush::NETBrush` dropped
- Added new brush style `bsPicture`
- Added new brush style `bsReplace` which ignores alpha channel and replaces a region with specified brush instead

- Global function `Font` renamed to `GetFont`. `Font` now refers to the type.
- `SetFontName()` is dropped --- instance new fonts instead using `Font('<path>/<name>')`
- `Font::Name` is read-only
- Functions `FontName`, `FontColor`, `FontSize`, and `FontStyle` are renamed to `GetFontName`, `GetFontColor`, `GetFontSize`, and `GetFontStyle` respectively
- `Font::NETFont` dropped

- `Picture::Create` renamed to `Picture::__init__()`, and only supports loading from file
- All pictures have an alpha channel, thus the `Transparent`/`TransparentColor` properties have been dropped
- `Picture` now has properties `X`, `Y` along with `Width`, `Height`. They are used for selecting a part of original picture
- Drawing on pictures is not supported. Use Raylib if you need to draw on pictures.

- Instead of setting event callbacks directly, use `SetOn*()`
- `OnMouseDown()`, `OnMouseUp()`, `OnMouseMove()` pass virtual codes instead of 0/1/2
- `OnKeyPress()` not supported



## Unimplemented (planned) functionality

If some functionality is denoted as "dropped" above in the list of alterations, there are not plans
of implementing it.  Still, some other functionality isn't yet supported and might be added later:

- Freehand shapes (`*ClosedCurve`, `Curve`, `*Polygon`, `Polyline`)
- `FloodFill`
- Any text / font functions
- Pen styles & width
- Brush styles
- Custom window coordinates



# Warning: Bad code inside

The original `PascalABC::GraphABC` API is built atop the Win32 API or a similar retained-mode
graphics toolset. Raylib, however, prefers immediate-mode drawing to the window instead. This forced
a rather awkward approach of using threading for connecting the two together.

Also, not all original functionality has a one-to-one mapping in Raylib --- thus some of it has to
be implemented manually.
