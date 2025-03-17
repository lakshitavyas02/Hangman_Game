# Hangman_Game
This is a simple Hangman Game implemented in Python.

## Description

Hangman is a classic word guessing game where one player thinks of a word and the other player tries to guess it by suggesting letters within a certain number of guesses.

## How to Play

1. Run the Python script `hangman.py`.
2. You will be presented with a blank word to guess and a set number of lives.
3. Guess a letter by inputting it in the terminal.
4. If the letter is in the word, it will be revealed in its correct positions.
5. If the letter is not in the word, you will lose a life.
6. Keep guessing letters until you either guess the word correctly or run out of lives.
7. If you guess the word correctly, you win! If you run out of lives, you lose.

## Features

- Randomly selects a word for the player to guess from a predefined list.
- Displays the current progress of the guessed word with underscores representing unknown letters.
- Keeps track of the number of lives remaining and displays a hangman ASCII art corresponding to the number of lives left.
- Notifies the player if they have already guessed a letter.
- Ends the game when the player either guesses the word correctly or runs out of lives.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository to your local machine:

```bash
git clone https://github.com/lakshitavyas02/Hangman_Game.git
```
2. Navigate to the project directory:
```bash
cd hangman-game
```
3. Run the Python script:
```bash
python hangman.py
```
## Contribution
Contributions are welcome! If you'd like to contribute to this project, please create a pull request with your proposed changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
