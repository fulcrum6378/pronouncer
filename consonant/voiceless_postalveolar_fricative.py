import func as fun
import numpy as np


def main():
    raw = fun.openJson('voiceless_postalveolar_fricative', 'consonant')
    data = np.array([raw, raw])
    return data.flatten()
