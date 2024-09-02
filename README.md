# Rock Paper Scissors Python

## Rules
Rock, paper, scissors is a game played by two participants.
The game consists of rounds. In each round, a participant chooses a symbol from rock, paper, or scissors, and the other participant does the same. 
Then a winner of the round is determined by comparing the chosen symbols. The rules of the game state that rock wins over scissors, scissors beats (cuts) paper, and paper beats (covers) rock. 
The winner of the round is awarded a point. The game goes on for as many rounds as the participants agree on. The winner is the participant with the most points.

## Model an OOP system

| Phase | Actor | Behavior | Data |
-----------------------------------
| Input | Players | Pick Symbol | Symbol |
| Processing | Gameboard | Decide winner | Results |
| Processing | Gameboard | Awards point to winner | Points |
| Processing | Game | Check if participants want to play | Answer |
| Output | Gameboard | Output who won | Output Message  |
| Output | Game | End game or new game |  |
