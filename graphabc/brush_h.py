from enum import IntEnum
from typing import Optional

from .colors_h import *
from .picture_h import *
from .picture_h import _Picture
from .exports import *

@Export
class BrushStyle(IntEnum):
#{
	Clear    = 0
	Solid    = 1
	Replace  = 1
	Hatch    = 2
	Gradient = 3
	Picture  = 4
#}

ExportNames('bsClear', 'bsSolid', 'bsReplace', 'bsHatch', 'bsGradient', 'bsPicture')
bsClear    = BrushStyle.Clear
bsSolid    = BrushStyle.Solid
bsReplace  = BrushStyle.Replace
bsHatch    = BrushStyle.Hatch
bsGradient = BrushStyle.Gradient
bsPicture  = BrushStyle.Picture

@Export
class BrushPictureStyle(IntEnum):
#{
	NONE    = 0
	Stretch = 1
	Repeat  = 2
#}

ExportNames('bpsNone', 'bpsStretch', 'bpsRepeat')
bpsNone    = BrushPictureStyle.NONE
bpsStretch = BrushPictureStyle.Stretch
bpsRepeat  = BrushPictureStyle.Repeat

@Export
class HatchStyle(IntEnum):
#{
	NONE                   = 0
	Horizontal             = 1
	Vertical               = 2
	ForwardDiagonal        = 3
	BackwardDiagonal       = 4
	Cross                  = 5
	DiagonalCross          = 6
	Percent05              = 7
	Percent10              = 8
	Percent20              = 9
	Percent25              = 10
	Percent30              = 11
	Percent40              = 12
	Percent50              = 13
	Percent60              = 14
	Percent70              = 15
	Percent75              = 16
	Percent80              = 17
	Percent90              = 18
	LightDownwardDiagonal  = 19
	LightUpwardDiagonal    = 20
	DarkDownwardDiagonal   = 21
	DarkUpwardDiagonal     = 22
	WideDownwardDiagonal   = 23
	WideUpwardDiagonal     = 24
	LightVertical          = 25
	LightHorizontal        = 26
	NarrowVertical         = 27
	NarrowHorizontal       = 28
	DarkVertical           = 29
	DarkHorizontal         = 30
	DashedDownwardDiagonal = 31
	DashedUpwardDiagonal   = 32
	DashedHorizontal       = 33
	DashedVertical         = 34
	SmallConfetti          = 35
	LargeConfetti          = 36
	ZigZag                 = 37
	Wave                   = 38
	DiagonalBrick          = 39
	HorizontalBrick        = 40
	Weave                  = 41
	Plaid                  = 42
	Divot                  = 43
	DottedGrid             = 44
	DottedDiamond          = 45
	Shingle                = 46
	Trellis                = 47
	Sphere                 = 48
	SmallGrid              = 49
	SmallCheckerBoard      = 50
	LargeCheckerBoard      = 51
	OutlinedDiamond        = 52
	SolidDiamond           = 53
	Min                    = 54
	LargeGrid              = 55
	Max                    = 56
#}


ExportNames('bhNone', 'bhHorizontal', 'bhVertical', 'bhForwardDiagonal', 'bhBackwardDiagonal',
	'bhCross', 'bhDiagonalCross', 'bhPercent05', 'bhPercent10', 'bhPercent20', 'bhPercent25',
	'bhPercent30', 'bhPercent40', 'bhPercent50', 'bhPercent60', 'bhPercent70', 'bhPercent75',
	'bhPercent80', 'bhPercent90', 'bhLightDownwardDiagonal', 'bhLightUpwardDiagonal',
	'bhDarkDownwardDiagonal', 'bhDarkUpwardDiagonal', 'bhWideDownwardDiagonal',
	'bhWideUpwardDiagonal', 'bhLightVertical', 'bhLightHorizontal', 'bhNarrowVertical',
	'bhNarrowHorizontal', 'bhDarkVertical', 'bhDarkHorizontal', 'bhDashedDownwardDiagonal',
	'bhDashedUpwardDiagonal', 'bhDashedHorizontal', 'bhDashedVertical', 'bhSmallConfetti',
	'bhLargeConfetti', 'bhZigZag', 'bhWave', 'bhDiagonalBrick', 'bhHorizontalBrick', 'bhWeave',
	'bhPlaid', 'bhDivot', 'bhDottedGrid', 'bhDottedDiamond', 'bhShingle', 'bhTrellis',
	'bhSphere', 'bhSmallGrid', 'bhSmallCheckerBoard', 'bhLargeCheckerBoard',
	'bhOutlinedDiamond', 'bhSolidDiamond', 'bhMin', 'bhLargeGrid', 'bhMax')

