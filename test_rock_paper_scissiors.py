import unittest

from rock_paper_scissiors import Participant


class Test(unittest.TestCase):
    def test_should_pass_when_user_choose_valid_option_rock(self):
        participant_input = Participant()
        participant_input.choose_an_option("rock")
        self.assertEqual(participant_input.choice, "rock")

    def test_should_pass_when_user_choose_valid_option_ROCK(self):
        participant_input = Participant()
        participant_input.choose_an_option("ROCK")
        self.assertEqual(participant_input.choice, "rock")

    def test_should_pass_when_user_choose_valid_option_paper(self):
        participant_input = Participant()
        participant_input.choose_an_option("paper")
        self.assertEqual(participant_input.choice, "paper")

    def test_should_pass_when_user_choose_valid_option_PAPER(self):
        participant_input = Participant()
        participant_input.choose_an_option("PAPER")
        self.assertEqual(participant_input.choice, "paper")

    def test_should_pass_when_user_choose_valid_option_scissors(self):
        participant_input = Participant()
        participant_input.choose_an_option("scissors")
        self.assertEqual(participant_input.choice, "scissors")

    def test_should_pass_when_user_choose_valid_option_SCISSORS(self):
        participant_input = Participant()
        participant_input.choose_an_option("SCISSORS")
        self.assertEqual(participant_input.choice, "scissors")

    def test_should_return_none_when_user_choose_invalid_option(self):
        participant_input = Participant()
        participant_input.choose_an_option("foo")
        self.assertEqual(participant_input.choice, None)


if __name__ == '__main__':
    unittest.main()
