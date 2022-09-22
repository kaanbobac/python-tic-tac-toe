import unittest
import io
import sys
from src import game


class GameTest(unittest.TestCase):
    def test_welcome_message(self):
        welcome_message = '***************************\nWelcome to ' \
                          'TIC TAC TOE Game\n***************************\n'
        output = io.StringIO()
        sys.stdout = output
        game.display_welcome_message()
        self.assertEqual(welcome_message, output.getvalue())
