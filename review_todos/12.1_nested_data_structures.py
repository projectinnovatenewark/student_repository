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
    "Sunday": {
        "morning": [40, 42, 44, 47, 50, 52, 54, 55],
        "afternoon": [57, 59, 56, 60, 62, 63, 64, 64],
        "evening": [60, 61, 59, 57, 55, 52, 48, 43]
    },
    "Monday": {
        "morning": [38, 40, 42, 44, 46, 48, 49, 50],
        "afternoon": [52, 55, 57, 60, 62, 64, 65, 66],
        "evening": [63, 61, 60, 60, 57, 54, 50, 47]
    },
    "Tuesday": {
        "morning": [46, 49, 50, 52, 57, 59, 62, 65],
        "afternoon": [63, 60, 60, 55, 53, 50, 50],
        "evening": [50, 49, 49, 45, 42, 41, 40, 39]
    },
    "Wednesday": {
        "morning": [30, 32, 33, 33, 34, 35, 35, 36],
        "afternoon": [37, 37, 39, 40, 43, 44, 46, 46],
        "evening": [45, 42, 38, 35, 34, 32, 30, 29]
    },
    "Thursday": {
        "morning": [32, 34, 36, 37, 40, 40, 41, 41],
        "afternoon": [42, 44, 45, 46, 50, 52, 57, 60],
        "evening": [59, 56, 54, 52, 50, 50, 48, 47]
    },
    "Friday": {
        "morning": [42, 44, 45, 46, 46, 48, 49, 50],
        "afternoon": [51, 53, 53, 56, 57, 57, 55, 52],
        "evening": [54, 53, 53, 54, 51, 49, 48, 46]
    },
    "Saturday": {
        "morning": [40, 41, 42, 42, 43, 43, 44, 45],
        "afternoon": [47, 48, 48, 50, 52, 51, 50, 50],
        "evening": [50, 49, 47, 45, 43, 40, 39, 37]
    },
}
