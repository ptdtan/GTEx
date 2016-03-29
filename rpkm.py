#!/usr/bin/env python

import numpy
import gzip
from collections import namedtuple, defaultdict

rpkmProfile = namedtuple('rpkmProfile', ['sTissue', 'rpkm'])

class RPKMInstance(object):

    """Docstring for RPKMprofile. 
    instance for computing median rpkm for given genes
    """

    def __init__(self, rpkm_records):
        self._profiles = _rpkm_computing(samples, rpkm_records)

    @staticmethod
    def _rpkm_computing(samples, rpkm_records):
        """compute the dict(tissue, median rpkm) for given rpkm record containing
        rpkm values for multiple samples

        :samples: list of sample objects
        :rpkm_records: raw rpkm data read from file, dict(key=sampleID, value=rpkm)

        :returns: list of rpkmProfile
        """
        IDsampleDict = sa._IDdict(samples)
        for record in rpkm_records:
            rpkm_stissue = defaultdict(list)
            map(lambda x: rpkm_stissue[IDsampleDict[x]._stissue].append(int(record[x])), record.keys())
        profiles = list(map(rpkmProfile._make, [ [stissue, numpy.median(numpy.array(rpkms))] \
                                                    for stissue, rpkms in rpkm_stissue.items() ]))
        return profiles
    
    @staticmethod
    def _records_from_file(filepath):
        """TODO: Reads records from file

        :filepath: path to RPKM file
        :returns: dict( key=geneID, value:dict(key=sampleID, value=RPKM))

        """
        with gzip.open(filepath, 'rb') as ofile:
            map(ofile.readline(), range(2))
            stissues = ofile.readline().strip().split('\t'[2:])
            records = defaultdict(dict)
            map(lambda x: records[x[0]] = dict(zip(stissues, x[2:])),\
                                    list(map(lambda y: y.strip().split("\t"), ofile.readlines())))
            return records

            


