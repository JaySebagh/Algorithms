#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  rps = ["rock", "paper", "scissors"]

  total_combinations = []

  def compute_value(i, c):
    index = c // (3 ** ( i - 1) ) % 3
    print("index here: ", index)
    return rps[int(index)]
  
  def helper(c):
    # create the individual combinations
    individual_combinations = [0] * n
    for i in range(0, len(individual_combinations)):
      individual_combinations[i] = compute_value(n - i, c)
    return individual_combinations
  
  for c in range(0, 3**n):
    result = helper(c)
    total_combinations.append(result)


  return total_combinations

# define rock, paper, and scissors
# loop over each one N times

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

# ['rock', 'rock', 'rock']
# ['rock', 'rock', 'paper']
# ['rock', 'rock', 'scissors']

# ['rock', 'paper', 'rock']
# ['rock', 'paper', 'paper']
# ['rock', 'paper', 'scissors']

# ['rock', 'scissors', 'rock']
# ['rock', 'scissors', 'paper']
# ['rock', 'scissors', 'scissors']

# ['paper', 'rock', 'rock']
# ['paper', 'rock', 'paper']
# ['paper', 'rock', 'scissors']

# ['paper', 'paper', 'rock']
# ['paper', 'paper', 'paper']
# ['paper', 'paper', 'scissors']

# ['paper', 'scissors', 'rock']
# ['paper', 'scissors', 'paper']
# ['paper', 'scissors', 'scissors']

# ['scissors', 'rock', 'rock']
# ['scissors', 'rock', 'paper']
# ['scissors', 'rock', 'scissors']

# ['scissors', 'paper', 'rock']
# ['scissors', 'paper', 'paper']
# ['scissors', 'paper', 'scissors']

# ['scissors', 'scissors', 'rock']
# ['scissors', 'scissors', 'paper']
# ['scissors', 'scissors', 'scissors']









# ['rock', 'rock', 'rock', 'rock'], 
# ['rock', 'rock', 'rock', 'paper'], 
# ['rock', 'rock', 'rock', 'scissors'],

# ['rock', 'rock', 'paper', 'rock'], 
# ['rock', 'rock', 'paper', 'paper'], 
# ['rock', 'rock', 'paper', 'scissors'],

# ['rock', 'rock', 'scissors', 'rock'], 
# ['rock', 'rock', 'scissors', 'paper'], 
# ['rock', 'rock', 'scissors', 'scissors'], 

# ['rock', 'paper', 'rock', 'rock'], 
# ['rock', 'paper', 'rock', 'paper'], 
# ['rock', 'paper', 'rock', 'scissors'], 

# ['rock', 'paper', 'paper', 'rock'], 
# ['rock', 'paper', 'paper', 'paper'], 
# ['rock', 'paper', 'paper', 'scissors'], 

# ['rock', 'paper', 'scissors', 'rock'], 
# ['rock', 'paper', 'scissors', 'paper'], 
# ['rock', 'paper', 'scissors', 'scissors'],

# ['rock', 'scissors', 'rock', 'rock'], 
# ['rock', 'scissors', 'rock', 'paper'], 
# ['rock', 'scissors', 'rock', 'scissors'], 

# ['rock', 'scissors', 'paper', 'rock'], 
# ['rock', 'scissors', 'paper', 'paper'], 
# ['rock', 'scissors', 'paper', 'scissors'], 

# ['rock', 'scissors', 'scissors', 'rock'], 
# ['rock', 'scissors', 'scissors', 'paper'], 
# ['rock', 'scissors', 'scissors', 'scissors'], 

# ['paper', 'rock', 'rock', 'rock'], 
# ['paper', 'rock', 'rock', 'paper'], 
# ['paper', 'rock', 'rock', 'scissors'], 

# ['paper', 'rock', 'paper', 'rock'], 
# ['paper', 'rock', 'paper', 'paper'], 
# ['paper', 'rock', 'paper', 'scissors'], 

# ['paper', 'rock', 'scissors', 'rock'], 
# ['paper', 'rock', 'scissors', 'paper'], 
# ['paper', 'rock', 'scissors', 'scissors'], 

# ['paper', 'paper', 'rock', 'rock'], 
# ['paper', 'paper', 'rock', 'paper'], 
# ['paper', 'paper', 'rock', 'scissors'], 

# ['paper', 'paper', 'paper', 'rock'], 
# ['paper', 'paper', 'paper', 'paper'], 
# ['paper', 'paper', 'paper', 'scissors'], 

# ['paper', 'paper', 'scissors', 'rock'], 
# ['paper', 'paper', 'scissors', 'paper'], 
# ['paper', 'paper', 'scissors', 'scissors'], 

# ['paper', 'scissors', 'rock', 'rock'], 
# ['paper', 'scissors', 'rock', 'paper'], 
# ['paper', 'scissors', 'rock', 'scissors'], 

# ['paper', 'scissors', 'paper', 'rock'], 
# ['paper', 'scissors', 'paper', 'paper'], 
# ['paper', 'scissors', 'paper', 'scissors'], 

# ['paper', 'scissors', 'scissors', 'rock'], 
# ['paper', 'scissors', 'scissors', 'paper'], 
# ['paper', 'scissors', 'scissors', 'scissors'], 

# ['scissors', 'rock', 'rock', 'rock'], 
# ['scissors', 'rock', 'rock', 'paper'], 
# ['scissors', 'rock', 'rock', 'scissors'], 

# ['scissors', 'rock', 'paper', 'rock'], 
# ['scissors', 'rock', 'paper', 'paper'], 
# ['scissors', 'rock', 'paper', 'scissors'], 

# ['scissors', 'rock', 'scissors', 'rock'], 
# ['scissors', 'rock', 'scissors', 'paper'], 
# ['scissors', 'rock', 'scissors', 'scissors'], 

# ['scissors', 'paper', 'rock', 'rock'], 
# ['scissors', 'paper', 'rock', 'paper'], 
# ['scissors', 'paper', 'rock', 'scissors'], 

# ['scissors', 'paper', 'paper', 'rock'], 
# ['scissors', 'paper', 'paper', 'paper'], 
# ['scissors', 'paper', 'paper', 'scissors'], 

# ['scissors', 'paper', 'scissors', 'rock'], 
# ['scissors', 'paper', 'scissors', 'paper'], 
# ['scissors', 'paper', 'scissors', 'scissors'], 

# ['scissors', 'scissors', 'rock', 'rock'], 
# ['scissors', 'scissors', 'rock', 'paper'], 
# ['scissors', 'scissors', 'rock', 'scissors'], 

# ['scissors', 'scissors', 'paper', 'rock'], 
# ['scissors', 'scissors', 'paper', 'paper'], 
# ['scissors', 'scissors', 'paper', 'scissors'], 

# ['scissors', 'scissors', 'scissors', 'rock'], 
# ['scissors', 'scissors', 'scissors', 'paper'], 
# ['scissors', 'scissors', 'scissors', 'scissors']

# 27*3 = 81

# 3^4 = 81
# 3^n