# !/usr/bin/python

import argparse

def find_max_profit(prices):
  # create a max profit array to keep track of max profit
  max_profit_arr = []
  # create a min loss array to keep track of min loss
  min_loss_arr = []
  for i in range(0, len(prices) - 1):
    #check if number on left is bigger than the number on right
    if prices[i] > prices[i + 1]:
      subtraction = prices[i + 1] - prices[i]
      min_loss_arr.append(subtraction)
    #if the number on the left is smaller than the number on the right
    else:
      # create a new array
      new_arr = []
      # pass in all the numbers starting from the small number
      new_arr.extend(prices[i:])
      # create an array to keep track of the profit
      profit = []
      for j in range(0, len(new_arr) - 1):
        # subtract small number from all the numbers to the right
        subtraction = new_arr[j + 1] - new_arr[0]
        # add the result of the subtraction to our profit array
        profit.append(subtraction)
      # add all the subtraction calculation for all the small numbers into our max profit array
      max_profit_arr.extend(profit)
  # create a result variable that will hold our max profit or min loss
  result = 0
  # check if there is a number in the max profit array
  if max_profit_arr:
    # if there are numbers, set result to the biggest profit number
    result = max(max_profit_arr)
  # if there is no number in the max profit array, that means the stock trade is a loss
  else:
    # set the result  to the lowest loss number
    result = max(min_loss_arr)
  # return our best stock trade
  return result

# find_max_profit([1050, 270, 1540, 3800, 2])
find_max_profit([100, 90, 80, 50, 20, 10])


# initial thoughts:
# if left number is > than right number skip
# if left number < right number, subtract that number from all numbers to the right
# check which calculation is the biggest number





if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))