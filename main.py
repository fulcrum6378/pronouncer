import numpy as np
import os

import consonant.alveolar as alveolar
import func as fun
import vowel.main as vow


def main():
    each()


def each():
    data = np.array([])
    mul = 1
    for d in range(0, 25):
        if d < 1:
            data = np.concatenate((data, alveolar.ss()))
            mul += 1.8
        else:
            data = np.concatenate((data, vow.tremble(vow.Vowel.NEAR_OPEN_FRONT_UNROUNDED, mul)))
            if mul > 1: mul -= 0.4
            if mul < 1: mul = 1
    fun.arrayToAudio(data, 'output', 1)
    os.system("start ./output.wav")
    fun.visualizeFile('output', '.')


main()
# fun.arrayToAudio(fun.audioToArray('ss_1', True)[0][202000:207000], 'ss_1_1', 1, 'example')
# fun.extractAudio('ss_1_1')
# fun.visualizeData(fun.openJson('ss_1_1')[0])
