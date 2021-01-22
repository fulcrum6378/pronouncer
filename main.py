import os

import dat.config as cfg
import pro.func as fun
from pro.main import main

mode = 0

if mode == 0:
    main(" adnaan ")  # æʃ
elif mode == 1:
    fun.visualizeFile('ne_1_nn_1', 'example')
elif mode == 2:
    fun.arrayToAudio(fun.audioToArray('ne_1_nn_1', True)[0][25000:34000], 'nn_1_1', 1, 'example')
    os.system("start " + cfg.root + "pro/example/nn_1_1.wav")
    fun.extractAudio('nn_1_1', 'alveolar_nasal')
