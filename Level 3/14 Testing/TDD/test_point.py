from point import *
import unittest
import io
from contextlib import redirect_stdout
import sys


class PointTests(unittest.TestCase):
    def setUp(self):
        self.point = Point(10, 20, "point-p1")

    def test_create_point(self):
        p = self.point
        self.assertIsNotNone(p)
        
    def test_initialize_point(self):
        p = self.point
        self.assertEqual(p.x, 10)
        self.assertEqual(p.y, 20)
        self.assertEqual(p.name, "point-p1")
    
    def test_moveBy(self):
        p = self.point
        p.moveBy(1, 11)

        self.assertEqual(p.x, 11)
        self.assertEqual(p.y, 31)
        self.assertEqual(p.name, "point-p1")
    
    def test_display_point(self):
        p = self.point
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        with io.StringIO() as buf, redirect_stdout(buf):
            p.display()
            output = buf.getvalue()
            print(output)
        sys.stdout = old_stdout        
        self.assertEqual("Point point-p1 is at [10,20]\n", output)
