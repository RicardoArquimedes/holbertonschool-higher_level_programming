#!/usr/bin/python3

import unittest
import pep8


class TestCodeFormat(unittest.TestCase):

        """Test format PEP8"""

        def test_pep8(self):
            """Test that we conform PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
