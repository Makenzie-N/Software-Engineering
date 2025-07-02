# pseudocode
*a way to plan your program before you write real code (like writing instructions in plain english using code-like logic)*
*describes what the program should do, what steps to follow, and what logic or decisions are involved*

**why use pseudocode?**
- It helps you think through the logic before you write code
- It’s easier to understand than real code
- It’s not tied to any specific programming language
- It helps teams communicate ideas clearly

**PSEUDOCODE BUILDING BLOCKS**
1. start and end (every program has a start and end)
`START`
`...`
`END`
2. variables (use set to create and store values)
`SET score TO 0`
3. input and output (use input to get info, and display to show info)
`INPUT name`
    `DISPLAY "Welcome", name`
4. decision making (IF statements)
`IF score >= 50 THEN`
    `DISPLAY "You passed!"`
`ELSE`
    `DISPLAY "Try again"`
`ENDIF`
5. loops (WHILE/FOR)
`WHILE lives > 0 DO`
    `DISPLAY "Keep playing"`
    `SUBTRACT 1 FROM lives`
`ENDWHILE`
6. function or procedures
`PROCEDURE greetUser`
    `DISPLAY "Hello!"`
`ENDPROCEDURE`

**PSEUDOCODE vs REAL CODE**
*psuedocode*         *python code*
SET count TO 10       count = 10
IF age >= 18 THEN     if age >= 18:
DISPLAY "Welcome!"    print("Welcome!")
FOR i FROM 1 TO 5 DO  for i in range(1, 6):

**EXAMPLE OF PSEUDOCODE**
`BEGIN`
   `SET total to 0`
   `FOR each item in list`
       `ADD item to total`
   `ENDFOR`
   `PRINT total`
`END`

*BEGIN/END: Used to denote the start and end of the pseudocode process.*
*IF/THEN/ELSE/ENDIF: Represents conditional logic.*
*FOR/ENDFOR: Indicates the beginning and end of a loop structure.*
*SET: Assigns a value to a variable.*
*ADD: Typically used to add values or items.*
*PRINT: Outputs information or results.*

**ALGORITHMS**
- Step by step instuctions for solving a problem or completing a  task
- Can be written as pseudocode, as a flowchart or in plain English
- Help computers do things in the right order
- Help computers make desicions
- Help computers repeat actions
- Help computers solve problems efficiently

**EXAMPLE OF AN ALGORITHM**
`START`
    `Put bread in toaster`
    `Push down toaster lever`
    `Wait until toast pops up`
    `Take toast out`
    `Spread butter`
`END`

**VARIABLES**
- Used to store data (is like a name pointing to a value)
- Can be reference/manipulated later
- Created when a value is assigned to them using = (the assignment operator)
- Like a container (you can put something in, change it or read what's inside + use it multiple times)

`name = "Liam"`
`score = 25`
`is_logged_in = True`

*name stores a string ("Liam"), score stores a number (25), is_logged_in stores a boolean (True or False)*

**DATA TYPES**
- Tell the computer the type of information it's dealing with
- All variables have a type (eg. numbers, text)
- They help the computer understand how to handle the value
- You can’t add a number to a word — the types must make sense
- Different types allow for different actions (e.g. looping through a list vs doing math)

**common/primative data types**
*Type              Description                              Example*

`String            A piece of text (in quotes)              "hello", "123"`

`Integer           A whole number                           7, 100, -1`

`Float             A number with a decimal                  3.14, 0.5`

`Boolean           A true or false value                    True, False`

`List              A group of values                        ["dog", "cat"]`

**FUNCTIONS**

**print() function**
- takes info from () and displays it
- "talks back" to the user
- adds a new line at the end by default

*can be used to print the following*
1. Strings
`print("Welcome to the game!")`

2. Numbers
`print(42)`
`print(3.14)`

3. Variables
`name = "Bluey"`
`print(name)`

4. Multiple Things
`name = "Bingo"`
`age = 6`
`print(name, "is", age, "years old.")`

5. Formatted Text
`print(f"Score is {score}")`

6. Print without new line
`print("Hello", end=" ")`
`print("world!")`
# ➜ Hello world!

**note that print("name") prints the word "name" + print(name) prints the value in name*

**input() function**
- gathers info while program is running
- pauses the program, waits for input, then stores it in a variable

e.g.
`name = input("What is your name?")`
- "What is your name?" = the prompt
- Whatever the user types gets stored in the variable name
- The input is always saved as a string, even if the user types a number

e.g. storing it as a number
`age = int(input("How old are you?"))`
# ➜ Converts to integer
`height = float(input("Your height in m?"))`
# ➜ Converts to decimal (float)

**PROCESSING DATA**

**types of operator**
*1. ARITHMETIC OPERATORS*
Operator    Meaning             Example   Result
`+          Addition            3 + 2     5`
`-          Subtraction         5 - 1     4`
`*          Multiplication      4 * 2     8`
`/          Division            8 / 2     4.0`
`//         Floor division      9 // 2    4`
`%          Modulo (remainder)  9 % 2     1`
`**         Exponent            2 ** 3    8`

*2. ASSIGNMENT OPERATORS*
Operator    Example   Meaning
`=          x = 5     Assigns 5 to x`
`+=         x += 1    Adds 1 to x (x = x + 1)`
`-=         x -= 2    Subtracts 2 from x`
`*=         x *= 3    Multiplies x by 3`
`/=         x /= 2    Divides x by 2`

*3. COMPARISON OPERATORS*
Operator    Meaning                Example   Result
`==         Equal to               5 == 5    True`
`!=         Not equal to           5 != 3    True`
`>          Greater than           6 > 4     True`
`<          Less than              2 < 8     True`
`>=         Greater than or equal  5 >= 5    True`
`<=         Less than or equal     3 <= 4    True`

*4. LOGICAL OPERATORS*
Operator    Description                       Example
`and        Both conditions must be true      x > 3 and x < 10`
`or         At least one must be true         x < 3 or x > 10`
`not        Reverses the condition (negates)  not(x == 5) is True if x != 5`

*5. STRING OPERATORS*

- String joining
greeting = "Hello" + " " + "World"
print(greeting) 
# ➜ Hello World

- String repetition
laugh = "ha" * 3
print(laugh)  
# ➜ hahaha

**CREATING A LIST**

**integers**
`numbers = [1, 2, 3, 4, 5]`

**string**
`fruits = ["apple", "banana", "cherry"]`

**different data types**
`mixed_list = [1, "text", 3.14, True]`

**USING A BOOLEAN**
    if processed_response == 'false':
        is_false = False
    elif processed_response == 'true':
        is_false = True
    else:
        # Handle invalid input, e.g., assign a default or raise an error
        print("Invalid input. Assuming False.")
        is_false = False 



name = str(input("What is your name?"))
age = int(input("How old are you?"))
snack = str(input("What snack would you like to bring?"))
game_length = float(input("How many minutes would you like to play?"))
water_play = bool(input("Do you like water play?"))

print("Hi", (name), "! You're", (age), "years old and ready to play in Bluey's backyard. You'll play for", (game_length), "minutes and bring your favourite snack:", (snack), "Water play?", (water_play), "Better bring a towel!")