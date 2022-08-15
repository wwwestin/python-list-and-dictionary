practice_dict = {
    "name": "Ilana",
    "age": 31,
}

# print all the keys in the dictionary:
for key in practice_dict.keys():
    print(key)
# >>> name
# >>> age



# print all the values in the dictionary:
for value in practice_dict.values():
    print(value)
# >>> Ilana
# >>> 31



# print keys keys and values in the dictionary:
for key, value in practice_dict.items():
    print(key, value)
# >>> name, Ilana
# >>> age, 31



# create a list of all keys and a list of all values in the dict
    # note: this is helpful just to simply see all the keys and values- 
        # the lists are not able to be indexed into, 
        # so generally use this for debugging along the way to building a solution
keys_lst = practice_dict.keys()
# >>> ["name", "age"]

values_lst = practice_dict.values()
# >>> ["Ilana", 31]


### how to key into a dictionary ###

# the ok way- bracket notation:
name = practice_dict["name"]
# >>> Ilana

# the better way- .get()
name = practice_dict.get("name")
# >>> Ilana

# if the key doesn't exist in the dict, returns None by default instead of erroring out
babe = practice_dict.get("favorite_babe") 
# >>> None

# manually set a backup default:
babe = practice_dict.get("favorite_babe", "Pabe") 
# >>> Pabe




### looping over lists of dictionaries ###

office_characters = [
    {
        "first_name": "Michael",
        "last_name": "Scott",
        "position": "Regional Manager"
    },
    {
        "first_name": "Dwight",
        "last_name": "Schrute",
        "position": "Assistant to the Regional Manager"
    },
    {
        "first_name": "Jim",
        "last_name": "Halpert",
        "position": "Assistant Regional Manager"
    }
]

# instead of going straight to keys and values, you will need to loop through each dictionary in the list
# since it's a list of dicts, you can grab a single dict by its index

office_characters[1].get("position") 
# >>> Assitant to the Regional Manager


for character_dict in office_characters:
    print(character_dict.get("first_name"))
# >>> Michael
# >>> Dwight 
# >>> Jim


# add in conditionals
for character_dict in office_characters:
    if "Assistant" in character_dict.get("position"):
        print(character_dict.get("first_name"))
# >>> Dwight
# >>> Jim