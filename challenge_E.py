#E1
def calculator(first_number, second_number, operation):
    if operation == "add":
        return first_number + second_number
    elif operation == "subtract":
        return first_number - second_number
    else:
        return "Error: Operation not supported"

print(calculator(6, 4, "add")) # should return 10
print(calculator(6, 4, "subtract")) # should return 2
print(calculator(6, 4, "divide")) # should return "Error: Operation not supported"

#E2
def compare_numbers(number1=int, number2=int):
    if number1 > number2:
        return "Number1 is greater."
    elif number1 < number2:
        return "Number2 is greater."
    elif number1 == number2:
        return "Both numbers are equal."
    
print(compare_numbers(8,3)) # should return "Number1 is greater."
print(compare_numbers(2,9)) # should return "Number2 is greater."
print(compare_numbers(4,4)) # should return "Both numbers are equal."