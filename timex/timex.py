__all__ = ['seconds_to_hhmmss']

import math


def seconds_to_hhmmss(secs):
    secs = int(secs)
    hh = int(math.floor(secs / 3600))
    mm = int(math.floor((secs - (hh * 3600)) / 60))
    ss = secs - (hh * 3600) - (mm * 60)
    return '{:02d}:{:02d}:{:02d}'.format(hh, mm, ss)
