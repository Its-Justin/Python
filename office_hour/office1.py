
# Challenge 1:
# Create a loop that will print *every other* value in a list, starting with the value at index 0, index 2, etc.
# For example (feel free to make up your own lists - use your own variables and values!):
# You should print 8, "Hello", True and -1.5 in this example
random_list = [8, 1, "Hello", "green", True, 4, -1.5]

def my_list(list):
    new_list=[]
    for x in range(0,len(list),2):
        new_list.append(list[x])
    return(new_list)
print(my_list(random_list))




# Challenge 2:
# Write a function that accepts a string as input and returns the number of vowels found in the string.
# For this exercise, "a", "e", "i", "o" and "u" are vowels; we will not count "y" for this challenge.
# If it helps, assume the string is all lower-case for now.  Then try to make it work regardless of if the
# letters are upper- or lower-case.
# For example: given "tommy", return 1 as "o" is a vowel, but "y" is not.  "adrian" should return 3.
person1= "tommy"
person2= "adrian"
def counting_vowels(name):
    counter=0
    for length_name in range(len(name)):
        if name[length_name] == "a":
            counter+=1
        elif name[length_name] == "e":
            counter+=1
        elif name[length_name] == "i":
            counter+=1
        elif name[length_name] == "o":
            counter+=1
        elif name[length_name] == "u":
            counter+=1
    return(counter)
print(counting_vowels(person1))
print(counting_vowels(person2))


# Challenge 3:
# Given a list of dictionaries as input in the format below, return a new list containing only the names.
# Format:
some_variable = [
    {
        "name": "Adrian",
        "favorite_food": "Pizza",
        "favorite_number": 88
    },
    {
        "name": "Jenny",
        "favorite_food": "Sushi",
        "favorite_number": 24
    },
]

def access_dict(human, list):
    new_list=[]
    for dict in list:
        new_list.append(dict[human])
    return(new_list)
print(access_dict("name", some_variable))

# In this example, we should get ["Adrian", "Jenny"] as those are the names found.  Make this work for all lists,
# so please make up your own examples!