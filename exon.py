#!/usr/bin/env python

import gzip
from collections import namedtuple
from copy import copy
JunctionRecord = namedtuple('JunctionRecord', ['gene', 'start', 'end', 'chr', 'profile'])

class JunctionsInstance(object):

    """Docstring for EXONInstance.
    instance for computing junctions reads count """

    def __init__(self, junctions_records, IDsampleDict):
        self._junction_profiles = defaultdict(list)
        self._junction_computing(IDsampleDict, junc_records)

    def _junction_computing(self, junc_records):
        """TODO: Docstring for _junction_computing

        :junc_records: records read from junctions file
        :returns: add self._junction_profiles[gene] = junctions_profiel
 	"""

	def __inferer(record):
            arr_junc_stissue = defaultdict(list)
            map(lambda x: arr_junc_stissue[IDsampleDict[x]._stissue].append(float(record.profile[x])),\
                                                              record.profile.keys())
            median_junc_stissue = defauldict()
            map(lambda y: setitem(median_junc_stissue, y, numpy.median(numpy.array(arr_junc_stissue[y])), \
                                                                        arr_junc_stissue.keys()))
            del arr_junc_stissue
            record.profile = copy(median_junc_stissue)
            del median_junc_stissue

            self._junc_profiles[record.gene].append(record)
        map(lambda x : __inferer(x), junctions_records)

    @staticmethod
    def _records_from_file(filepath):
        """TODO: Docstring for _records_from_file.
        :returns: TODO

        """
        def __record_process(record, stissue):
            chr, start, end = record[0].strip().split("_")
            geneid = record[1].split(',')[0]
            profile = dict(zip(stissue, record[4:]))
            return JunctionRecord(geneid, int(start), int(end), int(chr), profile) 
        
        with gzip.open(filepath, 'rb') as ofile:
            stissues = ofile.readline().strip().split('\t')[4:]
            records = list()
            map(lambda y: records.append(__record_process(y, stissues)), \
                    list(map(lambda x: x.strip().split("\t"), ofile.readlines())))
            return records

