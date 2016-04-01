#!/usr/bin/env python

from __future__ import division
import numpy as np
def toTPM(arrRPKMs):
    """TODO: Docstring for toTPM(arrRPKMs.
    convert array of RPKM value to TPM value
    :returns: arrTPM

    """
    arr = np.array(arrRPKMs)
    s = np.sum(arr)
    return list(map(lambda x: float((x/s))*1e6, list(arr)))
