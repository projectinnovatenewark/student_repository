"""
Working with for loops in dictionaries and lists
"""

# Section 1 of TODO: #########################################################################################
# Section 1 of TODO: Print numbers 5 through 10. Print each number using a basic for loop.
for num in range(5,11):
    print(num)
print("\n")

# Section 2 of TODO: #########################################################################################
# Section 2 of TODO: Loop through the list above and "curve" each grade by 3 points. Print those
# Section 2 of TODO: curved grades. In that loop, print out the student's number using the .index() function.
# Section 2 of TODO: Your first iteration should read in the format "Student 1 got a 63." and that should
# Section 2 of TODO: continue through all items in the list.

grades = [60, 73, 80, 87]

for grade in grades:
    cg = grade + 3
    print(cg)
print("\n")

# Section 3 of TODO: #########################################################################################
# Section 3 of TODO:
# Section 3 of TODO: Write a while loop and iterate through the list of todos. Use the "pop" method so that,
# Section 3 of TODO: for each iteration, you can print the todo that you are removing from the todolist.

todos = ["exercise for fun", "eat food", "go to school", "write some code"]
removed_todo = []

while todos:
    current_todo = todos.pop()
    print("I don't want to " + current_todo, "anymore!")
    print("\n")


# Section 4 of TODO: #########################################################################################
# Section 4 of TODO:
# Section 4 of TODO: Decrement var by 1 using a while loop. Print the number each time
# Section 4 of TODO: it is decremented. Once the number reaches two, end the while loop.

var = 7
while var > 1:
    var -= 1
    print(var)
print("\n")

# Section 5 of TODO: #########################################################################################
# Section 5 of TODO: 
# Section 5 of TODO: in the following dictionary, keys are associated with days of the week & values represent
# Section 5 of TODO: temps notice how, when in one line, the characters surpass our self-imposed 100 character
# Section 5 of TODO: limit therefore, we can format our dictionary like such to stick to our format!

# Section 5 of TODO: Here is a weather forecast with average temperatures for each day.
# Section 5 of TODO: since our dictionary has a lot of items, let's split it over many lines.
# Section 5 of TODO: Create a for loop that prints out each day of the week with the average temperature

TEMPERATURE_FORECAST = {
    "Sunday": 65,
    "Monday": 70,
    "Tuesday": 80,
    "Wednesday": 70,
    "Thursday": 67,
    "Friday": 95,
    "Saturday": 100
}

for day in TEMPERATURE_FORECAST:
    temp = TEMPERATURE_FORECAST[day]
    print("The temperature for", day, "is", temp, "degrees.")
