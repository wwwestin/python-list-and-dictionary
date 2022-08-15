import json

shows = open('shows-data.json')

show_data = json.load(shows)


# Problem 1:
# Print each dictionary where the show type is "Play"

# answer:
for show in show_data:
    if show.get("Show type") == "Play":
        print(show)


# Problem 2:
# print the opening date of each show
for show in show_data:
    print(show.get("Opening"))

# Problem 3:
# print the title of each show where the year is between 1750 and 1755, inclusive
for show in show_data:
    year = show.get("year")
    if year >= 1750 and year <= 1755:
        print(show.get("title"))

# Problem 4:
# print all show titles and theaters if the show opened in the month of August
for show in show_data:
    if "August" in show.get("Opening", ""):
        print(f"Title: {show.get('title')}, Theaters: {show.get('theaters')}")
# note: we needed to have a default of "" because we can't check if a string is in None


# Problem 5:
# print the show titles and their show id if they have "Other titles"
# if the show doesn't have an other title, print "No Other Titles"
for show in show_data:
    if show.get("Other titles"):
        print(f"Show title: {show.get('title')}, show id: {show.get('show_id')}")
    else:
        print(f"No other titles")


# Problem 6:
# print all theater id numbers for shows that are Original Productions
# hint: all ids are four numbers
for show in show_data:
    theater_id = show.get("theatre_id", "")
    if show.get("Production Type") == "Original Production" and theater_id:
        # print just the number
        print(theater_id[-4:])
    else:
        continue

# example of theater id: "theatre_id": "/shows/theatre.php?theatre_id=5259"
# the continue keyword will skip the current dictionary and move onto the next item in the list