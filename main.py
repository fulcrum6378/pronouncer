import numpy as np
import os

import consonant.main as con
import func as fun
import vowel.main as vow


def main():
    data = np.array([])
    data = np.concatenate((data, syllable("s", "a")))
    fun.arrayToAudio(data, 'output', 1)
    os.system("start ./output.wav")
    fun.visualizeFile('output', '.')


def syllable(cons, vows, stressed=False):
    data = con.compose(findEnumByVal(con.Consonant, cons))
    mul = 2.4
    if stressed: mul *= 1.25
    for vv in vows:
        for d in range(0, 25):
            data = np.concatenate((data, vow.tremble(findEnumByVal(vow.Vowel, vv), mul)))
            if mul > 1: mul -= 0.4
            if mul < 1: mul = 1
    return data


def findEnumByVal(enum, val):
    items = list(enum)
    found = None
    for en in items:
        if en.value == val:
            found = en
    return found


main()
# fun.arrayToAudio(fun.audioToArray('ss_1', True)[0][202000:207000], 'ss_1_1', 1, 'example')
# fun.extractAudio('ss_1_1')
# fun.visualizeData(fun.openJson('ss_1_1')[0])
