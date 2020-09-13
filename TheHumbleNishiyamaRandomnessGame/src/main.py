"""
PROJECT: CuriosityJar - The Humble-Nishiyama Randomness Game
DESCRIPTION: Explore and Experiment on Penney's game concepts
AUTHOR: Nuttaphat Arunoprayoch
DATE: 09-SEP-2020
"""
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from game_engine import GameEngine


# Load Core GameEngine
game_engine = GameEngine()


# Main function
def main() -> None:
    # Without a winning method
    without_winning_method_res = game_engine._start_experiment(is_winning_method_used=False)
    
    # With a winning method
    with_winning_method_res = game_engine._start_experiment(is_winning_method_used=True)

    # Prepare DataFrame
    df_without_winning_method = pd.DataFrame([without_winning_method_res])
    df_without_winning_method['cat'] = 'without'
    df_with_winning_method_res = pd.DataFrame([with_winning_method_res])
    df_with_winning_method_res['cat'] = 'with'
    df_final = pd.concat([df_without_winning_method, df_with_winning_method_res])
    df_final = df_final.set_index('cat')
    print(df_final)

    # Visualisation
    df_final.plot.bar()
    plt.show()

    return None


# Execute the script
if __name__ == '__main__':
    main()
