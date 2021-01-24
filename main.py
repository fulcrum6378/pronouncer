import os

import dat.config as cfg
import pro.func as fun
from pro.main import main

src = 'jj_1'
tar = 'jj_1_1'
con = 'voiced_postalveolar_affricate'
mode = 0

if mode == 0:
    main(" hanuuz ham kʼuuun nimidi ")  # æɔʃʒθʼʁɹ d͡ʒ t͡ʃ
elif mode == 1:
    os.system("start " + cfg.root + "pro/example/" + src + ".wav")
    fun.visualizeFile(src, 'example')
elif mode == 2:
    fun.arrayToAudio(fun.audioToArray(src, True)[0][172000:177000], tar, 1, 'example')
    # os.system("start " + cfg.root + "pro/example/jj_1_1.wav")
    fun.extractAudio(tar, con)
    main("salaam")
