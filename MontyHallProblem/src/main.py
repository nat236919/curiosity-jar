"""
PROJECT: Monty Hall Problem
DESCRIPTION: The experiment to prove Monty Hall Problem probability
AUTHOR: Nuttaphat Arunoprayoch
DATE: 23-Feb-2020
"""
# Import libraries
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from typing import List
from game_engine import MontyHall


# Main function
def main() -> None:
    # Inititate the experiment
    rounds = 1000
    monty_hall = MontyHall()
    swap_result = [monty_hall.play(automatic_swap=True) for _ in range(rounds)]
    stay_result = [monty_hall.play() for _ in range(rounds)]
    stats_result = lambda results: len([result for result in results if result]) / len(results)

    # Show result
    print('--- Monty Hall Problem ---')
    print(f'Plays: {rounds} rounds')
    print(f'Swap: Chance of winning {stats_result(swap_result)}')
    print(f'Stay: Chance of winning {stats_result(stay_result)}')

    # Visualization
    df = pd.DataFrame({'swap': stats_result(swap_result),
                        'stay': stats_result(stay_result)}, index=['Result'])
    df.plot.bar()
    plt.show()

    return None


if __name__ == '__main__':
    main()
