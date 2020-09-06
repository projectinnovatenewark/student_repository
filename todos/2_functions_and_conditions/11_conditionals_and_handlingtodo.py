"""
Conditions and while loops
"""

# TODO: Section 1

# Generate a user input asking for a number. Write an "if-else" statement that tells
# the user whether it is an odd or even number. Make sure the user's number is converted
# from a string to an integer, or else you'll get an error!


##################################################################################################

# TODO: Section 2

unconfirmed_users = ['alice', 'brian', 'candace', 'alshon']
confirmed_users = []

##################################################################################################

# TODO: "Verify" each user by removing them one-by-one and move "verified"
#  users into the confirmed users list by using a while loop. 
# 
# IMPORTANT: Remember,while loops will run for a list as long as there are items in it.

# FIXME: uncomment the line of code below when beginning section 2
# while unconfirmed_users:

##################################################################################################
# TODO: Section 2.

# Display all the confirmed users with a for loop. Each user statement should output
# "[user_name] has been confirmed".

##################################################################################################

# TODO: Section 2.1

#  Lets use list comprehension and create a new list with every name capitalized
# from `confirmed_users` called `upper_users`.

##################################################################################################
# TODO: Section 3

#  Let's implement a while loop, instead of a for loop, that uses the length of the
# new list of `upper_users` to iterate through the names. For each iteration, we want the
# output to be formatted as "confirmed [user]".

# Hint: Remember, if we want to access the length of a list we use len(list). Consider how
# we can use the list's length in a variable and then decrement it. Lesson 9 is a helpful
# resource for this problem. Consider using the variable to index the list.

##################################################################################################

# TODO: Section 3.1

# Use the enumerate function to iterate through the confirmed_users list. The output for
# each user should read "User number [x]'s name is [name]." X should start with 1 for the
# first user and iterate up by one, and the name represents the user's name. 
