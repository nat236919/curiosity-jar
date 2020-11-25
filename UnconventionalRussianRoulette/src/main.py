"""
PROJECT: CuriosityJar - Unconventional Russian Roulette
DESCRIPTION: Explore and Experiment on Unconventional Russian Roulette's game concepts
AUTHOR: Nuttaphat Arunoprayoch
DATE: 24-Nov-2020
"""
# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

from game_engine import GameEngine

# Load Core GameEngine
game_engine = GameEngine()


# Main Function
def main() -> None:
    # Experimental Results
    experimental_res = game_engine.start_experiment(n=1000)

    # Prepare DataFrame
    df = pd.DataFrame({}, columns=['cat', 'num_of_winning'])
    df = df.append({'cat': 'take_a_shot_won', 'num_of_winning': experimental_res.get('take_a_shot_won')}, ignore_index=True)
    df = df.append({'cat': 'pass_won', 'num_of_winning': experimental_res.get('pass_won')}, ignore_index=True)
    print(df)

    # Visualisation
    fig = px.pie(df, values='num_of_winning', names='cat', hole=.3)
    fig.show()

    return None


if __name__ == '__main__':
    main()
