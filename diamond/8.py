import numpy as np
import func as fun
import random

mini = 0
maxi = 100000
togg = True
togval = 0
togmax = 700  # Sound Pitch (int)
over = False
overadd = 0.1
overval = 0
overmax = 30  # Addition (int)
freq = False
freqval = 0
freqmax = 5  # Frequency (int)


def interpolator(i):
    global freq, freqval, freqmax, mini, maxi, togg, togval, togmax, over, overadd, overval, overmax
    x = 0

    # Frequency
    shallEnd = False
    if not freq: shallEnd = True
    if freqval >= freqmax:
        freq = not freq
        freqval = 0
    else:
        freqval += 1
    if shallEnd: return x

    median = maxi / 2
    if i < median:
        x += abs(i - mini)
    else:
        x += abs(i - maxi)
    x *= 0.000001

    # Addition
    if over: x += overadd * (random.random() * x)  # (x + 0.08)
    if overval >= overmax:
        over = not over
        overval = 0
    else:
        overval += 1
    # "random.random()" gives it a noise

    # Positive or Negative toggle
    if not togg: x = 0 - (x * 0.9)
    if togval >= togmax:
        togg = not togg
        togval = 0
    else:
        if togg: togval += 1
        else: togval += 5
    return x  # np.array([x, x])


def learn():
    data = np.array([])
    for d in range(mini, maxi):
        data = np.append(data, interpolator(d))
    fun.arrayToAudio(data, '8', 1)
    fun.visualizeData(data)


learn()
# fun.visualizeFile('aaa_1', 'example')
# fun.extractAudio('8', 'learn')
# print(fun.audioToArray('aaa_1')[0][250000:255000])
