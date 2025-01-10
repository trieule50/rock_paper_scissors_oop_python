class Participant:
    def __init__(self):
        self.choice = None

    def choose_an_option(self, choice):
        valid_options = ["rock", "paper", "scissors"]
        choice = choice.strip().lower()

        if choice in valid_options:
            self.choice = choice
        else:
            print("Please choose one of the following: rock, paper, scissors")


class Gameboard:
    def __init__(self):
        self.player_score = 0
        self.bot_score = 0

    def print_results(self, player_choice, bot_choice, winner):
        self.keep_scores(winner)
        print(f"You chose {player_choice}. The bot chose {bot_choice}. Winner is {winner}! Score is Player(You): {self.player_score}. Bot: {self.bot_score}.")

    def keep_scores(self, winner):
        if (winner == "You"):
            self.player_score += 1
        else:
            self.bot_score += 1


class Game:
    def __init__(self):
        self.player = Participant()
        self.bot = Participant()
        self.winner = None

    def determine_winner(self):
        outcomes = {
            ("rock", "scissors"): "You",
            ("scissors", "rock"): "Bot",
            ("paper", "rock"): "You",
            ("rock", "paper"): "Bot",
            ("scissors", "paper"): "You",
            ("paper", "scissors"): "Bot"
        }
        if self.player.choice == self.bot.choice:
            self.winner = "No one, it's a tie!"
        else:
            self.winner = outcomes.get((self.player.choice, self.bot.choice), "Error")

        return self.winner
