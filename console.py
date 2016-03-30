#!/usr/bin/env python
import sys
import samples as sa
import rpkm

from main import GeneProfile

samples = sa.GetSample(sys.argv[1])
records = rpkm.RPKMInstance._records_from_file(sys.argv[2])
RPKMinstance = rpkm.RPKMInstance(records, samples)

Genes = {geneid: GeneProfile(id = geneid, rpkms=rpkms) for geneid, rpkms in RPKMinstance._profiles.items() }

print Genes['ENSG00000223972.4'].rpkms['Testis']
