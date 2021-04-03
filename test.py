import numpy as np
import os

import func as fun
import plot as plt
import syllable as syl

# "start " for Windows
# "rhythmbox-client --play-uri="
player = "totem "
src = 'eeee'
tar = 'eeee'
con = 'voiced_postalveolar_affricate'
mode = 0


def main(text):
    data = np.array([])
    for s in syl.main(text.strip()):
        data = np.concatenate((data, s.compose()))
    fun.arrayToAudio(data, 'output', 1)
    os.system(player + fun.root() + "output.wav")
    plt.visualizeFile('output', '')


if mode == 0:
    main("salam")  # æɔʃʒθʼʁɹ d͡ʒ t͡ʃ
elif mode == 1:
    # os.system(cfg.player + fun.root() + "raw/" + src + ".m4a")
    plt.visualizeFile(src, 'raw', 'm4a')
elif mode == 2:
    fun.arrayToAudio(fun.audioToArray(src, True)[0][172000:177000], tar, 1, 'example')
    # os.system(cfg.player + fun.root() + "example/jj_1_1.wav")
    fun.extractAudio(tar, con)
    main("salaam")
