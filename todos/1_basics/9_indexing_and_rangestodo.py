"""
Working with for loops in dictionaries and lists
"""

# TODO: Section 1:
# Print numbers 5 through 10. Print each number using a basic for loop.

####################################################################################################

# TODO: Section 2:
# Loop through the list above and "curve" each grade by 3 points. Print those
# curved grades. In that loop, print out the phone name using the .index() function.
# Ypur print statement should read in the format "Phone [index + 1] is a [phone]." and that should
# continue through all items in the list.
phones = ["iPhone", "Galaxy", "Pixel", "Note"]

# TODO: Section 2.1:
# Now loop through the dictionary below. This time use a variable to reference each key's value,
# and print  "[company] is the maker of the [phone]."
phones = {"Apple": "iPhone", "Samsung": "Galaxy", "Google": "Pixel", "Samsung": "Note"}

####################################################################################################

# TODO: Section 3:
# Write a while loop and iterate through the list of todos. Use the "pop" method so that,
# for each iteration, you can then append the todo to the "removed_todo" list. Then print
# the new list.
todos = ["exercise for fun", "eat food", "go to school", "write some code"]
removed_todo = []

####################################################################################################

# TODO: Section 4: 
# In the following dictionary, keys are associated with days of the week & values represent
# temperatures. Here is a weather forecast with average temperatures for each day. Since our
# dictionary has a lot of items, let's split it over many lines. Create a for loop that prints
# out each day of the week with its associated temperature.

# TIP: Notice how when in one line, the characters surpass our self-imposed 100 character
# TIP: limit therefore, we can format our dictionary like such to stick to our format!

TEMPERATURE_FORECAST = {
    "Sunday": 65,
    "Monday": 70,
    "Tuesday": 80,
    "Wednesday": 70,
    "Thursday": 67,
    "Friday": 95,
    "Saturday": 100
}
