from enum import Enum, unique
import numpy as np

import pro.consonant.voiceless_alveolar_fricative as voiceless_alveolar_fricative
import pro.consonant.voiceless_postalveolar_fricative as voiceless_postalveolar_fricative


@unique
class Consonant(Enum):  # auto()  # auto-generates numbers for items
    VOICELESS_ALVEOLAR_FRICATIVE = "s"
    VOICELESS_POSTALVEOLAR_FRICATIVE = "ʃ"


def compose(con):
    if con == Consonant.VOICELESS_ALVEOLAR_FRICATIVE:
        return voiceless_alveolar_fricative.main()
    if con == Consonant.VOICELESS_POSTALVEOLAR_FRICATIVE:
        return voiceless_postalveolar_fricative.main()
    else:
        return np.array([])
