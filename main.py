#!/usr/bin/env python

class GeneProfile(object):
    def __init__(self, id=None, rpkms=None, exons_count = None, eQTL = None):
        self.id = id
        self.rpkms = rpkms
        self.exons_count = exons_count
        self.eQTL = eQTL
