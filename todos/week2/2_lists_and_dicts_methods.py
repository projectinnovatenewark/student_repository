"""Todo for lists and dictionary methods"""

pro_sports = ["NBA", "MLB", "WNBA", "NFL"]

# TODO: Remove MLB from your shopping list using the .remove method then print the list

pro_sports.remove("MLB")
print(pro_sports)

# TODO: Then add NHL to your list, then print the third item last item using index position
# TODO: Save each to vairables named third_item and last_item
# TODO: Print in this format: "Third Item: NFL - Last Item NHL"

pro_sports.append("NHL")
third_item = pro_sports[2]
last_item = pro_sports[-1]
print("Third Item:", third_item, "- Last Item:", last_item)

# TODO: Now in the original list, remove NFL 
# TODO: from the list using the .pop method and print NFL

pro_sports = ["NBA", "MLB", "WNBA", "NFL"]

football = pro_sports.pop()
print(football)

# TODO: The below dictionary contans some countries with their capitals,
# TODO: Add Bangkok, Thailand to the dictionary.

countries = {
    "Spain": "Mardid",
    "Italy": "Rome",
    "Argentina": "Buenos Aires",
    "United States": "Washington D.C."
}

countries["Thailand"] = "Bangkok"

print(countries)

# TODO: Let's say we want to see if England is in our dictionary. Use the .get
# TODO: method to return England's value. If England isn't in the dictionary
# TODO: have the value returned be "Not in Dict". Set it to the 
# TODO: variable get_england and print it.

get_england = countries.get("England", "Not in Dict")
print(get_england)