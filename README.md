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

### How the so call "AI" works

Yes, the so called "AI", since it is technically a bot that runs certain rules created with simple logical thinking. The rules/steps are simple:

1. Look for unique numbers in the dice
2. Apply da rules
3. Repeat step 1 and 2

#### Here are da rules

> **One Unique Number**
> You got the best set, do nothing!
>
> **Two Unique Number**
> Check if the it's Four of a kind or a Full House
> If it is a Full house, do nothing. This is good enough, don't spoil it
> Else, roll the lonely guy there and go for Five in a roll, you have nothing to lose doing that!
>
> **Three Unique Number**
> Check if the it's Three of a kind or a ... an awkward hand, the two-two-one
> For Three of a kind, just reroll the other two
> If you get an awkward hand, throw away the lonely dice, it might suprise you with a Full House
>
> **Four Unique Number**
> AKA DA SHIT HAND
> You got the worst hand, reroll those non-duplicate dices and leave it to fate
>
> **Five Unique Number**
> Well well, is it a straight? If it is, keep your hand away, this is great!
> If no, give the disgusting one a slap and hope you can get straight
