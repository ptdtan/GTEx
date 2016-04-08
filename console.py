#!/usr/bin/env python
import sys
import samples as sa

BUFFER = str(sys.argv[3])
samples = sa.GetSample(sys.argv[1])
transcript_samples = open(sys.argv[2]).read().strip().split("\t")[BUFFER:]

IDdict = sa._IDdict(samples)
arr_tissues = list(map(lambda x: IDdict[x]._stissue, transcript_samples))
tmp = arr_tissues[0]
tmp_idx = 0
for i, s in enumerate(arr_tissues):
    if i == 0:
        print "\t".join([s, str(BUFFER+i+1)])
    elif i == len(arr_tissues) -1 :
        print "\t".join([s, str(tmp_idx), str(BUFFER+len(arr_tissues)+1)])
    else:
        print "\t".join([s, str(tmp_idx), str(BUFFER+1+i)])
        tmp_idx = i+2
        tmp = s
