import unittest
import randomgame

class TestRandomgame(unittest.TestCase):
    def test_input_correct_guess(self):
        result = randomgame.run_guess(5, 5)
        self.assertTrue(result)
    
    def test_input_incorret_guess(self):
        result = randomgame.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = randomgame.run_guess(5, 11)
        self.assertFalse(result)
    
    def test_input_wrong_type(self):
        result = randomgame.run_guess(5, 'string')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
