#PRAC 9
# Creating a simple key-value pair in a dictionary
person = {
    "name": "Alice",
    "status": "active",
    "age": "28"
}

# Accessing the value using its key
dictName = person["name"]
print("The name is:", dictName)

age = person["age"]
print(dictName,"is", age, "years old.")



###
simple_dict = {
    "name": "John", # value can be a string
    "age": 30, # or an integer
    "city": "New York",
    "time": 12.30, # or a float
    "fave_colours": ["red", "blue", "green"] # or a list
}



#SIMPLE DICTIONARY USE
import os

# Create a simple dictionary example
simple_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

os.system('cls')  # on Windows System

for key, value in simple_dict.items():
    print(key, value)

if "name" in simple_dict:
    print(f"Name: {simple_dict['name']}")
else:
    print("Name not found")

if "surname" in simple_dict:
    print(f"Surname: {simple_dict['surname']}")
else:
    print("Surname not found")

query=input("what do you want to search for?")
if query in simple_dict:
    print(f"Found {query} in the dictionary. Here are the results:")
    for key, query in simple_dict.items():
        print(key, query)
    print("let's print all the **values** one by one")
    for key, value in simple_dict.items():
        print(value)
    print("let's print all the **keys** one by one")
    for key, value in simple_dict.items():
        print(key)
else:
    print(f"Could not find {query} in the dictionary")



#NESTED DICTIONARY
student_info = {
    'John': {
        'age': 22,
        'major': 'Mathematics'
    },
    'Alice': {
        'age': 24,
        'major': 'Physics'
    }
}
    
age_of_john = student_info['John']['age']



#CHALLENGES
#1
characters = {
    "dc": {
        "name": "Diana Prince",
        "alias": "Wonder Woman",
        "team": "Justice League"
    },
    "marvel": {
        "name": "Carol Danvers",
        "alias": "Captain Marvel",
        "team": "Avengers"
    },
    "2000ad": {
        "name": "Cassandra Anderson",
        "alias": "Judge Anderson",
        "team": "Justice Department"
    }
}

dc_team = characters['dc']['team']
print(dc_team)

# to be continued...