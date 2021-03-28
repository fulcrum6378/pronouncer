import os

import dat.config as cfg
import pro.func as fun
from pro.main import main

src = 'eeee'
tar = 'eeee'
con = 'voiced_postalveolar_affricate'
mode = 1

if mode == 0:
    main("salam")  # æɔʃʒθʼʁɹ d͡ʒ t͡ʃ
elif mode == 1:
    # os.system(cfg.player + cfg.root + "pro/raw/" + src + ".m4a")
    fun.visualizeFile(src, 'raw', 'm4a')
elif mode == 2:
    fun.arrayToAudio(fun.audioToArray(src, True)[0][172000:177000], tar, 1, 'example')
    # os.system(cfg.player + cfg.root + "pro/example/jj_1_1.wav")
    fun.extractAudio(tar, con)
    main("salaam")
