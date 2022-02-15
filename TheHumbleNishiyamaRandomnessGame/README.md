# The Humble-Nishiyama Randomness Game

* Game GUI: https://humble-nishiyama-randomness-game.netlify.app/

The rule of the game is simple, there is a deck of cards containing 26 black cards and 26 red ones. Two players select their own sequence consisting three colours (e.x., RED RED BLACK).

The game is played by drawing a card one by one, the winner is the one whose sequence appears first.

This seems to be a fair game; however, there is a solution that allows **player (B)** has a higher chance of winning than **player (A)**.

## Winning solution
With this solution, **player (B)** guarantees to have 70% chance of winning.
* Take a reference sequence **RED RED BLACK**
* Copy a second value, invert it, and put it in front of the sequence **BLACK RED RED BLACK**
* Remove the last value from the sequence **BLACK RED RED**

<p align="center">
    <img src="https://i.ibb.co/8Xzn74K/Screen-Shot-2020-09-13-at-8-30-38-PM.png" alt="Screen-Shot-2020-09-13-at-8-30-38-PM" border="0">
</p>

### References
* [Penney's game](https://en.wikipedia.org/wiki/Penney%27s_game)
* [Run Toppers](https://www.futilitycloset.com/2010/10/08/run-toppers/)
* [The Humble-Nishiyama Randomness Game](https://www.futilitycloset.com/2016/12/31/humble-nishiyama-randomness-game/)
