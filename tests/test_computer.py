import unittest
from unittest.mock import patch
from source.computer import computer_pon

class TestPlayer(unittest.TestCase):
    @patch('random.choice', return_value="グー")
    def test_computer_hand1(self, mock_choice):
        self.assertEqual(computer_pon(), "グー")

    @patch('random.choice', return_value="チョキ")
    def test_computer_hand2(self, mock_choice):
        self.assertEqual(computer_pon(), "チョキ")

    @patch('random.choice', return_value="パー")
    def test_computer_hand3(self, mock_choice):
        self.assertEqual(computer_pon(), "パー")

if __name__ == '__main__':
    unittest.main()