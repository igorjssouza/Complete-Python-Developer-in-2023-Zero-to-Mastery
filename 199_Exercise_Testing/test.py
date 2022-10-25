import unittest
import script

class TestScript(unittest.TestCase):
	def testInput(self):
		answer = 5
		guess = 5
		result = script.run_guess(guess,answer)
		self.assertTrue(result)

if __name__ == '__main__':
	unittest.main()	