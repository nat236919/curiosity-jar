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
