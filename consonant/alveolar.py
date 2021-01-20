import numpy as np

import func as fun


def ss():
    raw = fun.openJson('ss_1_1')
    data = np.array([raw, raw])
    return data.flatten()
