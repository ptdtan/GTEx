#!/usr/bin/env python
import sys
import samples as sa

samples = sa.GetSample(sys.argv[1])
transcript_samples = open(sys.argv[2]).read().strip().split("\t")[2:]

IDdict = sa._IDdict(samples)
STISSUEdict = sa._STISSUEdict(samples)
tmp = IDdict[transcript_samples[0]]._stissue
print "\t".join([tmp, transcript_samples.index(STISSUEdict[tmp]._id)])
for s in transcript_samples:
    if IDdict[s]._stissue != tmp:
        print "\t".join([IDdict[s]._stissue, transcript_samples.index(s)])
