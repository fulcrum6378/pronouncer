import numpy as np
import func as fun

mini = 0
maxi = 100000
togg = True
togval = 0
togmax = 20  # int
over = False
overadd = 0.1
overval = 0
overmax = 400  # int


def interpolator(i):
    global mini, maxi, togg, togval, togmax, over, overadd, overval, overmax
    x = 0
    median = maxi / 2
    if i < median:
        x += abs(i - mini)
    else:
        x += abs(i - maxi)
    x *= 0.000001

    if over: x += overadd * (x + 0.1)
    if overval >= overmax:
        over = not over
        overval = 0
    else:
        overval += 1
    # "random.random()" gives it a noise

    if not togg: x = 0 - x
    if togval >= togmax:
        togg = not togg
        togval = 0
    else:
        togval += 1
    return x


def learn():
    data = np.array([])
    for d in range(mini, maxi):
        data = np.append(data, interpolator(d))
    fun.arrayToAudio(data, '6')
    fun.visualizeData(data)


learn()
# fun.visualizeFile('uuu_1', 'example')
