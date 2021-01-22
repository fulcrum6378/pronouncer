from enum import Enum, unique
import numpy as np

import pro.consonant.alveolar_nasal as alveolar_nasal
import pro.consonant.bilabial_nasal as bilabial_nasal
import pro.consonant.velar_ejective_plosive as velar_ejective_plosive
import pro.consonant.voiced_alveolar_fricative as voiced_alveolar_fricative
import pro.consonant.voiced_alveolar_plosive as voiced_alveolar_plosive
import pro.consonant.voiced_dental_fricative as voiced_dental_fricative
import pro.consonant.voiced_labiodental_fricative as voiced_labiodental_fricative
import pro.consonant.voiced_postalveolar_fricative as voiced_postalveolar_fricative
import pro.consonant.voiced_uvular_fricative as voiced_uvular_fricative
import pro.consonant.voiceless_alveolar_fricative as voiceless_alveolar_fricative
import pro.consonant.voiceless_alveolar_plosive as voiceless_alveolar_plosive
import pro.consonant.voiceless_dental_fricative as voiceless_dental_fricative
import pro.consonant.voiceless_labiodental_fricative as voiceless_labiodental_fricative
import pro.consonant.voiceless_postalveolar_fricative as voiceless_postalveolar_fricative
import pro.consonant.voiceless_velar_plosive as voiceless_velar_plosive


@unique
class Consonant(Enum):  # auto()  # auto-generates numbers for items
    ALVEOLAR_NASAL = "n"
    BILABIAL_NASAL = "m"
    VELAR_EJECTIVE_PLOSIVE = "ḱ"
    VOICED_ALVEOLAR_FRICATIVE = "z"
    VOICED_ALVEOLAR_PLOSIVE = "d"
    VOICED_DENTAL_FRICATIVE = "ð"
    VOICED_LABIODENTAL_FRICATIVE = "v"
    VOICED_POSTALVEOLAR_FRICATIVE = "ʒ"
    VOICED_UVULAR_FRICATIVE = "ʁ"
    VOICELESS_ALVEOLAR_FRICATIVE = "s"
    VOICELESS_ALVEOLAR_PLOSIVE = "t"
    VOICELESS_DENTAL_FRICATIVE = "θ"
    VOICELESS_LABIODENTAL_FRICATIVE = "f"
    VOICELESS_POSTALVEOLAR_FRICATIVE = "ʃ"
    VOICELESS_VELAR_PLOSIVE = "k"


def compose(con, before):
    if con == Consonant.ALVEOLAR_NASAL:
        return alveolar_nasal.main(before)
    if con == Consonant.BILABIAL_NASAL:
        return bilabial_nasal.main()
    if con == Consonant.VELAR_EJECTIVE_PLOSIVE:
        return velar_ejective_plosive.main()
    if con == Consonant.VOICED_ALVEOLAR_FRICATIVE:
        return voiced_alveolar_fricative.main()
    if con == Consonant.VOICED_ALVEOLAR_PLOSIVE:
        return voiced_alveolar_plosive.main(before)
    if con == Consonant.VOICED_DENTAL_FRICATIVE:
        return voiced_dental_fricative.main()
    if con == Consonant.VOICED_LABIODENTAL_FRICATIVE:
        return voiced_labiodental_fricative.main()
    if con == Consonant.VOICED_POSTALVEOLAR_FRICATIVE:
        return voiced_postalveolar_fricative.main()
    if con == Consonant.VOICED_UVULAR_FRICATIVE:
        return voiced_uvular_fricative.main()
    if con == Consonant.VOICELESS_ALVEOLAR_FRICATIVE:
        return voiceless_alveolar_fricative.main()
    if con == Consonant.VOICELESS_ALVEOLAR_PLOSIVE:
        return voiceless_alveolar_plosive.main(before)
    if con == Consonant.VOICELESS_DENTAL_FRICATIVE:
        return voiceless_dental_fricative.main()
    if con == Consonant.VOICELESS_LABIODENTAL_FRICATIVE:
        return voiceless_labiodental_fricative.main()
    if con == Consonant.VOICELESS_POSTALVEOLAR_FRICATIVE:
        return voiceless_postalveolar_fricative.main()
    if con == Consonant.VOICELESS_VELAR_PLOSIVE:
        return voiceless_velar_plosive.main()
    return np.array([])
