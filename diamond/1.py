import numpy as np
import func as fun
import random as rnd

mini = 0
maxi = 100000
togg = True


def interpolator(i):
    global mini, maxi, togg
    x = 0
    median = maxi / 2
    if i < median:
        x += abs(i - mini)
    else:
        x += abs(i - maxi)
    x *= 0.000002
    x += rnd.random()  # * x (=> second)
    if not togg: x = 0 - x
    togg = not togg
    return x


data = np.array([])
for d in range(mini, maxi):
    data = np.append(data, interpolator(d))
fun.arrayToAudio(data, 'second')
fun.visualizeData(data)
