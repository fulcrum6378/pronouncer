import numpy as np
import func as fun
import random as rnd

mini = 0
maxi = 50000
togg = True
togval = 0
togmax = 50


def interpolator(i):
    global mini, maxi, togg, togval, togmax
    x = 0
    median = maxi / 2
    if i < median:
        x += abs(i - mini)
    else:
        x += abs(i - maxi)
    x *= 0.000002
    x += rnd.random() * x
    if not togg: x = 0 - x
    if togval >= togmax:
        togg = not togg
        togval = 0
    else:
        togval += 1
    return x


data = np.array([])
for d in range(mini, maxi):
    data = np.append(data, interpolator(d))
data = np.concatenate((data, data))
fun.arrayToAudio(data, 'second')
fun.visualizeData(data)
