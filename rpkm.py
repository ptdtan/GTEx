#!/usr/bin/env python

import numpy
import gzip
import samples as sa
import matplotlib.pyplot as plt
from multithread import ThreadPool
from collections import namedtuple, defaultdict
from operator import setitem

Profile = namedtuple('BoxplotProfile', ['median', 'q75', 'q25', 'high', 'low'])
class RPKMInstance(object):

    """Docstring for RPKMprofile. 
    instance for computing median rpkm for given genes
    """

    def __init__(self, rpkm_records, IDsampleDict):
        pass
        #self._rpkm_profiles = defaultdict()
        #self._rpkm_computing(IDsampleDict, rpkm_records)
    
    @staticmethod
    def _records_from_file(filepath):
        """TODO: Reads records from file

        :filepath: path to RPKM file
        :returns: dict( key=geneID, value:array of expression)

        """
        with gzip.open(filepath, 'rb') as ofile:
            map(lambda x: ofile.readline(), range(2))
            #stissues = ofile.readline().strip().split('\t')[2:]
            records = defaultdict(dict)
            map(lambda x: setitem(records, x[0], x[2:]),\
                                    list(map(lambda y: y.strip().split("\t"), ofile.readlines())))
	return records
