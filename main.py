import base64
import cgi
import numpy as np
import socket
from soundfile import SoundFile

import config as cfg
import func as fun
import syllable as syl


if socket.gethostname() == "WIN-KJ6QV3R1373KIR":
    print("Content-Type: text/plain\n")
    got = {"t": ""}
    try:
        for g in cgi.FieldStorage().list: got[g.name] = g.value
    except:
        pass
    if got["t"] == "":
        print("hello there")
    else:
        data = np.array([])
        for s in syl.main(got["t"].strip()):
             data = np.concatenate((data, s.compose()))
        fun.arrayToAudio(data, 'output', 1)
        with open(fun.here() + 'output.wav', 'rb') as f:
            print(str(base64.b64encode(f.read()))[2:-1])
            f.close()
