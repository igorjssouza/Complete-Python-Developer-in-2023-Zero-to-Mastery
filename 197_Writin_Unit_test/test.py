import unittest
import main

class TestMain(unittest.TestCase):
	def test_do_stuff(self):
		test_parm = 10
		result = main.do_stuff(test_parm)
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		test_parm = 'hdgsd'

		result = main.do_stuff(test_parm)

		self.assertIsInstance(result, ValueError)

	def test_do_stuff3(self):
		test_parm = None
		result = main.do_stuff(test_parm)
		self.assertEqual(result, 'Please, return a number')

	def test_do_stuff4(self):
		test_parm = ''
		result = main.do_stuff(test_parm)
		self.assertEqual(result, 'Please, return a number')

	def test_do_stuff5(self):
		test_parm = 0
		result = main.do_stuff(test_parm)
		self.assertEqual(result, 0)




unittest.main()		
