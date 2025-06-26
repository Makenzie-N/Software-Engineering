####### prac 3.1
name = input("What is your name?")

health = 100
food = 50
in_cave = True

hours = int(input("How many hours did you wait in the cave?"))

health -= hours * 5
food -= hours * 3

if health <= 50 or food <= 20:
    print("Warning: You are weak!")
else:
    print(name, ", Your health is now", health)
    print("Your food is now", food)

if hours >= 5:
    print("You survived the cave night!")
else:
    print("You left too early and got attacked!")



######## prac 3.2
fruits = ["apple", "banana", "cherry"]
print(fruits)
# Lists use square brackets [ ] and each item is separated by a comma.

# Step 2: Access Items in a List
# Each item has a position (called an index) starting from 0.

print(fruits[0])  # prints "apple"
print(fruits[-1])  # prints "cherry"
# Use negative numbers to count from the end: fruits[-1] prints "cherry".

# Step 3: Change or Add Items
# You can change an item by using its index, or add new items using .append().

fruits[1] = "blueberry"
fruits.append("orange")
print(fruits)

 # Result: ['apple', 'blueberry', 'cherry', 'orange']

# Step 4: Remove Items
# Use .remove() or del to remove items from a list.


fruits.remove("apple")  # removes by name
del fruits[0]           # removes by position
print(fruits)
# Make sure the item exists before removing, or it will cause an error.

# Step 5: Loop Through a List
# Use a for loop to go through each item in the list.

for fruit in fruits:
    print("I like", fruit)
# This is great for printing, checking, or using each item one by one.