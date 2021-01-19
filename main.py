import numpy as np

import func as fun
import vowel


# 10 => a, 11 => o, 12 => ä, 13 => i, 14 => u

def learn():
    data = np.array([])
    for d in range(0, 1000):  # changeable
        data = np.concatenate((data, vowel.tremble()))
    fun.arrayToAudio(data, '10', 1)
    fun.visualizeData(data)


# learn()
# fun.visualizeFile('sa_1', 'example')
# fun.extractAudio('uuu_1_1', True)
# fun.arrayToAudio(np.array(fun.audioToArray('äää_1', True)[0][200000:205000]), 'äää_1_1', 1, 'example')
# fun.jsonToAudio('uuu_1_2')
