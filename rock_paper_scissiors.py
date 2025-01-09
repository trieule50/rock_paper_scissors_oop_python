class Participant:
    def __init__(self):
        self.choice = None

    def choose_an_option(self, choice):
        valid_options = ["rock", "paper", "scissors"]
        choice = choice.lower()

        if choice in valid_options:
            self.choice = choice
        else:
            print("Please choose one of the following: Rock, Paper, Scissors")


class Gameboard:
    pass


class Game:
    pass
