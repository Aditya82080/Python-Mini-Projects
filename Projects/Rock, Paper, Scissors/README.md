# Rock, Paper, Scissors Game

## Description

The Rock, Paper, Scissors Game is a simple Python application that allows users to play the classic game against the computer. The program randomly generates the computer's choice and compares it with the user's input to determine the winner. The user can play multiple rounds and choose to quit anytime.
## Features

1. User Choices:

- Rock, Paper, or Scissors.

2. Computer's Random Choice:

- The computer randomly selects its choice using Python's random module.

3. Outcome Determination:

- The program determines the winner based on the rules of the game:

     - Rock crushes Scissors.

     - Scissors cut Paper.

     - Paper covers Rock.

4. Replay Option:

- The user can play multiple rounds and quit when desired.

5. Interactive Feedback:

- Clear instructions and results after each round.

## Required Modules

random: Used for generating the computer's random choice. This module is part of Python's standard library.

## How to Install Required Modules

No additional modules need to be installed as the program only relies on Python’s built-in functionality. Ensure you have Python installed on your system (version 3.6 or above).

To check your Python version:
```
python --version
```
or
```
python3 --version
```
If Python is not installed, download it from python.org.

## How to Run the Script

1. Download the Script:

- Save the script as `rock_paper_scissors.py`.

2. Run the Script:

- Open a terminal or command prompt.

- Navigate to the directory where `rock_paper_scissors.py` is saved.

- Execute the script:
```
python rock_paper_scissors.py
```
or
```
python3 rock_paper_scissors.py
```

3. Gameplay:

- Follow the instructions to select your choice (1 for Rock, 2 for Paper, 3 for Scissors).

- The computer will display its choice.

- The result of the round will be displayed (Win, Lose, or Tie).Choose whether to play again or exit.


## Example Interaction
```bash
Welcome to Rock, Paper, Scissors!

Enter your choice:
1. Rock
2. Paper
3. Scissors
Your choice (1/2/3): 1

You chose: Rock
Computer chose: Scissors
You win! Rock crushes Scissors.

Do you want to play again? (y/n): y

Enter your choice:
1. Rock
2. Paper
3. Scissors
Your choice (1/2/3): 2

You chose: Paper
Computer chose: Rock
You win! Paper covers Rock.

Do you want to play again? (y/n): n
Thanks for playing! Goodbye!

```
## Enhancements

- Add a scoring system to track wins, losses, and ties.

- Include a graphical user interface (GUI) using `tkinter` or `PyGame`.

- Extend to multiplayer mode.

- Add more moves (e.g., Lizard and Spock from "Rock, Paper, Scissors, Lizard, Spock").
