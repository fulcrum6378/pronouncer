import numpy as np
import os

import func as fun
import syllable as syl

src = 'eeee'
tar = 'eeee'
con = 'voiced_postalveolar_affricate'
mode = 1


if mode == 0:
    main("salam")  # æɔʃʒθʼʁɹ d͡ʒ t͡ʃ
elif mode == 1:
    # os.system(cfg.player + fun.root() + "raw/" + src + ".m4a")
    fun.visualizeFile(src, 'raw', 'm4a')
elif mode == 2:
    fun.arrayToAudio(fun.audioToArray(src, True)[0][172000:177000], tar, 1, 'example')
    # os.system(cfg.player + fun.root() + "example/jj_1_1.wav")
    fun.extractAudio(tar, con)
    main("salaam")


def main(text):
    data = np.array([])
    for s in syl.main(text.strip()):
        data = np.concatenate((data, s.compose()))
    fun.arrayToAudio(data, 'output', 1)
    os.system(cfg.player + fun.root() + "output.wav")
    fun.visualizeFile('output', fun.root()[:-1])
