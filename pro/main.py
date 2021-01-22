import numpy as np
import os

import dat.config as cfg
import pro.func as fun
import pro.syllable as syl


def main(text):
    data = np.array([])
    for s in syl.main(text.strip()):
        data = np.concatenate((data, s.compose()))
    fun.arrayToAudio(data, 'output', 1)
    os.system("start " + cfg.root + "pro/output.wav")
    fun.visualizeFile('output', cfg.root[:-1])
