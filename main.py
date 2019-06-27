import player
import random as random
import matplotlib.pyplot as plt
import numpy as np
import collections

def rand():
    return random.randint(1,6)



p1 = player.Player()
# print("Dice:" + str(dice_face))
# print("Score:" + str(p1.checkScore(dice_face)))
# print("Rerolls:" + str(available_rerolls))
# while available_rerolls != 0:
#     rerolls = p1.testPlay1(dice_face, available_rerolls)
#     for x in rerolls:
#         dice_face[x] = rand()
#     print("Dice:" + str(dice_face))
#     print("Score:" + str(p1.checkScore(dice_face)))
#     print("Rerolls:" + str(rerolls))
#     available_rerolls -= 1
# print("Final Score:" + str(p1.checkScore(dice_face)))

test = 10000
scoreList = []
lowScore = 0
game_set_a = []
game_set_b = []
game_roll = []
intial_state = []
while test != 0:
    dice_face = [rand(), rand(), rand(), rand(), rand()]

    # Check initial state
    # intial_state.append(p1.checkState(dice_face))
    
    available_rerolls = 5
    game_set_a.clear()
    game_set_b.clear()
    game_roll.clear()
    while available_rerolls != 0:
        game_set_a.append(dice_face)
        rerolls = p1.testPlay18(dice_face, available_rerolls)
        for x in rerolls:
            dice_face[x] = rand()
        available_rerolls -= 1
        game_set_b.append(dice_face)
        game_roll.append(rerolls)
    score = p1.checkScore(dice_face)
    if score <= 37:
        lowScore += 1
    scoreList.append(score)
    test -= 1

# Print GAME
# while test != 0:
#     dice_face = [rand(), rand(), rand(), rand(), rand()]
#     available_rerolls = 5
#     game_set_a.clear()
#     game_set_b.clear()
#     game_roll.clear()
#     print()
#     print("GAME: XX")
#     while available_rerolls != 0:
#         game_set_a.append(dice_face)
#         print("Before:" + str(dice_face))
#         rerolls = p1.testPlay8(dice_face, available_rerolls)
#         print("Reroll:" + str(rerolls))
#         for x in rerolls:
#             dice_face[x] = rand()
#         available_rerolls -= 1
#         print("After :" + str(dice_face))
#         game_set_b.append(dice_face)
#         game_roll.append(rerolls)


#     scoreList.append(p1.checkScore(dice_face))
#     test -= 1


# Print GRAPH
print("Average: " + str(sum(scoreList)/len(scoreList)))
print("Sum: " + str(sum(scoreList)))
print("Low Score Percentage: " + str((lowScore/len(scoreList))*100) + "%")
c = collections.Counter(scoreList)
c = sorted(c.items())
score = [i[0] for i in c]
freq = [i[1] for i in c]
f, ax = plt.subplots()
plt.bar(score, freq)
plt.title("Score Frequency")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()

# Print Initial State distribution Graph
# c = collections.Counter(intial_state)
# c = sorted(c.items())
# score = [i[0] for i in c]
# freq = [i[1] for i in c]
# f, ax = plt.subplots()
# plt.bar(score, freq)
# plt.title("Unique Number vs Frequency Bar Chart")
# plt.xlabel("Unique Number in Initial State")
# plt.ylabel("Frequency")
# plt.show()