print(f"Before we get started we would like to offer you a position in our amazing art compition 'Time for Tales' taking place today.")
art_comp = input("Would you like to partake in this? ").strip().lower()

if art_comp == [True, False]:
    if art_comp == [True]:
        print("Amazing, we'll see you there.")
    elif art_comp == [False]:
        print("Okay, I guess you're not very artsy and that's alright. Maybe next time!")
else:
    while art_comp != [True, False]:
        print("I don't understand, please answer yes/no.")
        art_comp = input("Would you like to partake in 'Time for Tales'? ").strip().lower()
        if art_comp == [True, False]:
            break