#!/usr/bin/env python
import sys

def hashtable(ohash):
    return {arr[1]:arr[0] for arr in [line.strip().split("\t") 
                                        for line in ohash.read().strip().split("\n")]}
def hashENSG(arrgenes, htable):
    return list(map(lambda x: htable.get(x, "NA"), arrgenes))

if __name__ == "__main__":
    genes = open(sys.argv[1]).read().strip().split("\n")
    htable = hashtable(open(sys.argv[2]))
    ensggenes = hashENSG(genes, htable)
    fout = open(sys.argv[3], "w")
    fout.write("\n".join(ensggenes))


