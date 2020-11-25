"""
FILE: game_engine.py
DESCRIPTION: A file containing game logics
AUTHOR: Nuttaphat Arunoprayoch
DATE: 24-Nov-2020
"""
# Import libs
import random
from typing import List, Dict, Any


# Core Game Engine
class GameEngine:
    """ Unlike its original rules, Unconventional Russian Roulett puts 2 bullets
        in the cylinder (n=6) **adjacently**. The game proceeds as usual in which the cylinder is initially spun,
        and each player takes turn to pull the trigger. The survival wins, obviously.

        Assume, we were "Player B" starting second round. After the first round had been played by Player A, and he/she survived.
        Now it is out turn to play; however, you were given a choice to take a shot or to stay. Here are rules
            - If we took a shot, and it was empty -> WE WON 1 MILIION DOLLARS
            - If we chose to stay, and it was loaded -> WE WON 1 MILIION DOLLARS
            
        The question raised here is that
            - Should we take a shot or not? and why?
            - Assuming that our main goal was to get 1 million dollars at all costs
    """

    def __init__(self) -> None:
        """ Generate cylinders (6 rounds)
            0   -> Empty (n=3)
            1   -> Loaded (n=3)
        """
        self._load_cylinder()
    
    def _load_cylinder(self) -> None:
        self.loaded_cylinder = [1, 1, 1] + [0 for _ in range(3)] # 3 loaded; 3 empty
    
    def _spin_cylinder(self) -> None:
        """ Simulate spinning cylinder """
        random_spin_num = random.randrange(1, 7) # random 1 - 6
        self.loaded_cylinder = self.loaded_cylinder[random_spin_num:] + self.loaded_cylinder[:random_spin_num]
    
    def _play(self, take_a_shot: bool = False) -> bool:
        """ Play the game
            1.) Player A will guarantee to survive the first round
            2.) Player B will need to choose to whether take a shoot or stay
            3.) The game will stop at the Player B's first round for simplicity
        """
        # Keep spinning to make sure the first round is not loaded
        self._load_cylinder()
        while self.loaded_cylinder[0] == 1:
            self._spin_cylinder()
    
        # Skip the first round since it is guaranteed to be empty for Player A
        has_player_won_million = False
        for bullet in self.loaded_cylinder[1:]:
            if take_a_shot and bullet == 0:
                has_player_won_million = True
            elif not take_a_shot and bullet == 1:
                has_player_won_million = True
            break
        return has_player_won_million
    
    def start_experiment(self, n: int = 1000) -> Dict[str, List[bool]]:
        experimental_results = {'game_num': n, 'take_a_shot_won': [], 'pass_won': []}
        if not isinstance(n, int):
            return experimental_results

        experimental_results['take_a_shot_won'] = sum([self._play(take_a_shot=True) for _ in range(n)])
        experimental_results['pass_won'] = sum([self._play(take_a_shot=False) for _ in range(n)])
        return experimental_results
