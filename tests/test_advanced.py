# -*- coding: utf-8 -*-

from .context import qmworld

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_genFunctions(self):
        qmworld.genSimpleWavePackage()


if __name__ == '__main__':
    unittest.main()