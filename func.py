import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
import json
from enum import Enum


class Vowel(Enum):
    AA = 1
    AAA = 2
    II = 3
    OO = 4
    UU = 5


def audioToArray(file, flatten=False, fold='example', ext='wav'):
    rawData = sf.read(fold + '/' + file + '.' + ext)
    ex = rawData[0].tolist()
    if flatten:
        data = []
        for r in ex:
            if isinstance(r, np.ndarray):
                data.append(r[0])
            elif isinstance(r, list):
                data.append(r[0])
            else:
                data.append(r)
    else:
        data = ex
    return [data, rawData[1]]


def arrayToAudio(data, file, channels=1, fold='.', ext='wav'):  # CANNOT CREATE FOLDER
    with sf.SoundFile(fold + '/' + file + '.' + ext, 'w', 44100, channels, 'PCM_24') as f:
        f.write(data)
        f.close()


def visualizeFile(file, fold='example', ext='wav'):
    plt.plot(audioToArray(file, False, fold, ext)[0])
    plt.show()


def visualizeData(data):
    plt.plot(data)
    plt.show()


def extractAudio(file, flatten=False, fold='example', ext='wav'):
    f = open(fold + '/' + file + '.json', 'w')
    f.write(json.dumps(audioToArray(file, flatten, fold, ext)))
    f.close()


def jsonToAudio(file, fold='example', ext='wav'):
    f = open(fold + '/' + file + '.json', 'r')
    data = json.loads(f.read())
    f.close()
    arrayToAudio(np.array(data), file, 1, fold, ext)
