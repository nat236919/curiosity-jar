"""
PROJECT: Rock Paper Scissors
DESCRIPTION: A simple game of rock paper scissors against the computer.
AUTHOR: Nuttaphat Arunoprayoch (@nuttaphat)
DATE: 24-Jan-2022
"""

from game_engine import RockPaperScissors


def main():
    print("Welcome to Rock Paper Scissors!")
    game = RockPaperScissors()
    game.play(3)
    return None


if __name__ == '__main__':
    main()
