"""
Working with for loops in dictionaries and lists
"""

# Hint! Remember that None is useful for setting initial variables as placeholders. You should
# consider setting low and high temperature variables to None, then populating them with the
# first temperature of each day to start comparing them to later temperatures.

# TODO: Create a series of for loops that prints out each day of the week with the high and low of each day.
# TODO: Each day's value is split into times of the day, with each time of day having the average temperature
# TODO: of each hour. In total, each day has 24 temperatures that signify the average temperature of each hour.
# TODO: An example output for each day should be "Sunday has a high of ____ and a low of ____".

ADVANCED_FORECAST = {
    "Sunday": {"morning": [40, 42, 44, 47, 50, 52, 54, 55], "afternoon": [57, 64], "evening": [59, 43]},
    "Monday": {"morning": [38, 50], "afternoon": [52, 66], "evening": [54, 47]},
    "Tuesday": {"morning": [46, 65], "afternoon": [50, 58], "evening": [59, 39]},
    "Wednesday": {"morning": [30, 35], "afternoon": [35, 56], "evening": [48, 29]},
    "Thursday": {"morning": [32, 41], "afternoon": [48, 62], "evening": [60, 37]},
    "Friday": {"morning": [42, 50], "afternoon": [45, 52], "evening": [54, 35]},
    "Saturday": {"morning": [40, 43], "afternoon": [52, 64], "evening": [60, 37]},
}
