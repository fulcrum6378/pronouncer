import numpy as np
import os

import func as fun
import vowel


def makeIt():
    raw = fun.audioToArray('ss_1', True)[0][202000:208000]
    data = np.array([])
    for d in range(0, 40):
        if d < 1:
            data = np.concatenate((data, raw))
        else:
            data = np.concatenate((data, vowel.tremble(fun.Vowel.UU)))
    fun.arrayToAudio(data, 'output', 1)
    os.system("start ./output.wav")
    fun.visualizeFile('output', '.')  # 'ss_1'


makeIt()
