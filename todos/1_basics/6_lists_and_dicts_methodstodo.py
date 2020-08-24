"""
Using methods on lists and dictionaries
"""

# TODO: Section 1:
sweet_foods = ["ice cream", "skittles", "broccoli", "strawberries", "oreos", "asparagus"]

# Remove "broccoli" from the sweet_foods list using .remove()

# TODO: Section 1.1:
# Remove the last item in the list using the .pop() method. Do not set it equal to a variable.

# TODO: Section 1.2:
# Use the .pop() method again on the list. This time, use it to remove the first item in the list.
# Set it equal to a variable called "first_item", then print that variable.

# TODO: Section 1.3:
# Append the above variable to the "sweet_foods" list.

# TODO: Section 1.4:
# Print the sweet_foods list. Your output should be:
# ['skittles', 'strawberries', 'oreos', 'ice cream']

####################################################################################################

# TODO: Section 2:
values = [1, 2, 3, 4, 5, 6]

# Segment the items in the list "values" to include only the even numbers.
# Save this slice as the variable "even". Then, print the "even" variable.
# HINT: Use a stepper, which would skip every other number)

####################################################################################################

# TODO: Section 3:
my_car = {"make": "Tesla", "model": "Cybertruck", "year": "2022"}

# Use the .get() method on the my_car dictionary to search for the "car_type" key. Set it equal
# to a variable called "c_type". If that key doesn't exist, have the .get() method return
# "type doesn't exist". Print that variable.

# TODO: Section 3.1:
# Lets add a key/value pair of "car_type": "Electric" to the above "my_car" dictionary

# TODO: Section 3.2:
# Use the .pop() method to remove the "year" key/value pair from the "my_car" dict. Set it equal
# to a variable called "year". Print the "year" variable and print the "my_car" dictionary.

# TODO: Section 3.3:
automobile_attributes = ['color', 'engine', 'door count']

# Append a string "make" to the automobile_attributes list. Set a variable equal to the last item in
# the newly updated list.

# Now, since the new variable will be equal to a string of "make", you can use that variable
# to find the value of the key/value pair in the "my_car" dictionary in the format "dict[key]".

# TODO: Section 3.4:
# Print out the output of using this variable to access that value
# ex: print(dict_name[var_with_key])
