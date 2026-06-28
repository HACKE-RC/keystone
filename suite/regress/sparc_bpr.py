#!/usr/bin/python

# Test SPARC BPr instruction encoding.
#
# Github issue: #599
# Author: keystone-engine fork

from keystone import *

import regress


class TestSPARC(regress.RegressTest):
    def runTest(self):
        ks = Ks(KS_ARCH_SPARC, KS_MODE_SPARC32 + KS_MODE_BIG_ENDIAN)
        encoding, _ = ks.asm(b"brlez %g1, 0x400", 0)
        self.assertEqual(encoding, [0x04, 0xC8, 0x41, 0x00])


if __name__ == '__main__':
    regress.main()
