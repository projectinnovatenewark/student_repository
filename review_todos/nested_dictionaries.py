youth_groups = {
    "Acting Class": {
        "members": ["Janet", "Samma", "Ali"],
        "location": "Passaic",
        "purpose": "Learn to act",
    },
    "Girls Who Code": {
        "members": ["Alysse", "Zoe", "Wendy"],
        "location": "Newark",
        "purpose": "Promote growth and fellowship in female developers"
    },
    "Book Club": {
        "members": ["Quentin", "Zacharius", "Moses"],
        "location": "Jersey City",
        "purpose": "Read cool books and chat about it"
    }
}

# TODO: Output the following formatted message for each youth group:
# TODO: "name1, name2, and name3 are a part of the (organization here). They meet in (location here) to (purpose here)."

for g in youth_groups:
    members = youth_groups[g]["members"]
    mems = f"{members[0]}, {members[1]}, and {members[2]}"
    print(mems)