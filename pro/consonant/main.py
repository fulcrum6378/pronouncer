from enum import Enum, unique
import numpy as np

import pro.consonant.alveolar_nasal as alveolar_nasal
import pro.consonant.voiced_alveolar_fricative as voiced_alveolar_fricative
import pro.consonant.voiced_alveolar_plosive as voiced_alveolar_plosive
import pro.consonant.voiced_labiodental_fricative as voiced_labiodental_fricative
import pro.consonant.voiced_postalveolar_fricative as voiced_postalveolar_fricative
import pro.consonant.voiceless_alveolar_fricative as voiceless_alveolar_fricative
import pro.consonant.voiceless_alveolar_plosive as voiceless_alveolar_plosive
import pro.consonant.voiceless_labiodental_fricative as voiceless_labiodental_fricative
import pro.consonant.voiceless_postalveolar_fricative as voiceless_postalveolar_fricative


@unique
class Consonant(Enum):  # auto()  # auto-generates numbers for items
    ALVEOLAR_NASAL = "n"
    VOICED_ALVEOLAR_FRICATIVE = "z"
    VOICED_ALVEOLAR_PLOSIVE = "d"
    VOICED_LABIODENTAL_FRICATIVE = "v"
    VOICED_POSTALVEOLAR_FRICATIVE = "ʒ"
    VOICELESS_ALVEOLAR_FRICATIVE = "s"
    VOICELESS_ALVEOLAR_PLOSIVE = "t"
    VOICELESS_LABIODENTAL_FRICATIVE = "f"
    VOICELESS_POSTALVEOLAR_FRICATIVE = "ʃ"


def compose(con, before):
    if con == Consonant.ALVEOLAR_NASAL:
        return alveolar_nasal.main(before)
    if con == Consonant.VOICED_ALVEOLAR_FRICATIVE:
        return voiced_alveolar_fricative.main()
    if con == Consonant.VOICED_ALVEOLAR_PLOSIVE:
        return voiced_alveolar_plosive.main(before)
    if con == Consonant.VOICED_LABIODENTAL_FRICATIVE:
        return voiced_labiodental_fricative.main()
    if con == Consonant.VOICED_POSTALVEOLAR_FRICATIVE:
        return voiced_postalveolar_fricative.main()
    if con == Consonant.VOICELESS_ALVEOLAR_FRICATIVE:
        return voiceless_alveolar_fricative.main()
    if con == Consonant.VOICELESS_ALVEOLAR_PLOSIVE:
        return voiceless_alveolar_plosive.main(before)
    if con == Consonant.VOICELESS_LABIODENTAL_FRICATIVE:
        return voiceless_labiodental_fricative.main()
    if con == Consonant.VOICELESS_POSTALVEOLAR_FRICATIVE:
        return voiceless_postalveolar_fricative.main()
    return np.array([])
