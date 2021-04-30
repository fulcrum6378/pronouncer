import json
import numpy as np
import os.path
import socket
import soundfile as sf

mergen = "WIN-KJ6QV3R1373"


def root():
    return os.path.realpath(__file__)[:-7].replace("\\", "/")


def can_print():
    return socket.gethostname() != mergen


def audioToArray(file, flatten=False, fold='raw', ext='wav'):
    rawData = sf.read(root() + fold + '/' + file + '.' + ext)
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
    try:
        with sf.SoundFile(root() + fold + '/' + file + '.' + ext, 'w', 44100, channels, 'PCM_24') as f:
            f.write(data)
            f.close()
    except RuntimeError:
        arrayToAudio(data, file, channels, fold, ext)


def extractAudio(file1, file2, fold1='example', fold2='consonant', ext='wav', flatten=False):
    f = open(root() + fold2 + '/' + file2 + '.json', 'w')
    f.write(json.dumps(audioToArray(file1, flatten, fold1, ext)[0]))
    f.close()


def openJson(file, fold='raw'):
    f = open(root() + fold + '/' + file + '.json', 'r')
    data = json.loads(f.read())
    f.close()
    return data


def jsonToAudio(file, fold='raw', ext='wav'):
    arrayToAudio(np.array(openJson(file, fold)), file, 1, fold, ext)


def r(x, y, i=None, start=None, end=None):  # return random.uniform(x, y)  # which gives it a noise
    if i is None:
        return (x + y) / 2  # , 0  # make it like a gradient later
    else:
        frames = end - start
        if frames < 1:
            return (x + y) / 2 , start
        else:
            return x + (((y - x) / frames) * i) , start


def findEnum(enum, val):
    items = list(enum)
    found = None
    for en in items:
        if en.value == val:
            found = en
    return found
