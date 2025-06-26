#activity 1
count = 0
while count < 5:
    print("Count:", count)
    count += 1
print("Program Ended")

count = 0
while count < 2:
    print("Count:", count)
    count += 1
else:
    print("Count:", 10)
    print("Program Ended")

##activity 2
count = 0
while count < 5:
    print("This is loop number", count)
    count += 1
print("Program Ended")

###activity 3
while True:

    question = input("Enter a number: ")
    print("You entered:", question)

    if question.isdigit():
        print("Valid")
        break
    else:
        print("Invalid, try again.")

print("Program Exited")

####activity 4
num = 1
while True:
    print("Number:", num)
    num += 1
    if num > 10:
        break
    print("Didn't break")
print("Finally broke out the loop")

#####activity 5
swiftAlbums=["Taylor Swift","Fearless","Speak Now","Red","1989","Reputation","Lover","TPD"]

print("Taylor Swift Albums:")
for album in swiftAlbums:
    print(swiftAlbums)

albumToCheck = input("Enter an album to check: ")
if albumToCheck in swiftAlbums:
    print(f"{albumToCheck} is in the list")
else:
    print(f"{albumToCheck} is not in the list")

######activity 6
swiftAlbums=["Taylor Swift","Fearless","Speak Now","Red","1989","Reputation","Lover","TPD"]

print("Taylor Swift Albums:")
for album in swiftAlbums:
    print(swiftAlbums)

albumToCheck = input("Enter an album to check: ")
if albumToCheck in swiftAlbums:
    print(f"{albumToCheck} is in the list")
else:
    print(f"{albumToCheck} is not in the list")

while True:
    print("\n"*5)
    albumToCheck = input("Enter an album to check or type 'exit' to quit: ")
    if albumToCheck == "exit":
        break
    if albumToCheck in swiftAlbums:
        print(f"{albumToCheck} is in the list")
    else:
        print(f"{albumToCheck} is not in the list")

