import json

shows = open('shows-data.json')

show_data = json.load(shows)

# Problem 1:
# Print each dictionary where the show type is "Play"

for k in show_data:
    if k.get("Show type") == "Play":
	    print (k)

# Problem 2:
# print the opening date of each show

for k in show_data:
	print (k.get("Opening"))

# Problem 3:
# print the title of each show where the year is between 1750 and 1755, inclusive

for k in show_data:
    if 1750 <= k.get("year") <= 1755:
	    print (k.get("title"))

# Problem 4:
# print all show titles and theaters if the show opened in the month of August

for k in show_data:
   if "August" in k.get("Opening", ""):
        print (f"Title: {k.get('title')}, Theaters: {k.get('Theatres')}")
	    
# Problem 5:
# print the show titles and their show id if they have "Other titles"
# if the show doesn't have an other title, print "No Other Titles"

for k in show_data:
    if k.get("Other titles") == None:
        print ("No Other Titles")
    else:
        print (f"Title: {k.get('title')}, AKA: {k.get('Other titles')}")


# Problem 6:
# print all theater ids for shows that are Original Productions
# hint: all ids are four numbers 

# for k in show_data:
#     theater_id = k.get("theatre_id", "")
   
#     if k.get("Production Type") == "Original Production" and theater_id:
#         print (theater_id[-4:])
#     else:
#         continue