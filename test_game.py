from unittest import TestCase

from game import Game


class TestGame(TestCase):

    def setUp(self):
        super().setUp()
        self.game = Game()

    def generate_question(self, question_number):
        self.game.question = question_number

    def assert_illegal_argument(self, guess_number):
        try:
            self.game.guess(guess_number)
            self.fail()
        except TypeError:
            pass

    def assert_matched_number(self, result, solved, strikes, balls):
        self.assertIsNotNone(result)
        self.assertEqual(solved, result.get_solved())
        self.assertEqual(strikes, result.get_strikes())
        self.assertEqual(balls, result.get_balls())

    def test_exception_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument('12')
        self.assert_illegal_argument('1234')
        self.assert_illegal_argument('12e')
        self.assert_illegal_argument('121')

    def test_matched_number(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("123"), True, 3, 0)

    def test_not_matched_number(self):
        self.generate_question("123")
        self.assert_matched_number(self.game.guess("456"), False, 0, 0)
