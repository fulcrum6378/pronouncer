from enum import Enum, unique
import numpy as np

import consonant.voiceless_alveolar_fricative as voiceless_alveolar_fricative


@unique
class Consonant(Enum):  # auto()  # auto-generates numbers for items
    VOICELESS_ALVEOLAR_FRICATIVE = "s"


def compose(con):
    if con == Consonant.VOICELESS_ALVEOLAR_FRICATIVE:
        return voiceless_alveolar_fricative.main()
    else:
        return np.array([])
