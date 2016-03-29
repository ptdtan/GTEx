#!/usr/bin/env python

import sys

class Sample(object):
    def __init__(self, id, tissue, name):
        self._id = id
        self._tissue = tissue
        self._name = name
    
    @staticmethod
    def _from_record(line):
        record = line.strip().split('\t')
        return Sample(record[0], record[5], record[6])

def GetSample(filepath):
    with open(filepath) as ofile:
        ofile.readline()
        return list(map(lambda x:Sample._from_record(x), ofile.readlines()))
def _samplesDict(samples):
    return dict(zip(list(map(lambda x:x._id, samples)), samples))

