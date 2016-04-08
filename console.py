#!/usr/bin/env python
import sys
import samples as sa

BUFFER = int(sys.argv[3])
samples = sa.GetSample(sys.argv[1])
transcript_samples = open(sys.argv[2]).read().strip().split("\t")[BUFFER:]

IDdict = sa._IDdict(samples)
arr_tissues = list(map(lambda x: IDdict[x]._stissue, transcript_samples))
tmp = arr_tissues[0]
samples_index = [(tmp, 0+BUFFER+1)]
for i, s in enumerate(arr_tissues):
    if s != tmp:
        samples_index.append((s, i+1+BUFFER))
        tmp = s
for i in range(len(samples_index)):
    print samples_index[i][0], samples_index[i][1], samples_index[i+1].[1]-1
