#!/usr/bin/env python

import gzip
from collections import defaultdict

class Sample(object):
    def __init__(self, id, tissue, stissue):
        self._id = id
        self._tissue = tissue
        self._stissue = stissue
    
    @staticmethod
    def _from_record(line):
        record = line.strip().split('\t')
        return Sample(record[0], record[5], record[6])

def GetSample(filepath):
    with gzip.open(filepath, 'rb') as ofile:
        ofile.readline()
        return list(map(lambda x:Sample._from_record(x), ofile.readlines()))

def _IDdict(samples):
    return dict(zip([sample._id for sample in samples], samples))

def _sTISSUEdict(samples):
    sTISSUEdict = defaultdict(list)
    map(lambda x: sTISSUEdict[x._stissue].append(x), samples)
    return sTISSUEdict


