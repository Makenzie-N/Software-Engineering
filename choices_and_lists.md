**RECOGNISABLE OPERATIONS**
- Equals: a == b
- Not Equals: a != b
- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b

**CONDITIONAL STATEMENTS**
**i, eli and else are the primary conditional statements**
`x = 10`
`if x > 0:`
`    print("Positive")`
`elif x == 0:`
`    print("Zero")`
`else:`
`    print("Negative")`
*In this example, the if statement checks if x is greater than 0. If this condition is true, it executes the code within that block. If x is not greater than 0, the elif statement checks if x is equal to 0. If not, the else statement executes, indicating that x is negative. Conditional statements are fundamental for controlling the flow of a program.*

**BRO_CODE**

**LISTS**
*🧠 Remember: Indexes start at 0, not 1.*

# Add to end of list
`fruits.append("kiwi")`

# Remove an item
`fruits.remove("apple")`

**looping through a list**
`for fruit in fruits:`
`    print("I like", fruit)`

**length of a list**
`print(len(fruits))`  
*displays the number of items in the list*

**MINI QUIZ**
What index is the first item in a list?
0
How do you add something to a list?
.append
What does len(my_list) return?
it gets the program to display the length of the list/the number of items in the list
Can a list store both numbers and strings?
yes, a list can store both numbers and strings



Lists in programming provide a versatile data structure that supports various operations for data manipulation. Common operations include appending elements using the append() method, inserting elements at specific positions with insert(), and removing elements using remove() or pop(). Lists can be concatenated using the + operator or extended with extend(). Additionally, you can retrieve elements by index, slice lists for sublists, and reverse the order using reverse(). Sorting operations are also available through the sort() method. These operations make lists a powerful tool for handling collections of data efficiently.

# Create an array of 5 numbers
numbers = [32, 14, 7, 25, 19]

# Create a new array to hold numbers in ascending order
ascending_numbers = sorted(numbers)

# Create a new array to hold numbers in descending order
descending_numbers = sorted(numbers, reverse=True)

print("Original numbers:", numbers)
print("Ascending order:", ascending_numbers)
print("Descending order:", descending_numbers)
