# AI for Dice Game

## Rules of Game

- In every game, the player has 5 dice.
- The player is allowed 5 rerolls.
- For each reroll, the player can decide which dice to be kept and choose any number of dice to reroll.
- The game ends after 5 rerolls or when the player - decides not to reroll.
- After the game ends, points are calculated based on the output combination of the dice.
- Every player will play 5 games.


### Points

| Dice combinations | Points |
| - | - |
| Five-in-a-row | Sum of dice + 70 |
| Straight (1-2-3-4-5, 2-3-4-5-6) | Sum of dice + 60 |
| Full house (Three + Two of a kind) | Sum of dice + 50 |
| Four-of-a-kind (Four + One) | Sum of dice + 40 |
| Three-of-a-kind (Three + One + One) | Sum of dice + 30 |
| Other combinations | Sum of dice |

### The so call AI

Yes, the so called "AI", since it is technically a bot that runs certain rules created with simple logical thinking. The rules/steps are simple:

1. Look for unique numbers
