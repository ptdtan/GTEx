#!/usr/bin/env python
import sys
import samples as sa
import rpkm
import rpkm2tpm as rt

samples = sa.GetSample(sys.argv[1])
transcript_samples = open(sys.argv[2]).read().strip().split("\t")[2:]

iddict = sa._IDdict(samples)
tissuedict = sa._STISSUEdict(samples)
#print tissuedict.keys(), tissuedict.values()
tmp = tissuedict[transcript_samples[0]]._stissue
print tmp, transcript_samples.index(
for s in transcript_samples:

    #sleep(0.5)
