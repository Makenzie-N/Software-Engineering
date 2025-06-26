# prac 2.0
START

SET options TO [rock, paper, scissors]

DISPLAY "Choose Rock, Paper, or Scissors:"
INPUT players_choice

SET computer_choice TO pick random from options

IF player_choice = computer_choice THEN
    DISPLAY "IT'S A TIE"

ELSE IF player_choice = rock and computer_choice = scissors THEN
    DISPLAY "You win!"

ELSE IF player_choice = scissors and computer_choice = paper THEN
    DISPLAY "You win!"

ELSE IF player_choice = paper and computer_choice = rock THEN
    DISPLAY "You lose!"

ELSE
    DISPLAY "ERROR :O. Choose again."

END

## prac 2.1
START

SET username TO bob21
SET password TO stop87

DISPLAY "Enter username below."

INPUT username

IF username = bob21 THEN
    DISPLAY "User found."
ELSE
    DISPLAY "Username is incorrect, try again."

DISPLAY "Enter password."

INPUT password

IF password = stop87 THEN
    DISPLAY "Login successful."
ELSE
    DISPLAY "Password is incorrect, try again."

END

### variable challenge

START

SET name TO INPUT("Enter your name:")
SET age TO INPUT("Enter your age:")

DISPLAY "Welcome", name
DISPLAY "You are", age, "years old"

END

#### data types challenge

SET name TO "Kenzie"   ← String
SET score TO 145   ← Integer
SET is_logged_in TO True   ← Boolean
SET height TO 5.6  ← Float
SET colours TO ["Pink", "Blue"]  ← List

##### quick quiz
1. What does == do?
A. States that two things are equal to each other e.g 5 == 5

2. What's the difference between / and //?
A. / is division and // is floor division meaning it rounds the decimal to creat a full number.

3. What is the result of 3 * 2 + 1?
A. 7, because 3 * 2 = 6 then + 1 = 7.

4. How can you check if a number is divisible by 2?
A. Use /= to divide something by 2.

###### prac 3.0
START

SET name TO "Kenzie"
SET age TO 13

DISPLAY "Hello", name
DISPLAY "You are", age, "years old"

END