import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import json

import dat.config as cfg

pro = "pro/"


def audioToArray(file, flatten=False, fold='example', ext='wav'):
    rawData = sf.read(cfg.root + pro + fold + '/' + file + '.' + ext)
    ex = rawData[0].tolist()
    if flatten:
        data = []
        for rr in ex:
            if isinstance(rr, np.ndarray):
                data.append(rr[0])
            elif isinstance(rr, list):
                data.append(rr[0])
            else:
                data.append(rr)
    else:
        data = ex
    return [data, rawData[1]]


def arrayToAudio(data, file, channels=1, fold='.', ext='wav'):  # CANNOT CREATE FOLDER
    with sf.SoundFile(cfg.root + pro + fold + '/' + file + '.' + ext, 'w', 44100, channels, 'PCM_24') as f:
        f.write(data)
        f.close()


def visualizeFile(file, fold='example', ext='wav'):
    plt.plot(audioToArray(file, False, fold, ext)[0])
    plt.show()


def visualizeData(data):
    plt.plot(data)
    plt.show()


def extractAudio(file, flatten=False, fold='example', ext='wav'):
    f = open(cfg.root + pro + fold + '/' + file + '.json', 'w')
    f.write(json.dumps(audioToArray(file, flatten, fold, ext)))
    f.close()


def openJson(file, fold='example'):
    f = open(cfg.root + pro + fold + '/' + file + '.json', 'r')
    data = json.loads(f.read())
    f.close()
    return data


def jsonToAudio(file, fold='example', ext='wav'):
    arrayToAudio(np.array(openJson(file, fold)), file, 1, fold, ext)


def r(x, y):  # return random.uniform(x, y)  # which gives it a noise
    return (x + y) / 2  # make it like a gradient later


def findEnum(enum, val):
    items = list(enum)
    found = None
    for en in items:
        if en.value == val:
            found = en
    return found