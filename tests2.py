#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from code import add
from code2 import divide


class TestSum(unittest.TestCase):
	def test_1(self):
		u = 1
		v = 0
		result = add(u, v)
		self.assertEqual(result, 0)

	def test_2(self):
		u = 30
		v = 10
		result = add(u, v)
		self.assertEqual(result, 50)

	def test_3(self):
		u = -100.5
		v = 200.5
		result = add(u, v)
		self.assertEqual(result, 0.0)

if __name__ == '__main__':
	unittest.main()