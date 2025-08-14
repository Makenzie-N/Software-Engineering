name = str(input("What is your name?"))
age = int(input("How old are you?"))
snack = str(input("What snack would you like to bring?"))
game_length = float(input("How many minutes would you like to play?"))
water_play = bool(input("Do you like water play?")).strip().lower()

print("Hi", (name), "! You're", (age), "years old and ready to play in Bluey's backyard. You'll play for", (game_length), "minutes and bring your favourite snack:", (snack), "Water play?", (water_play), "Better bring a towel!")