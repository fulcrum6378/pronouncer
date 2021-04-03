import numpy as np
from typing import Dict, List

import consonant.main as con
import vowel.main as vow


def basic(whole: Dict[str, List], subject: List[int]):
    diff: Dict[str, int] = dict()
    for name, arr in whole.items():
        d = 0
        for i in range(len(arr)): d += abs(arr[i] - subject[i])
        diff[name] = d
    # noinspection PyTypeChecker
    diff = dict(sorted(diff.items(), key=lambda item: item[1]))
    return min(diff.keys(), key=(lambda k: diff[k]))


def main(whole: np.ndarray, subject: np.ndarray):
    diff: Dict[int, float] = dict()
    for a in range(len(whole)):
        d = 0.0
        for i in range(len(whole[a])):
            try:
                d += abs(whole[a][i] - subject[i])
            except IndexError:
                pass
        diff[a] = d
    # noinspection PyTypeChecker
    diff = dict(sorted(diff.items(), key=lambda item: item[1]))
    # WHAT IF TWO CANDIDATES HAVE ONE SCORE?!?
    return min(diff.keys(), key=(lambda k: diff[k]))  # whole[


mode = 1
if mode == 0:
    ret = main(np.array([
        [4, 5, 6, 3, 3, 7, 1, 7, 8, 8],
        [1, 3, 5, 6, 7, 9, 1, 6, 4, 7],
        [0, 1, 2, 4, 4, 5, 6, 7, 8, 9],
        [9, 2, 5, 2, 2, 6, 2, 5, 7, 2],
        [4, 8, 1, 6, 2, 7, 9, 9, 2, 4],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # BUT THIS ONE IS MORE SIMILAR
    ]), np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(ret)
elif mode == 1:
    xxx = con.compose(con.Consonant.VOICELESS_POSTALVEOLAR_FRICATIVE, False)  # SH
    for x in range(len(xxx)): xxx[x] -= 0.0001
    ret = main(np.array([
        con.compose(con.Consonant.ALVEOLAR_APPROXIMANT, False),  # R
        con.compose(con.Consonant.VOICELESS_LABIODENTAL_FRICATIVE, False),  # F
        con.compose(con.Consonant.VOICELESS_ALVEOLAR_FRICATIVE, False)  # S
    ]), xxx)  # VOICELESS_DENTAL_FRICATIVE TH (THREE)
    print(ret)
elif mode == 2:
    xxx = vow.tremble(vow.Vowel.OPEN_FRONT_UNROUNDED, 2)  # a
    for x in range(len(xxx)): xxx[x] -= 0.0001
    ret = main(np.array([
        vow.tremble(vow.Vowel.NEAR_OPEN_FRONT_UNROUNDED, 2),  # ae
        vow.tremble(vow.Vowel.OPEN_MID_BACK_ROUNDED, 2),  # o
        # vow.tremble(vow.Vowel.OPEN_FRONT_UNROUNDED, 2),  # a
        vow.tremble(vow.Vowel.CLOSE_FRONT_UNROUNDED, 2),  # i
        vow.tremble(vow.Vowel.CLOSE_BACK_ROUNDED, 2)  # u
    ]), xxx)
    print(ret)
