"""
Using methods on lists and dictionaries
"""

# Lets start with list methods

sweet_foods = ["ice cream", "skittles", "broccoli", "strawberries", "oreos", "asparagus"]

# TODO: Remove "broccoli" from the sweet_foods list using .remove()

# TODO: Remove the last item in the list using the .pop() method. Do not set it equal to a variable.

# TODO: Use the .pop() method again on the list. This time, use it to remove the first item in the list.
# TODO: Set it equal to a variable called `first_item`, then print that variable.

# TODO: Append the above variable to the `sweet_foods` list.

# TODO: Print the sweet_foods list. Your output should be: ['skittles', 'strawberries', 'oreos', 'ice cream']

# Now onto dictionary methods

my_car = {"make": "Tesla", "model": "Cybertruck", "year": "2022"}

# TODO: Use the .get() method on the my_car dictionary to search for the `car_type` key. Set it equal to a
# TODO: variable called c_type. If that key doesn't exist, have the .get() method return "type doesn't exist".
# TODO: Print that variable.

# TODO: Lets add a key/value pair of "car_type": "Electric" to the above my_car dictionary

# TODO: Use the .pop() method to remove the "year" key/value pair from the my_car dict. Set it equal
# TODO: to a variable called `year`. Print the `year` variable and print the `my_car` dictionary.

# Combining concepts

# TODO: Append a string "year" to the sweet_foods list. Set a variable equal to the last item in the newly
# TODO: updated list ( i.e. year_item = sweet_foods[4] ). Then, since the new variable will be equal
# TODO: to a string of "year", you can use that variable to find the value of the key/value pair in the
# TODO: my_car dictionary. Print out the output of using this variable to access that value
# TODO: ex: print(my_car[year_item])