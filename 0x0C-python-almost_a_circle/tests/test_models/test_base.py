#!/usr/bin/python3

from models.base import Base
import unittest


class TestBase(unittest.TestCase):

        def test_id_1(self):

                obj_1 = Base()
                self.assertEqual(obj_1.id, 1)

        def test_id_2(self):

                obj_2 = Base()
                self.assertEqual(obj_2.id, 2)

        def test_id_any(self):

                obj = Base(15)
                self.assertEqual(obj.id, 15)

if __name__ == '__main__':
        unittest.main()

        def test_pep8(self):
            """Test that we conform PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
