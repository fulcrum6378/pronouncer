import numpy as np
import func as fun
import random as r


def eachTremble(i):
    if i < 57:
        x = r.uniform(0.05, 0.1)
    elif i < 61:
        x = r.uniform(0, 0.04)
    elif i < 116:
        x = r.uniform(-0.03, 0.01)
    elif i < 178:
        x = r.uniform(-0.05, 0)
    elif i < 210:
        x = r.uniform(-0.07, -0.02)
    elif i < 230:
        x = r.uniform(-0.05, -0.01)
    elif i < 278:
        x = r.uniform(-0.08, -0.04)
    elif i < 290:
        x = r.uniform(-0.05, -0.03)
    elif i < 320:
        x = r.uniform(-0.07, -0.04)
    elif i < 327:
        x = r.uniform(-0.09, -0.06)
    elif i < 337:
        x = r.uniform(-0.1, -0.13)
    elif i < 340:
        x = r.uniform(-0.1, -0.08)
    elif i < 343:
        x = r.uniform(-0.07, -0.05)
    elif i < 346:
        x = r.uniform(-0.04, -0.01)
    elif i < 349:
        x = r.uniform(-0.01, 0)
    elif i < 356:
        x = r.uniform(0, 0.01)
    elif i < 358:
        x = r.uniform(-0.01, 0.001)
    elif i < 362:
        x = r.uniform(-0.02, -0.01)
    elif i < 365:
        x = r.uniform(-0.03, -0.02)
    elif i < 369:
        x = r.uniform(-0.06, -0.04)
    elif i < 387:
        x = r.uniform(-0.07, -0.05)
    elif i < 391:
        x = r.uniform(-0.05, -0.03)
    elif i < 398:
        x = r.uniform(-0.01, -0.001)
    elif i < 400:
        x = r.uniform(-0.001, 0)
    elif i < 404:
        x = r.uniform(0, 0.02)
    elif i < 407:
        x = r.uniform(0.02, 0.05)
    elif i < 409:
        x = r.uniform(0.04, 0.07)
    elif i < 412:
        x = r.uniform(0.07, 0.09)
    elif i < 415:
        x = r.uniform(0.09, 0.1)
    elif i < 421:
        x = r.uniform(0.09, 0.12)
    elif i < 428:
        x = r.uniform(0.06, 0.09)
    elif i < 431:
        x = r.uniform(0.08, 0.1)
    elif i < 432:
        x = r.uniform(0.11, 0.13)
    elif i < 433:
        x = r.uniform(0.14, 0.16)
    elif i < 434:
        x = r.uniform(0.16, 0.17)
    elif i < 441:
        x = r.uniform(0.18, 0.2)
    elif i < 445:
        x = r.uniform(0.2, 0.23)
    elif i < 450:
        x = r.uniform(0.23, 0.26)
    elif i < 453:
        x = r.uniform(0.2, 0.22)
    elif i < 454:
        x = r.uniform(0.17, 0.2)
    elif i < 458:
        x = r.uniform(0.13, 0.15)
    elif i < 462:
        x = r.uniform(0.11, 0.13)
    elif i < 478:
        x = r.uniform(0.06, 0.08)
    elif i < 481:
        x = r.uniform(0.03, 0.06)
    elif i < 497:
        x = r.uniform(0.1, 0.13)
    else:
        x = r.uniform(0.13, 0.15)
    return x


def tremble():
    data = np.array([])
    for i in range(0, 500):  # unchangeable
        data = np.append(data, eachTremble(i))
    return data


def learn():
    data = np.array([])
    for d in range(0, 1000):  # changeable
        data = np.concatenate((data, tremble()))
    fun.arrayToAudio(data, '10', 1)
    fun.visualizeData(data)


learn()
# fun.visualizeFile('ooo_1_1', 'example')
# fun.extractAudio('ooo_1', True)
# fun.arrayToAudio(np.array(fun.audioToArray('ooo_1', True)[0][250000:255000]), 'ooo_1_1', 1, 'example')
