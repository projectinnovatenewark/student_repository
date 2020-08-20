"""
Working with lists and dictionaries to convey a weather forecast
"""

# TODO: Section 1:
# Identifying index values

GREEK_LETTERS = ["Alpha", "Beta", "Gamma"]
# Save the item in the list that is equal to index value "0" as a variable, then print the variable. 
# Print the item in the list that is equal to index value "-1" using [] (bracket notation).

# Add the word "Delta" to the list "GREEK_LETTERS".

# Now print the item in the list that is equal to index value "-1" using bracket notation.

####################################################################################################

# TODO: Section 2:
# Combining concepts of lists and dictionaries
DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# In the following dictionary, the keys are associated with days of the week and the
# values represent temperatures. Dictionaries have indexes just like lists do.
TEMPERATURE_FORECAST = {"0": 85, "1": 70, "2": 80, "3": 72, "4": 67, "5": 95, "6": 100}

# Print out "Wednesday" with it's index value from the list "DAYS_OF_WEEK". Set that value equal
# to a variable called "weds" which you will use in the print statement. Then, print
# Wednesday's temperature by using the forecast dictionary. You want to use the "weds" variable
# in your final print statement, but for the temperature, use it's value directly in the print
# statement instead of setting a variable. Your output should read "The temperature on Wednesday
# will be 72 degrees."

####################################################################################################

# TODO: Section 3:
# Print out the first student of the first class followed by the
# starting class time.
classes = [
    {
        'subject': 'math',
        'level': 'linear algebra',
        'students': ['billy', 'beatrice', 'bronny', 'bart'],
        'teacher_description': {
            'name': 'Betty',
            'education': ['Masters of Math', 'Bachelors of Science']
        },
        'classTime': ['11:00 AM', '12:30 PM']
    },
    {
        'subject': 'english',
        'level': 'composition',
        'students': ['chris', 'callie', 'crysta', 'calista'],
        'teacher_description': {
            'name': 'Joanny',
            'education': ['PHD of English', 'Masters of Literacy', 'Bachelors of Biology']
        },
        'classTime': ['1:00 PM', '2:45 PM']
    }
]
