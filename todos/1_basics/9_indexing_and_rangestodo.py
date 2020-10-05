"""
Working with for loops in dictionaries and lists
"""

# TODO: Section 1:
# Print numbers 5 through 10. Print each number using a basic for loop.

####################################################################################################

# TODO: Section 2:
# Loop through the list below and "curve" each grade by 3 points. Print those
# curved grades. In that loop, print out the student's number using the .index() function.
# Your first iteration should read in the format "Student 1 got a 63." and that should
# continue through all items in the list.

grades = [60, 73, 80, 87]

####################################################################################################

# TODO: Section 3: 
# In the following dictionary, keys are associated with days of the week & values represent
# temperatures.

# TIP: Notice how when in one line, the characters surpass our self-imposed 100 character
# TIP: limit therefore, we can format our dictionary like such to stick to our format!

# Here is a weather forecast with average temperatures for each day.
# Since our dictionary has a lot of items, let's split it over many lines.
# Create a for loop that prints out each day of the week with its associated temperature.

TEMPERATURE_FORECAST = {
    "Sunday": 65,
    "Monday": 70,
    "Tuesday": 80,
    "Wednesday": 70,
    "Thursday": 67,
    "Friday": 95,
    "Saturday": 100
}
