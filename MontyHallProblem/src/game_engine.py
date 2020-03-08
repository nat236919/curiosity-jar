"""
FILE: game_engine.py
DESCRIPTION: The file contains the Monty Hall game mechanism
AUTHOR: Nuttaphat Arunoprayoch
DATE: 23-Feb-2020
"""
# Import libraries
import random
import numpy as np
from typing import List, Dict, Any


# Monty Hall mechanism
class MontyHall():
    """ Monty Hall Game Mechanism
        1. There are 3 doors to be selected, and one of the doors contains a reward. The rest is empty
        2. Choose 1 door of the three doors
        3. Reveal ONLY 1 empty door: (1 opened, 2 left unopened)
        4. Give a choice to a player whether to swtich or not
        5. Open all the doors
        6. Summarise the result (reward found = 1, empty = 0)
    """
    def play(self, automatic_swap: bool = False) -> bool:
        """ Play a game with an option to swap automatically """
        self.doors = list(range(3)) # doors: [0] [1] [2]
        self.award_door = random.choice(self.doors)
        user_selection = random.choice(self.doors)

        # Determine the result (Swap)
        if automatic_swap:
            if user_selection != self.award_door:
                return True
            else:
                return False
        
        # Determine the result (Stay)
        result =  bool(user_selection == self.award_door)

        return result
