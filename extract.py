import sys
import os

fin = open(sys.argv[1])
samples = fin.readlines()
samples = list(map(lambda x: x.strip().split("\t"), samples))
for s in samples:
	s[0] = s[0].replace(" ", "_").replace("(", "_").replace(")","_")
	#os.system(' '.join(["./trim", s[1], s[2], s[0]]))
	print ' '.join(["./trim", s[1], s[2], s[0]])
