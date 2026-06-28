#!/usr/bin/python

# Test RISC-V branch fixups with labels.
#
# Github issue: #595
# Author: keystone-engine fork

from keystone import *

import regress


class TestRISCV(regress.RegressTest):
    def runTest(self):
        ks = Ks(KS_ARCH_RISCV, KS_MODE_RISCV32 + KS_MODE_LITTLE_ENDIAN)
        encoding, _ = ks.asm(
            b"beq x0, x0, label\n"
            b"addi x0, x0, 0\n"
            b"label:\n"
            b"addi x0, x0, 0\n",
            0,
        )
        self.assertEqual(encoding, [0x63, 0x03, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00])


if __name__ == '__main__':
    regress.main()
