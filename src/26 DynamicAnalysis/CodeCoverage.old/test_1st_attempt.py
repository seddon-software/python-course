#!/usr/bin/env python

import unittest
from mycode import process_input

class TestApp(unittest.TestCase):
   """Test the mathematical operations"""

   def setUp(self):
       "This runs before the test cases are executed"
       self.a = 10
       self.b = 5

   def test_add_operation(self):
       result = process_input(self.a, self.b, "add")
       self.assertEqual(result, 15)


