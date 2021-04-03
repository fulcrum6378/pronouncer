import matplotlib.pyplot as plt

import func as fun


def visualizeFile(file, fold='raw', ext='wav'):
    plt.plot(fun.audioToArray(file, False, fold, ext)[0])
    plt.show()


def visualizeData(data):
    plt.plot(data)
    plt.show()
