while True:
    action = str(input("What did they do? (choose: insulted, ignored, apologised, praised) ")).lower().strip()
    if action in ["insulted", "ignored", "apologised", "praised"]:
        break

while True:
    like = (input("Did they like your latest post? ")).strip().lower()
    if like in ["yes", "no"]:
        break

while True:
    friend = (input("Are they your real-life friend? ")).strip().lower()
    if friend in ["yes", "no"]:
        break

if action in ["praised", "apologised"]:
    if like == "yes":
        if friend == "yes":
            print("They seem like a true and engaging friend, keep following them!")
        elif friend == "no":
            print("Not a real-life friend but still engaging and nice, keep following them!")
    elif like == "no":
        if friend == "yes":
            print("Maybe they missed your post, let this one slide and keep following them.")
        elif friend == "no":
            print("Unfollow them, they haven't shown you full deserved care and shouldn't gain your trust just yet.")
    else:
        print("Error! I don't understand, please try again.")
else:  # activity = insulted/ignored
    if like == "yes":
        if friend == "yes":
            print("They don't deserve to talk to you like that but they must still care, mute them for now and let them reflect on their actions.")
        elif friend == "no":
            print("Unfollow them, they seem untrustworthy and not fit to be your true companion.")
    elif like == "no":
        if friend == "yes":
            print("They are showing no effort to reflect and change their actions, mute them until they are.")
        elif friend == "no":
            print("Block them! They are proving no commitment or effort to build a loyal relationship and don't deserve all your time and energy.")
