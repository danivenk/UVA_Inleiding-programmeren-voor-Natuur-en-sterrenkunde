# -*- coding: utf-8 -*-

import codecs

output_filehandle = codecs.open(u"初ファイル.txt", 'w', encoding='utf-8')
for line in range(0, 100):
    if line < 10:
        newline = u"さしすせそ\n"
        output_filehandle.write(newline)

printing = u"岡山"

print printing
