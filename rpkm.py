#!/usr/bin/env python

import numpy
import gzip
import samples as sa
from multithread import ThreadPool
from collections import namedtuple, defaultdict
from operator import setitem


class RPKMInstance(object):

    """Docstring for RPKMprofile. 
    instance for computing median rpkm for given genes
    """

    def __init__(self, rpkm_records, samples):
        self._profiles = defaultdict()
        self._rpkm_computing(samples, rpkm_records)

    def _rpkm_computing(self, samples, rpkm_records):
        """compute the dict(tissue, median rpkm) for given rpkm record containing
        rpkm values for multiple samples

        :samples: list of sample objects
        :rpkm_records: raw rpkm data read from file, dict(key=sampleID, value=rpkm)

        :returns: list of rpkmProfile
        """
        IDsampleDict = sa._IDdict(samples)
        def __inferer(gene, record):
            rpkm_stissue = defaultdict(list)
            map(lambda x: rpkm_stissue[IDsampleDict[x]._stissue].append(float(record[x])), record.keys())
            self._profiles[gene] = {stissue: numpy.median(numpy.array(rpkms)) \
                  for stissue, rpkms in rpkm_stissue.items() }

        map(lambda arg : __inferer(*arg), [[gene, record] for gene, record in rpkm_records.items()])
    
    @staticmethod
    def _records_from_file(filepath):
        """TODO: Reads records from file

        :filepath: path to RPKM file
        :returns: dict( key=geneID, value:dict(key=sampleID, value=RPKM))

        """
        with gzip.open(filepath, 'rb') as ofile:
            map(lambda x: ofile.readline(), range(2))
            stissues = ofile.readline().strip().split('\t')[2:]
            records = defaultdict(dict)
            map(lambda x: setitem(records, x[0], dict(zip(stissues, x[2:]))),\
                                    list(map(lambda y: y.strip().split("\t"), ofile.readlines())))
            return records

            


