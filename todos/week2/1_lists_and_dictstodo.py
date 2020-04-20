"""
Working with lists and dictionaries to convey a weather forecast
Reference lesson(s): week_2/1_lists_and_dicts.py
"""

# TODO: Create a list with days from Monday through Sunday
DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# TODO: In the following dictionary, the keys are associated with days of the week while
# TODO: values represent temps the first value of 0 represents Sunday's temperature all
# TODO: the way to 6 which represents Saturday
TEMPERATURE_FORECAST = {"0": 85, "1": 70, "2": 80, "3": 72, "4": 67, "5": 95, "6": 100}

# TODO: Print out Wednesday by accessing it through the list `DAYS_OF_WEEK`. Set that value equal
# TODO: to a variable called `weds` which you will use in the print statement. Then, print
# TODO: Wednesday's temperature by using the forecast dictionary. You want to use the `weds` variable
# TODO: in your final print statement, but for the temperature, use it's value directly in the print statement
# TODO: instead of setting a variable. Your output should read `The temperature on Wednesday will be 72 degrees.`
