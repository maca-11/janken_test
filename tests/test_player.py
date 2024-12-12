import unittest
from source.player import player_pon
from unittest.mock import patch

class TestPlayer(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_hand1(self, mock_input):
        self.assertEqual(player_pon(), "グー")

    @patch('builtins.input', side_effect=['2'])
    def test_hand2(self, mock_input):
        self.assertEqual(player_pon(), "チョキ")

    @patch('builtins.input', side_effect=['3'])
    def test_hand3(self, mock_input):
        self.assertEqual(player_pon(), "パー")

    @patch('builtins.input', side_effect=['0', '1'])
    def test_invalid_hand0(self, mock_input):
        self.assertEqual(player_pon(), "グー")

    @patch('builtins.input', side_effect=['4', '2'])
    def test_invalid_hand4(self, mock_input):
        self.assertEqual(player_pon(), "チョキ")

if __name__ == '__main__':
    unittest.main()