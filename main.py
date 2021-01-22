import os

import dat.config as cfg
import pro.func as fun
from pro.main import main

mode = 1

if mode == 0:
    main(" mikɔnamit  ad'naaaan ")  # æɔʃθḱʁ
elif mode == 1:
    fun.visualizeFile('ja_1', 'example')
elif mode == 2:
    fun.arrayToAudio(fun.audioToArray('ja_1', True)[0][33500:37500], 'jj_1_1', 1, 'example')
    # os.system("start " + cfg.root + "pro/example/jj_1_1.wav")
    fun.extractAudio('jj_1_1', 'voiced_uvular_fricative')
    main("ʁaʁiti")