bhNone                   = HatchStyle.NONE
bhHorizontal             = HatchStyle.Horizontal
bhVertical               = HatchStyle.Vertical
bhForwardDiagonal        = HatchStyle.ForwardDiagonal
bhBackwardDiagonal       = HatchStyle.BackwardDiagonal
bhCross                  = HatchStyle.Cross
bhDiagonalCross          = HatchStyle.DiagonalCross
bhPercent05              = HatchStyle.Percent05
bhPercent10              = HatchStyle.Percent10
bhPercent20              = HatchStyle.Percent20
bhPercent25              = HatchStyle.Percent25
bhPercent30              = HatchStyle.Percent30
bhPercent40              = HatchStyle.Percent40
bhPercent50              = HatchStyle.Percent50
bhPercent60              = HatchStyle.Percent60
bhPercent70              = HatchStyle.Percent70
bhPercent75              = HatchStyle.Percent75
bhPercent80              = HatchStyle.Percent80
bhPercent90              = HatchStyle.Percent90
bhLightDownwardDiagonal  = HatchStyle.LightDownwardDiagonal
bhLightUpwardDiagonal    = HatchStyle.LightUpwardDiagonal
bhDarkDownwardDiagonal   = HatchStyle.DarkDownwardDiagonal
bhDarkUpwardDiagonal     = HatchStyle.DarkUpwardDiagonal
bhWideDownwardDiagonal   = HatchStyle.WideDownwardDiagonal
bhWideUpwardDiagonal     = HatchStyle.WideUpwardDiagonal
bhLightVertical          = HatchStyle.LightVertical
bhLightHorizontal        = HatchStyle.LightHorizontal
bhNarrowVertical         = HatchStyle.NarrowVertical
bhNarrowHorizontal       = HatchStyle.NarrowHorizontal
bhDarkVertical           = HatchStyle.DarkVertical
bhDarkHorizontal         = HatchStyle.DarkHorizontal
bhDashedDownwardDiagonal = HatchStyle.DashedDownwardDiagonal
bhDashedUpwardDiagonal   = HatchStyle.DashedUpwardDiagonal
bhDashedHorizontal       = HatchStyle.DashedHorizontal
bhDashedVertical         = HatchStyle.DashedVertical
bhSmallConfetti          = HatchStyle.SmallConfetti
bhLargeConfetti          = HatchStyle.LargeConfetti
bhZigZag                 = HatchStyle.ZigZag
bhWave                   = HatchStyle.Wave
bhDiagonalBrick          = HatchStyle.DiagonalBrick
bhHorizontalBrick        = HatchStyle.HorizontalBrick
bhWeave                  = HatchStyle.Weave
bhPlaid                  = HatchStyle.Plaid
bhDivot                  = HatchStyle.Divot
bhDottedGrid             = HatchStyle.DottedGrid
bhDottedDiamond          = HatchStyle.DottedDiamond
bhShingle                = HatchStyle.Shingle
bhTrellis                = HatchStyle.Trellis
bhSphere                 = HatchStyle.Sphere
bhSmallGrid              = HatchStyle.SmallGrid
bhSmallCheckerBoard      = HatchStyle.SmallCheckerBoard
bhLargeCheckerBoard      = HatchStyle.LargeCheckerBoard
bhOutlinedDiamond        = HatchStyle.OutlinedDiamond
bhSolidDiamond           = HatchStyle.SolidDiamond
bhMin                    = HatchStyle.Min
bhLargeGrid              = HatchStyle.LargeGrid
bhMax                    = HatchStyle.Max

class _Brush:
#{
	_usr: object
	Color: Color
	Style: BrushStyle
	Hatch: HatchStyle
	HatchBackgroundColor: Color
	GradientSecondColor: Color
	Picture: Optional[_Picture]
	PictureStyle: BrushPictureStyle

	def __init__(self,
			color: Color = clBlack,
		):
	#{
		self.Color = color
		self.Style = bsSolid
		self.Hatch = bhNone
		self.HatchBackgroundColor = clWhite
		self.GradientSecondColor = clWhite
		self.Picture = None
		self.PictureStyle = bpsNone
	#}
#}

__all__ = get_local_exports()
