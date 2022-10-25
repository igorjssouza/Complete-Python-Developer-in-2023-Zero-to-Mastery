import unittest
import main

class TestMain(unittest.TestCase):
	def test_do_stuff(self):
		test_parameter = 10
		result = main.do_stuff(test_parameter)

		self.assertEqual(result, 15)
	def test_do_stuff2(self):
		test_parameter = 'hdgsd'

		result = main.do_stuff(test_parameter)

		self.assertTrue(isinstance(result, ValueError))

unittest.main()		
