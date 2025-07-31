def hello_world(): #defines the function hello_world
    print("Hello world!")

hello_world() #calls function
              #therefore prints "Hello World!"
    

#num1 and num2 are just place holders/parameters
def sum(num1=0, num2=0): #both numbers are automatically 0 if only one (or no) argument is entered below
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2 #returns whichever arguments are inputed e.g if we inoput 2, 3 it should return as 5

total = sum() #if eg "a" is entered python will return "none", if nothing is entered error will appear (would only occur if numbers weren't defined as automatically 0 above)
print(total)


def multiple_items(*args): #args = arguments
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sarah")

def mult_named_items(**kwargs): #kwargs = keyword arguments
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last = "Gray")
