import numpy as np
import os

import func as fun
import syllable as syl


def main(text):
    data = np.array([])
    for s in syl.main(text.strip()):
        data = np.concatenate((data, s.compose()))
    fun.arrayToAudio(data, 'output', 1)
    os.system("start ./output.wav")
    fun.visualizeFile('output', '.')


main(" sæsus ")
# fun.arrayToAudio(fun.audioToArray('ss_1', True)[0][202000:207000], 'ss_1_1', 1, 'example')
# fun.extractAudio('ss_1_1')
# fun.visualizeData(fun.openJson('ss_1_1')[0])
