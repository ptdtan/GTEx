#!/usr/bin/env python
import sys
import samples as sa
import rpkm

samples = sa.GetSample(sys.argv[1])
records = rpkm.RPKMInstance._records_from_file(sys.argv[2])
RPKMprofiles = rpkm.RPKMInstance(records, samples)
