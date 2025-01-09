import unittest

from rock_paper_scissiors import Participant, Gameboard, Game


class Test(unittest.TestCase):

    # Participant Class Test
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

    # Gameboard Class Test
    def test_should_user_score_should_be_1_when_winner_is_player(self):
        game_board = Gameboard()
        game_board.keep_scores("you")
        self.assertEqual(game_board.player_score, 1)

    def test_should_user_score_should_be_2_when_winner_is_player_twice(self):
        game_board = Gameboard()
        game_board.keep_scores("you")
        game_board.keep_scores("you")
        self.assertEqual(game_board.player_score, 2)

    def test_should_print_result(self):
        pass
        # Approval Test Here

    # Game Class Test
    def test_should_determine_winner_correctly(self):
        game = Game()
        game.player.choose_an_option("rock")
        game.bot.choose_an_option("scissors")
        game.determine_winner()
        self.assertEqual(game.winner, "You")


if __name__ == '__main__':
    unittest.main()
