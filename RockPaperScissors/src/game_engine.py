"""
FILE: game_engine.py
DESCRIPTION: A game engine for Rock Paper Scissors against the computer.
AUTHOR: Nuttaphat Arunoprayoch (@nuttaphat)
DATE: 24-Jan-2022
"""
import random


class RockPaperScissors:
    """A game engine class for Rock Paper Scissors against the computer.
    """

    def __init__(self):
        self.choices = ['r', 'p', 's']
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0
        self.times_played = 0

        self.player_last_played = {
            'choice': None,
            'result': None,
        }
        self.computer_last_played = {
            'choice': None,
        }

    def show_summary(self) -> None:
        """Display statistical results
        """
        if not self.times_played:
            text = 'No games played yet.'
        else:
            won_rate = self.player_score / self.times_played
            text = f"""
            --------------------- Summary ----------------------
                Played {self.times_played} times.
                You won {self.player_score} times.
                The computer won {self.computer_score} times.
                Draws: {self.draws} times.
                Player won {won_rate * 100}% of the time.
            ----------------------------------------------------
            """

        print(text)

        return None

    def play(self, n: int = 1, autoplay=False, apply_strategy=False) -> None:
        """Play game n times.

        Args:
            n (int, optional): times to be played. Defaults to 1.
            autoplay (bool, optional): randomly choose a hand for player
            apply_strategy (bool, optional): apply a strategy to the player

        Returns:
            [None]
        """
        while n > 0:
            # Computer picks a hand
            computer_hand = self.__pick_hand().lower()

            # Player picks a hand
            if autoplay:
                player_hand = self.__strategic_pick_hand() if apply_strategy else self.__pick_hand()
            else:
                player_hand = str(
                    input('Enter your choice [r, p, s]: '))

            print(f'Player picked [{player_hand}]')
            print(f'Computer picked [{computer_hand}]')

            if player_hand not in self.choices:
                print('Invalid choice! Try again.')
                continue

            # Determine winner (player-based)
            result = self.__determine_result(player_hand, computer_hand)
            if result == 0:
                print('It\'s a draw!')
                self.draws += 1
            elif result == 1:
                self.player_score += 1
                print(f'You won! Computer picked {computer_hand}')
            elif result == 2:
                self.computer_score += 1
                print(f'Computer won! Computer picked {computer_hand}')

            # Update other stats
            self.times_played += 1
            self.player_last_played.update({
                'choice': player_hand,
                'result': result,
            })
            self.computer_last_played.update({
                'choice': computer_hand,
            })
            n -= 1

        # Display summary
        self.show_summary()

        return None

    def __determine_result(self, player_hand: str, computer_hand: str) -> int:
        """Return the result of a round

        Args:
            player_hand (str): A hand from the list of choices by player
            computer_hand (str): A hand from the list of choices by computer

        Returns:
            int: {
                0: draw,
                1: player wins,
                2: computer wins
            }

        Raises:
            ValueError: if player_hand or computer_hand is not in choices
        """
        if not player_hand or not computer_hand:
            raise ValueError('Invalid input!')

        if player_hand == computer_hand:
            return 0

        return 1 if self.__player_won(player_hand, computer_hand) else 2

    @staticmethod
    def __player_won(player_hand: str, computer_hand: str) -> bool:
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

        Raises:
            ValueError: if choices is empty
        """
        if not self.choices:
            raise ValueError('No choices available!')

        return random.choice(self.choices).lower()

    def __pick_winning_hand(self, hand: str) -> str:
        """Get a winning hand based on a given play

        Args:
            hand (str): A hand from the list of choices

        Returns:
            str: A winning hand from the list of choices

        Raises:
            ValueError: if hand is not given or not in choices
        """
        if not hand or hand not in self.choices:
            raise ValueError('Invalid input!')

        winning_hand = None
        if hand == 'r':
            winning_hand = 'p'
        elif hand == 'p':
            winning_hand = 's'
        elif hand == 's':
            winning_hand = 'r'

        return winning_hand.lower()

    def __strategic_pick_hand(self) -> str:
        """Get a hand based on the player last played

        Returns:
            str: A hand from the list of choices based on the player last played

        References:
            https://arstechnica.com/science/2014/05/win-at-rock-paper-scissors-by-knowing-thy-opponent/
        """
        if not self.player_last_played.get('choice'):
            return self.__pick_hand()

        # In case of a draw and a win, pick the hand that beats the player's last hand
        hand = None
        if self.player_last_played.get('result') in [0, 1]:
            hand = self.__pick_winning_hand(
                self.player_last_played.get('choice'))
        # In case of a loss, pick the hand that beats to the computer's last hand
        elif self.player_last_played.get('result') == 2:
            hand = self.__pick_winning_hand(
                self.__pick_winning_hand(self.computer_last_played.get('choice')))

        return hand.lower()
