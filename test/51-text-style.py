from graphabc import *

# Unicode sample:
#     Georg საქართველო Jap こんにちは世界 Bel Прывітанне Свет! Ej ⏩🍪🦊🦘🤭🙃🐕

SetFont('Times New Roman');
SetFontSize(30);
SetFontStyle(fsBold | fsItalic | fsUnderline);
SetFontColor(clRed);

s1 = "Прывітанне Свет!"
s2 = "Გამარჯობა Მსოფლიო!"
s3 = "⏩🍪🦊🦘🤭🙃🐕"

x = 100
y = 10

TextOut(x, y, s1);

x += int(TextWidth(s1) / 2) - int(TextWidth(s2) / 2)
y += TextHeight('X');

TextOut(x, y, s2);

x += int(TextWidth(s2) / 2) - int(TextWidth(s3) / 2)
y += TextHeight('X');

TextOut(x, y, s3);
