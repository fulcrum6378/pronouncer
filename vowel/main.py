from enum import Enum
import numpy as np

import vowel.close_back_rounded as close_back_rounded
import vowel.close_front_unrounded as close_front_unrounded
import vowel.near_open_front_unrounded as near_open_front_unrounded
import vowel.open_front_unrounded as open_front_unrounded
import vowel.open_mid_back_rounded as open_mid_back_rounded


class Vowel(Enum):
    CLOSE_BACK_ROUNDED = 1  # Persian UUU
    CLOSE_FRONT_UNROUNDED = 2  # Persian III
    OPEN_FRONT_UNROUNDED = 3  # Latin AAA
    OPEN_MID_BACK_ROUNDED = 4  # Persian OOO
    NEAR_OPEN_FRONT_UNROUNDED = 5  # Persian-American AAA


def tremble(vow, multiply):
    data = np.array([])
    for i in range(0, 500):  # unchangeable
        if vow == Vowel.OPEN_FRONT_UNROUNDED:
            myFun = lambda: open_front_unrounded.main(i)
        elif vow == Vowel.NEAR_OPEN_FRONT_UNROUNDED:
            myFun = lambda: near_open_front_unrounded.main(i)
        elif vow == Vowel.CLOSE_FRONT_UNROUNDED:
            myFun = lambda: close_front_unrounded.main(i)
        elif vow == Vowel.OPEN_MID_BACK_ROUNDED:
            myFun = lambda: open_mid_back_rounded.main(i)
        elif vow == Vowel.CLOSE_BACK_ROUNDED:
            myFun = lambda: close_back_rounded.main(i)
        else:
            return None
        data = np.append(data, myFun() * multiply)
    return data
