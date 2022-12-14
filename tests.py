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
		self.assertEqual(result, 1)

	def test_2(self):
		u = 30
		v = 10
		result = add(u, v)
		self.assertEqual(result, 40)

	def test_3(self):
		u = -100.5
		v = 200.5
		result = add(u, v)
		self.assertEqual(result, 100.0)

	def test_4(self):
		u = "Hello "
		v = "World"
		result = add(u, v)
		self.assertEqual(result, "Hello World")

	def test_5(self):
		u = 0.60
		v = 0.09
		result = add(u, v)
		self.assertEqual(result, 0.69)

	def test_6(self):
		u = 100
		v = 0
		result = divide(u,v)
		self.assertEqual(result,-1)

	def test_7(self):
		u = 100
		v = 50
		result = divide(u,v)
		self.assertEqual(result,2)

	def test_8(self):
		u = 25
		v = 2
		result = divide(u,v)
		self.assertEqual(result,12.5)

if __name__ == '__main__':
	unittest.main()