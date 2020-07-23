"""
Using methods on lists and dictionaries
"""

# Section 1. List Methods
sweet_foods = ["ice cream", "skittles", "broccoli", "strawberries", "oreos", "asparagus"]

# TODO: Remove "broccoli" from the sweet_foods list using .remove()

# TODO: Remove the last item in the list using the .pop() method. Do not set it equal to a variable.

# TODO: Use the .pop() method again on the list. This time, use it to remove the first item in the list.
# TODO: Set it equal to a variable called `first_item`, then print that variable.

# TODO: Append the above variable to the `sweet_foods` list.

# TODO: Print the sweet_foods list. Your output should be: ['skittles', 'strawberries', 'oreos', 'ice cream']

# TODO: #########################################################################################

# Section 2. Slicing
values = [1, 2, 3, 4, 5, 6]

# TODO: Segment the items in the list 'values'to include only the odd numers. 
# TODO: Save this slice as the variable 'odd'. Then, print 'odd'.
# TODO: (Hint: Use a stepper, which would skip every other number)

# TODO: Now segment the last number in 'odd' and save this additional slice as the variable 'last'. 
# TODO: Then, print 'last'.

# TODO: #########################################################################################

# Section 3. Dictionary Methods.
my_car = {"make": "Tesla", "model": "Cybertruck", "year": "2022"}

# TODO: Use the .get() method on the my_car dictionary to search for the `car_type` key. Set it equal to a
# TODO: variable called c_type. If that key doesn't exist, have the .get() method return "type doesn't exist".
# TODO: Print that variable.

# TODO: Lets add a key/value pair of "car_type": "Electric" to the above my_car dictionary

# TODO: Use the .pop() method to remove the "year" key/value pair from the my_car dict. Set it equal
# TODO: to a variable called `year`. Print the `year` variable and print the `my_car` dictionary.

# TODO: #########################################################################################

# Section 4. Combining list/dict Methods
# TODO: Append a string "make" to the sweet_foods list. Set a variable equal to the last item in the newly
# TODO: updated list ( i.e. make_item = sweet_foods[4] ). Then, since the new variable will be equal
# TODO: to a string of "make", you can use that variable to find the value of the key/value pair in the
# TODO: my_car dictionary. Print out the output of using this variable to access that value
# TODO: ex: print(my_car[make_item])
