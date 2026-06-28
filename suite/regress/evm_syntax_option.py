#!/usr/bin/python

# Test that unsupported syntax options fail cleanly instead of crashing.
#
# Github issue: #602
# Author: keystone-engine fork

from keystone import *

import regress
import subprocess
import sys
import textwrap


class TestEVM(regress.RegressTest):
    def runTest(self):
        code = textwrap.dedent("""
            from keystone import *

            ks = Ks(KS_ARCH_EVM, 0)
            try:
                ks.syntax = KS_OPT_SYNTAX_INTEL
            except KsError as exc:
                raise SystemExit(0 if exc.errno == KS_ERR_OPT_INVALID else 3)
            raise SystemExit(4)
        """)

        result = subprocess.run(
            [sys.executable, "-c", code],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(
            result.returncode,
            0,
            result.stderr.decode("utf-8", "replace") + result.stdout.decode("utf-8", "replace"),
        )


if __name__ == '__main__':
    regress.main()
