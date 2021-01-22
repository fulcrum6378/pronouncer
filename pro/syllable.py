import copy
import numpy as np

import pro.consonant.main as con
import pro.func as fun
import pro.vowel.main as vow

stress = "'"
prolong = ":"


def main(text):
    syllables = np.array([])
    s = Syllable()
    for c in range(0, len(text)):
        ch = text[c]
        isCon = fun.findEnum(con.Consonant, ch)
        isVow = fun.findEnum(vow.Vowel, ch)
        if isCon is not None:
            if len(s.vows) == 0:
                s.addBCon(isCon)
            elif len(text) > (c + 1) and fun.findEnum(vow.Vowel, text[c + 1]) is not None:
                syllables = np.append(syllables, [copy.deepcopy(s)])
                s = Syllable()
                s.addBCon(isCon)
                continue
            else:
                s.addACon(isCon)
        elif isVow is not None:
            s.addVow(isVow)
        elif ch == prolong:
            s.prolong = True
        elif ch == stress:
            s.stressed = True
        else:
            raise Exception("Unknown IPA character!")
    if len(s.vows) > 0:
        syllables = np.append(syllables, [s])
    print([sy.__dict__ for sy in syllables])
    return syllables


class Syllable:
    def __init__(self):
        self.stressed = False
        self.bCons = []
        self.vows = []
        self.aCons = []
        self.prolong = False

    def addBCon(self, consonant):
        self.bCons.append(consonant)

    def addVow(self, vowel):
        self.vows.append(vowel)

    def addACon(self, consonant):
        self.aCons.append(consonant)

    def compose(self):
        data = np.array([])
        for bc in self.bCons:
            data = np.concatenate((data, con.compose(bc, True)))
        mul = 2  # too much of this bitch makes an echo sound
        if self.stressed: mul *= 1.25
        for vv in self.vows:
            for d in range(0, 15):
                data = np.concatenate((data, vow.tremble(vv, mul)))
                if mul > 1: mul -= 0.25
                if mul < 1: mul = 1
        for ac in self.aCons:
            data = np.concatenate((data, con.compose(ac, False)))
        return data
