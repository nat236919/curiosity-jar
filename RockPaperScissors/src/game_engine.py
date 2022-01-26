"""
FILE: game_engine.py
DESCRIPTION: A game engine for Rock Paper Scissors against the computer.
AUTHOR: Nuttaphat Arunoprayoch (@nuttaphat)
DATE: 24-Jan-2022
"""
import random
from typing import List, Dict, Any


class RockPaperScissors:
    """A game engine class for Rock Paper Scissors against the computer.
    """

    def __init__(self):
        self.choices = ['r', 'p', 's']
        self.player_score = 0
        self.computer_score = 0
        self.times_played = 0

    def show_summary(self) -> None:
        """Display statistical results
        """
        if not self.times_played:
            text = 'No games played yet.'
        else:
            won_rate = self.player_score / self.times_played
            text = f"""
            --- Summary ----------------------------------------
                You won {self.player_score} times
                The computer won {self.computer_score} times.
                Player won {won_rate * 100}% of the time.
            ----------------------------------------------------
            """

        print(text)

        return None

    def play(self, n: int = 1) -> None:
        """Play game n times.

        Args:
            n (int, optional): times to be played. Defaults to 1.

        Returns:
            [None]: [description]
        """
        while n > 0:
            # Get choices
            computer_hand = self.__pick_hand().lower()
            player_hand = str(input('Enter your choice [r, p, s]: ')).lower()
            if player_hand not in self.choices:
                print('Invalid choice! Try again.')
                continue

            # Determine winner
            if computer_hand == player_hand:
                print(f'Computer picked {computer_hand}')
                print('It\'s a draw!')

            player_won = self.__player_won(player_hand, computer_hand)

            # Display result and Update stats
            if player_won:
                self.player_score += 1
                print(f'You won! Computer picked {computer_hand}')
            else:
                self.computer_score += 1
                print(f'Computer won! Computer picked {computer_hand}')

            self.times_played += 1
            n -= 1

        # Display summary
        self.show_summary()

        return None

    def __player_won(self, player_hand: str, computer_hand: str) -> bool:
        """Check if player wins a round

        Args:
            player_hand (str): A hand from the list of choices
            computer_hand (str): A hand from the list of choices

        Returns:
            bool: Did Player win or not?
        """
        return (player_hand == 'r' and computer_hand == 's') or \
            (player_hand == 'p' and computer_hand == 'r') or \
            (player_hand == 's' and computer_hand == 'p')

    def __pick_hand(self) -> str:
        """Get a hand randomly from the list of choices.

        Returns:
            str: A random hand from the list of choices.
        """

        return random.choice(self.choices)
