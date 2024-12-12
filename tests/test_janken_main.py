import unittest
from unittest.mock import patch
import source.janken_main

class TestJankenMain(unittest.TestCase):
    @patch('source.player.player_pon')
    @patch('source.computer.computer_pon')
    @patch('source.janken_judge.judge')
    def test_main(self, mock_judge, mock_computer_pon, mock_player_pon):
        mock_computer_pon.side_effect = ['グー', 'チョキ', 'パー']
        mock_player_pon.side_effect = ['チョキ', 'パー', 'グー']
        mock_judge.side_effect = ['computer_win', 'player_win', 'computer_win']

        with patch('builtins.print') as mocked_print:
            source.janken_main.main()
            self.assertEqual(mock_computer_pon.call_count, 3)
            self.assertEqual(mock_player_pon.call_count, 3)
            self.assertEqual(mock_judge.call_count, 3)

            expected_calls = [
                ("-----ラウンド 1 -----",),
                ("あなたの手:チョキ",),
                ("コンピューターの手:グー",),
                ("",),
                ("コンピューターの勝ちです！",),
                ("",),
                ("-----ラウンド 2 -----",),
                ("あなたの手:パー",),
                ("コンピューターの手:チョキ",),
                ("",),
                ("あなたの勝ちです！",),
                ("",),
                ("-----ラウンド 3 -----",),
                ("あなたの手:グー",),
                ("コンピューターの手:パー",),
                ("",),
                ("コンピューターの勝ちです！",),
                ("",),
                ("【最終結果】",),
                ("あなた:1勝",),
                ("コンピュータ:2勝",),
                ("コンピュータの総合勝利です！",),
            ]
            actual_calls = [call[0] for call in mocked_print.call_args_list]
            for expected_call in expected_calls:
                self.assertIn(expected_call, actual_calls)

if __name__ == '__main__':
    unittest.main()