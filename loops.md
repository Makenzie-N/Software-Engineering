**PSEUDOCODE**
**for**
`FOR i = 1 TO 5 DO`
`    PRINT "Iteration number " + i`
`END FOR`

**while**
`SET count = 1`
`WHILE count <= 5 DO`
`    PRINT "Iteration number " + count`
`    SET count = count + 1`
`END WHILE`

**WHILE**
`count = 0`
`while count < 5:`
`    print("Count:", count)`
`    count += 1`
`print("Program Ended")`

-----*This loop will run as long as the condition is True*

- while = the function
- count = the variable
- <5 = the condition
- : = semi-colon

**semi-colon**
Indicates the following lines are a process or logic you have to do.

**CONDITIONS OF AN IF STATMENT**

Initialisation: Sets the starting point (i = start).
Condition: The loop continues as long as this condition is true (i <= end).
Iteration: Updates the loop variable after each iteration (i increments by default).

**e.g.**
`for i in range(1, 6):`
`    print(i)`
*Initialisation: The loop starts at 1.*
*Condition: The loop continues until it reaches 5.*
*Iteration: i is automatically updated in each iteration by the range function.*

`fruits = ["apple", "banana", "cherry"]`
`for count in fruits:`
`    print(count)` 

*Initialisation: The variable fruit is initialized with the first element from the list.*
*Condition: The loop continues until all elements in the list have been iterated over.*
*Iteration: fruit is automatically updated to the next element in the list in each iteration.*

###### prac 4
// PseudoCode

start the program
    ground = 0
    maxHeight = 100
    rocketLocation = 0
    
    while rocketLocation <= maxHeight
        output the rocket height
        increase the rocketLocation by one meter
    
    when the rocket has reached maxHeight
        output maxHeight reached
    
    While the rocketLocation > 0
        output "rocket falling"
        decrease the rocketLocation by 1
        output "new loacation"
    
    When rocketLocation = 0
        output "rocket has landed"
end the program