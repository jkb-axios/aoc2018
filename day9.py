#!/bin/env python

# 431 players; last marble is worth 70950 points

# examples:
'''
10 players; last marble is worth 1618 points: high score is 8317
13 players; last marble is worth 7999 points: high score is 146373
17 players; last marble is worth 1104 points: high score is 2764
21 players; last marble is worth 6111 points: high score is 54718
30 players; last marble is worth 5807 points: high score is 37305
'''

num_players = 431
last_marble_worth = 70950*100

# test1
#num_players = 10
#last_marble_worth = 1618

# test2
#num_players=13
#last_marble_worth = 7999

players = [0]*num_players

circle = [0,2,1]
current_marble_index = 1
next_marble_number = 3
last_score = 0
turn = 3

while next_marble_number < last_marble_worth:
  if next_marble_number%23 == 0:
    # special case
    remove_idx = (current_marble_index-7)%len(circle)
    remove_val = circle[remove_idx]
    del circle[remove_idx]
    current_marble_index = remove_idx
    last_score = next_marble_number + remove_val

    player = turn%num_players
    players[player] += last_score
    #print 'Turn %s: Player %s scores %s (marble %s + removed %s)'%(turn,player,last_score,next_marble_number,remove_val)
  else:
    current_marble_index = (current_marble_index+2)%len(circle)
    if current_marble_index == 0:
      current_marble_index = len(circle)
    circle.insert(current_marble_index, next_marble_number)

  # increment for next turn
  turn += 1
  next_marble_number += 1

  #print '%s: %s'%(turn,circle)
  if turn%10000 == 0:
    print 'Turn: %s, cur_idx: %s, next_num: %s'%(turn,current_marble_index,next_marble_number)
  #inp = raw_input()

print 'High Score: Player %s with %s'%(players.index(max(players))+1,max(players))
#for elf,score in enumerate(players):
#  print elf+1,score


