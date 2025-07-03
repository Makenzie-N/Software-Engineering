# prac 5
mylist = ["apple", "banana", "cherry"]
print(mylist)

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print(thislist[1])
print(thislist[0])
# indexing

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# accessing values between values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# accessing from the beginning to the position

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]
# accessing from the end to the position

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# is the string in the list?

numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("Yes, 3 is in the numbers list")
# is the integer in the list

# Creating a list
fruits = ['apple', 'banana', 'cherry']

# Appending an element
fruits.append('orange') 

# Inserting an element at index 1
fruits.insert(1, 'kiwi') 

# Removing an element by value
fruits.remove('banana')

# Popping an element from the end
last_fruit = fruits.pop()

# Retrieving an element by index
first_fruit = fruits[0]

# Slicing the list
sublist = fruits[0:2]

# Reversing the list
fruits.reverse()

# Sorting the list
fruits.sort()


print(fruits)

## prac 6

no_drinks =[]
drinks = [
    "Water",
    "Orange Juice",
    "Apple Juice",
    "Lemonade",
    "Iced Tea",
    "Coffee",
    "Green Tea",
    "Hot Chocolate",
    "Milk",
    "Cola",
    "Ginger Ale",
    "Energy Drink",
    "Smoothie",
    "Milkshake",
    "Sparkling Water",
    "Herbal Tea",
    "Coconut Water",
    "Mango Lassi",
    "Tomato Juice",
    "Grape Juice"
]

print(drinks)

drinks.remove("Milk")
drinks.remove("Cola")
drinks.append("Jungle Juice")
sublist = drinks[0:4]
no_drinks = ["Mango Lassi", 
             "Tomato Juice",
             "Grape Juice",
             "Jungle Juice"
            ]
print(drinks)
print(no_drinks)
print(len(drinks))

### prac 7
    #challenge 1

myNumbers = []
for i in range (1-4):
  userInput = int(input("Enter number: "))
  myNumbers.append(userInput)
print(myNumbers)
for number in myNumbers:
  print(number)

BEGIN
  DECLARE myNumbers AS LIST OF INTEGER
  FOR i FROM 1 TO 5
    PROMPT "Enter number:"
    READ userInput
    APPEND userInput TO myNumbers
  ENDFOR

  DECLARE sortedAscending AS LIST
  SET sortedAscending TO SORT(myNumbers)

  DECLARE sortedDescending AS LIST
  SET sortedDescending TO SORT(myNumbers) IN REVERSE ORDER

  PRINT "Middle number of the original list:" 
  PRINT myNumbers[2]

  PRINT "Middle number of the sorted ascending list:"
  PRINT sortedAscending[2]

  PRINT "Middle number of the sorted descending list:"
  PRINT sortedDescending[2]
END

myNumbers = []
for i in range (1-5):
  userInput(int(input("Enter number: "))
  myNumbers.append(userInput)
sortedAscending = []
sortedAscending = sorted(myNumbers)

sortedAscending = []
sortedAscending = sorted(myNumbers, reverse = True)
