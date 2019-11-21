#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # How many batches can we make?
  batches = 0
  # recipe_keys holds all of the keys in the recipe dictionary
  recipe_keys = [*recipe]
  # ingredients_keys holds all of the keys in the ingredients dictionary
  ingredients_keys = [*ingredients]
  # recipe_values holds all of the values in the recipe dictionary
  recipe_values = recipe.values()
  # ingredients_values holds all of the values in the ingredients dictionary
  ingredients_values = ingredients.values()
  # checking if we have all the ingredients needed, listed in the recipe
  if recipe_keys != ingredients_keys:
    # if we are missing ingredients, we cannot make any batches
    batches = 0
  # if we have all the ingredients
  else:
    # create an array that will check if our ingredients quantities are suffifient enough to make at least 1 batch
    quantity_check = []
    # looping over both recipe_values and ingredients_values, using zip
    for i, j in zip(recipe_values, ingredients_values):
      # if the recipe calls for more than the ingredient we have
      if i > j:
        # append failure to quantity_check
        quantity_check.append("failure")
      else:
        # if we have enough, append success to quantity_check
        quantity_check.append("success")
    # If we end up having a failure in quantity_check, return 0 batches
    if "failure" in quantity_check:
      batches = 0
    else:
      # Create ingredients_batches array that will hold how many times we can use the ingredients
      ingredients_batches = []
      # looping over both recipe_values and ingredients_values, using zip
      for i, j in zip(recipe_values, ingredients_values):
        # divide the value of ingredients by the value of recipes and floor it
        # this allows us to see the most we can produce with each ingredient
        # the lowest number would be our batch quantity
        division = math.floor(j / i)
        # add the floored division to ingredients_batches
        ingredients_batches.append(division)
      # set batches to the smallest value in ingredients_batches
      batches = min(ingredients_batches)
  return batches

# recipe_batches( # should be 0 - missing ingredient
#   {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 },
#   {'milk': 1288, 'flour': 9, 'sugar': 95 }
# )

# recipe_batches( # should be 0 - not enough cheese
#   {'milk': 100, 'butter': 50, 'cheese': 10},
#   {'milk': 198, 'butter': 52, 'cheese': 9}
# )

# recipe_batches( # should be 1
#   {'milk': 100, 'butter': 50, 'cheese': 10},
#   {'milk': 198, 'butter': 52, 'cheese': 10}
# )

# recipe_batches( # should be 2
#   {'milk': 2, 'sugar': 40, 'butter': 20},
#   {'milk': 5, 'sugar': 120, 'butter': 500}
# )

# recipe_batches( # should be 100
#   {'milk': 2},
#   {'milk': 200}
# )

# initial thoughts:
# check if ingredients contains all the keys in recipe
  # if it does 
    # check if all the values in the ingredients are equal to or greater than values in the recipe
      # if it does
        # divide all the values in ingredients by the values in recipe
        # floor the values (we can't make 2.3 of something, but we can make 2)
        # return the smallest value, as that is the maximum we can make
      # if it does not
        # return 0
  # if it does not
    # return 0

# Resources:
# https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python (2nd answer)


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))