import unittest
from unittest.mock import patch
from io import StringIO
from project import main, generateRandomNumbers, get_name, selectionOfDigit, gameStatus, saveToFile

class TestDonGame(unittest.TestCase):

    @patch('builtins.input', return_value='John')
    def test_get_name_valid_input(self, mock_input):
        self.assertEqual(get_name("Player Name: "), 'John')

    @patch('builtins.input', side_effect=['123', 'John'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_name_invalid_input_then_valid(self, mock_stdout, mock_input):
        self.assertEqual(get_name("Player Name: "), 'John')
        self.assertEqual(mock_stdout.getvalue().strip(), 'Invalid Entry')

    @patch('random.sample', return_value=[15, 16, 17, 18, 19])
    def test_generate_random_numbers(self, mock_sample):
        self.assertEqual(generateRandomNumbers(5), [15, 16, 17, 18, 19])

    @patch('builtins.input', return_value='10')
    def test_selection_of_digit_valid_input(self, mock_input):
        self.assertEqual(selectionOfDigit([10, 20, 30]), 10)

    @patch('builtins.input', side_effect=['invalid', '20'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_selection_of_digit_invalid_input_then_valid(self, mock_stdout, mock_input):
        self.assertEqual(selectionOfDigit([int(10), int(20), int(30), int(40), int(50)]), int(60))
        self.assertEqual(mock_stdout.getvalue().strip(), 'No Such Enemy\n*** Game Status ***\nPlayer Name: John\nTotal Attempts: 1\nFinal Score: 1\nJohn was defeated !!!\n\nThanks for Playing!!')

    def test_game_status_player_defeated(self):
        status = gameStatus("John", 30, 15)
        self.assertIn("John was defeated", status)

    def test_game_status_player_saved_kingdom(self):
        status = gameStatus("John", 30, 21)
        self.assertIn('*** Game Status ***\nPlayer Name: John\nTotal Attempts: 21\nFinal Score: 30\nJohn was defeated !!!\n\nThanks for Playing!!', status.strip())

    @patch('builtins.input', return_value='John')
    def test_main_game_over(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO):
            with patch('project.saveToFile'):
                with self.assertRaises(SystemExit):
                    main()

if __name__ == '__main__':
    unittest.main()
