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
        self._rpkm_profiles = defaultdict()
        self._rpkm_computing(IDsampleDict, rpkm_records)

    def _rpkm_computing(self, IDsampleDict, rpkm_records):
        """compute the dict(tissue, rpkm_profile) for given rpkm record containing
        rpkm values for multiple IDsampleDict

        :IDsampleDict: list of sample objects
        :rpkm_records: raw rpkm data read from file, dict(key=sampleID, value=rpkm)

        :returns: add rpk._rpkm_profiles to self._rpkm_profiles
        """        

        def __boxplot_computing(data):
            arr = numpy.array(data)
            box = plt.boxplot(arr)
            return [item.get_ydata()[1] for item in box['whishkers']]

        def __inferer(gene, record):
            arr_rpkm_stissue = defaultdict(list)
            map(lambda x: arr_rpkm_stissue[IDsampleDict[x]._stissue].append(float(record[x])),\
                                                              record.keys())
            tup_rpkm_stissue = defauldict()
            map(lambda y: setitem(tup_rpkm_stissue, y, __boxplot_computing(arr_rpkm_stissue[y])), \
                                                                        arr_rpkm_stissue.keys())
            self._rpkm_profiles[gene] = {stissue: values for stissue, values in tup_rpkm_stissue.items() }
        
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
