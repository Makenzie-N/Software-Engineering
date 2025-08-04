# FUNCTION PARAMETERS
*PARAMETERS LET YOU PASS VALUES INTO A FUNCTION*
`def greet(name):`
`    print(f"Hello, {name}!")`

`greet("Anna")` # prints "Hello!"

## DEFAULT PARAMETERS
*PARAMETERS CAN HAVE DEFAULT VALUES, USED WHEN NO ARGUEMENT IS PROVIDED*
`def greet(name="friend"):`
`    print(f"Hello, {name}!")`

`greet()`          # prints Hello, friend!
`greet("Alice")`   # prints Hello, Alice!

### RETURN VALUES
*FUNCTIONS CAN RETURN A VALUE USING THE RETURN KEYWORD*
`def add(x, y):`
`    return x + y`

`result = greet("Bob")`  # Hello, Bob!

#### MULTIPLE PARAMETERS
*FUNCTIONS CAN ACCEPT MULTIPLE PARAMETERS*
`def add(a, b):`
`    return a + b`

`result = add(3, 5)`
`print(result)`   # prints 8

##### RETURN STATEMENTS
*RETURN IS USED TO PASS BACK A VALUE FROM THE FUNCTION*
`def square(number):`
`    return number * number`

`answer = square(4)`
`print(answer)`    # prints 16

###### VOID vs VALUE-RETURNING FUNCTIONS
*VOID FUNCTIONS PERFORM AN ACTION BUT RETURN NO VALUE*
`def say_hi():`
`    print("Hi there!")`

*VALUE-RETURNING FUNCTIONS PERFORM AN ACTION AND RETURN A VALUE*
`def multiply(x, y):`
`    return x * y`

###### # LOCAL vs GLOBAL VARIABLES
*VARIABLES CREATED INSIDE FUNCTIONS ARE LOCAL*
*VARIABLES CREATED OUTSIDE FUNCTIONS ARE GLOBAL*
`x = 10`  # global

`def my_function():`
`    x = 20`  # local variable
`    print(x)`

`my_variable = 100`
`print(my_variable)`  # prints 100 (global)

###### ## USING FUNCTIONS IN LOOPS
*YOU CAN REPEATEDLY CALL FUNCTIONS WITHIN LOOPS*
`def shout(word):`
`    print(word.upper())`

`words = ["hello", "world", "python"]`
`for w in words:`
`    shout(w)`
. # prints:
. # HELLO
. # WORLD
. # PYTHON

###### ### BUILT-IN PYTHON FUNCTIONS
*PYTHON PROVIDES BUILT IN FUNCTIONS SUCH AS LEN(), PRINT(), TYPE()*
name = "Python"
length = len(name)
print(length)  # prints 6

###### #### FUNCTION DOCUMENTATION (DOCSTRINGS)
*DOCSTRINGS ARE USED TO EXPLAIN WHAT YOUR FUNCTION DOES*
`def multiply(a, b):`
`    """Returns the product of two numbers."""`
`    return a * b`

help(multiply)  # displays the docstring

###### ##### A def function in Python is structured as follows:

Keyword: The function definition starts with the def keyword.

Function Name: Followed by the name of the function which should be descriptive.

Parameters: Enclosed in parentheses (), parameters are optional inputs to the function.

Colon: Ends the function header with a colon :.

Docstring: An optional description of the function in a string format.

Body: Indented block of code that performs the function’s task.

Return Statement: Optionally returns a value using the return keyword.

`Example:`
`def function_name(parameters):`
`    """Docstring describing the function."""`
`    # function body`
`    return result`


