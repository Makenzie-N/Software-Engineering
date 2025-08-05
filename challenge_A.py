name = str(input("What is your name? "))
age = int(input("How old are you? "))
snack = str(input("What snack would you like to bring? "))
game_length = float(input("How many minutes would you like to play? "))
water_play = bool(input("You like water play. input true/false. "))

if water_play == "true":
    is_false = False
elif water_play == "false":
    is_false = True
else:
    is_false = False

print(f"Hi {name}! You're {age} years old and ready to play in Bluey's backyard. You'll play for {game_length} minutes and bring your favourite snack: {snack}. You like water play. {is_false}.")

if is_false == True:
    print("Better bring a towel!")
else:
    print("No towel needed.")

games_list = ["Keepy Uppy", "Magic Asparagus", "Shadowlands", "Obstacle Course", "Muffin Cone"]

print(games_list)
print("First game:", games_list[0])
print("Last game:", games_list[-1])

games_list.append("Grannies")
print(games_list)

games_list[1] = "Magic Wand"
print(games_list)
# first item in list is 0

for game in games_list:
    print("Let's play:", game)
