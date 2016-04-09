#!/usr/bin/env python
import sys
import samples as sa

samples = sa.GetSample(sys.argv[1])
transcript_samples = open(sys.argv[2]).read().strip().split("\t")[4:]

IDdict = sa._IDdict(samples)
STISSUEdict = sa._sTISSUEdict(samples)
tmp = IDdict[transcript_samples[0]]._stissue
print "\t".join([tmp, "0"])
for i, s in enumerate(transcript_samples):
    if IDdict[s]._stissue != tmp:
        print "\t".join([IDdict[s]._stissue, str(transcript_samples.index(s))])
        tmp = IDdict[s]._stissue
