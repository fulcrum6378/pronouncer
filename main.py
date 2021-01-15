import numpy as np

import func as fun
import vowel


def learn():
    data = np.array([])
    for d in range(0, 1000):  # changeable
        data = np.concatenate((data, vowel.tremble()))
    fun.arrayToAudio(data, '12', 1)
    fun.visualizeData(data)


# learn()
# fun.visualizeFile('äää_1', 'example')
# fun.extractAudio('ooo_1_1', True)
# fun.arrayToAudio(np.array(fun.audioToArray('äää_1', True)[0][200000:205000]), 'äää_1_1', 1, 'example')
# fun.jsonToAudio('ooo_1_2')
