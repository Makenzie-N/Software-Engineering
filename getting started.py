# prac 1

message = "Welcome"
balance = 1

print (message + balance)
print ("Level up.")

balance = 2

print ("Your new level is " + balance)

print(f"Your new level is {balance}")

## prac 2

score = (1-100)

### sequence
print("Hello")
print("Welcome to the program")

#### if + else statements

if score >= 50:
    print("You passed!")
else:
    print("Try again.")

##### loops (while + for)

lives = (1-100)
level = (1-100)

while lives > 0:
    print("Keep playing")
for level in range(1, 4):
    print("Level", level)

###### variables and data types
    
# variables store information
    
# data types include:
# *int ~> numbers ~> eg. 5
# *float ~> numbers with a decimal point/a fractional component ~> eg. 2.25
# *str ~> text ~> eg. "hello"
# *bool ~> true or false
# *list (array) ~> collection of items ~> eg 1,2,3
    
name = "Kenzie"
score = 10
passed = True

####### functions (reusable blocks)

def greet(name):
    print(f"Hello", name)

greet("Kenzie")

######## input and output

# input() lets users type something
# print() shows something on screen

name = input("Kenzie")

print("Hi", name)

######### operations

# logical operations:
# Checking if a user is either an "admin" OR "superuser" to grant access to restricted settings.

# mathematical operations:
# calculating the total price in a shopping cart by multiplying item price with quantity ordered.

# relational operations:
# comparing two product release dates to determine which one is newer.


########## Data vs Information vs Knowledge

# DATA
# Raw, unprocessed facts and figures without context.
# Examples include numbers, dates, and strings of text.

# INFORMATION
# Data that has been processed and organised in a meaningful way. 
# It provides context, relevance, and purpose, enabling decision-making.

# In essence, data becomes information when it is processed and interpreted.

# Example of Data: Imagine you have a list of numbers: 12, 25, 7, and 19. 
# These numbers by themselves don't tell us much.

# Example of Information: Now, if we learn that these numbers are the ages of students in a classroom, that becomes information. 
# This helps us understand more about the classroom and provides something meaningful that we can use to make decisions, like planning activities suitable for that age group.

# KNOWLEDGE
# Knowledge refers to the understanding and awareness gained through experience, education, or research. 
# It allows individuals to comprehend, analyde, and interpret various concepts and situations. 

# 1.Critical Analysis: Evaluating and interpreting information to understand its implications and relevance. 

# 2.Synthesis: Combining different pieces of information to form a comprehensive understanding or new concepts. 

# 3.Refinement: Continuously updating and improving knowledge based on new data, insights, and experiences. 

# 4.Application: Using knowledge to address real-world problems, innovate, and create value.
