from unittest import TestCase

from game import Game


class TestGame(TestCase):

    def setUp(self):
        super().setUp()
        self.game = Game()

    def assert_illegal_argument(self, guess_number):
        try:
            self.game.guess(guess_number)
            self.fail()
        except TypeError:
            pass

    def test_exception_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument('12')
        self.assert_illegal_argument('1234')
        self.assert_illegal_argument('12e')
        self.assert_illegal_argument('121')

    def test_matched_number(self):
        self.game.question = "123"
        result = self.game.guess("123")

        self.assertIsNotNone(result)
        self.assertTrue(result.get_solved())
        self.assertEqual(3, result.get_strikes())
        self.assertEqual(0, result.get_balls())

    def test_not_matched_number(self):
        self.game.question = "123"
        result = self.game.guess("456")

        self.assertIsNotNone(result)
        self.assertFalse(result.get_solved())
        self.assertEqual(0, result.get_strikes())
        self.assertEqual(0, result.get_balls())
