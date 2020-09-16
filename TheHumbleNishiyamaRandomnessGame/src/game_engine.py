"""
FILE: game_engine.py
DESCRIPTION: A file containing game logics
AUTHOR: Nuttaphat Arunoprayoch
DATE: 09-SEP-2020
"""
# Import libraries
import random
from typing import List, Dict, Any


# Core Game Engine
class GameEngine:
    """ Two players play the game using an ordinary deck of cards.
        The cards will be dealt out in a row, one after another. 
        Before the dealing begins, each player claims an ordered sequence of colors that might turn up, 
        for example “red black red” (RBR) or “black red red” (BRR). 
        As the cards are dealt, if three successive cards turn up in one of these sequences, 
        the player who claimed it gets to collect those three cards as a trick, and the dealing continues. 
        When all 52 cards have been dealt, the player who has collected the most tricks wins
        (In a typical game, 7 to 9 tricks are won.)
    """
    
    def __init__(self) -> None:
        """ Generate a deck of cards containing blacks (26) and reds (26) """
        self.all_cards = ['black' for _ in range(26)] + ['red' for _ in range(26)]
    
    def _card_selection(self) -> List[str]:
        """ Select patterns of cards (n=3)
            return ['black', 'black', 'red']
        """
        return [random.choice(self.all_cards) for _ in range(3)]
    
    def _card_selection_winning(self, reference_sequence: List[str]) -> List[str]:
        """ Apply a winning method
            Take a middle value, conjugate, put it in fromt of the sequence, and ditch the last value
            Ex.1) BBR -> RBBR -> RBB
            Ex.2) RRR -> BRRR -> BRR
        """
        if not isinstance(reference_sequence, list) or len(reference_sequence) not in [3]:
            return []
        converted_value = 'red' if reference_sequence[1] in ['black'] else 'black'
        winning_sequence = reference_sequence[:2]
        winning_sequence.insert(0, converted_value)
        return winning_sequence
    
    def _check_result(self, computer_sequence: List[str],
                                player_sequence: List[str],
                                current_game_sequence: List[str]) -> Dict[str, bool]:
        """ Check the result of a game
            All sequences must contain the same length of elements
            return the result of a player winnig a game or not
        """
        result = {
            'computer_has_won': False,
            'player_has_won': False
        }

        if computer_sequence == current_game_sequence:
            result['computer_has_won'] = True

        if player_sequence == current_game_sequence:
            result['player_has_won'] = True

        return result
    
    def _play(self, is_winning_method_used = False) -> None:
        """ Play the game """
        deck = self.all_cards.copy() # Get a dek of cards
        random.shuffle(deck) # Shuffle a deck (in place)

        # Select patterns
        computer_sequence = self._card_selection()
        player_sequence =  self._card_selection_winning(computer_sequence) \
                                if is_winning_method_used else self._card_selection()
        
        # Start playing game
        current_game_sequence = []
        final_result = {}
        while deck:
            drawn_card = deck.pop()
            current_game_sequence.append(drawn_card)
            # Adjust current_game_sequence to contain only three elements
            if len(current_game_sequence) > 3:
                current_game_sequence = current_game_sequence[-3:]
            # Check the result
            if len(current_game_sequence) == 3:
                game_result = self._check_result(computer_sequence, player_sequence, current_game_sequence)
                if True in game_result.values():
                    final_result = game_result.copy()
                    break

        return final_result
    
    def start_experiment(self, is_winning_method_used = False, n: int = 1000) -> Dict[str, int]:
        """ Start an experiment and Display the result """
        experimental_result = {'player_won': 0, 'computer_won': 0}
        if not isinstance(n, int):
            return None
        
        for _ in range(n):
            game_result = self._play(is_winning_method_used)
            experimental_result['player_won'] += game_result['player_has_won']
            experimental_result['computer_won'] += game_result['computer_has_won']

        return experimental_result
