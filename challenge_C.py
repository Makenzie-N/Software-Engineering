while True:
        action = (input("What did they do? (choose: insult, ignored, apologised, praised) ")).lower().strip()
        if action in ["insult", "ignored", "apologised", "praised"]:
                like = (input("Did they like your latest post? ")).lower().strip()
                if like in ["yes", "no"]:
                        friend = (input("Are they your real-life friend? ")).lower().strip()
                        if friend in ["yes", "no"]:
                                break

if like == 'yes':
        like_good = True
elif like == 'no':
        like_good = False
else:
        like_good = False

if friend == 'yes':
        friend_good = True
elif friend == 'no':
        friend_good = False
else:
        friend_good = False

if action in ["apologised", "praised"]:
    action_good = True
elif action in ["insult", "ignored"]:
    action_good = False
else:
    action_good = False

if like_good == True + friend_good == True + action_good == True:
       print("They seem like a good friend, keep following them!")
elif like_good == False + friend_good == True + action_good == True:
       print("They most likely missed your post, keep following them!")
elif like_good == True + friend_good == False + action_good == True:
       print("Their not a real-life friend, probably best to unfollow them.")
elif like_good == True + friend_good == True + action_good == False:
       print("Let them think about their actions, mute them for now.")
elif like_good == False + friend_good == False + action_good == True:
       print("Unfollow, what are they praising or apologising for if they aren't even a real life friend?")
elif like_good == False + friend_good == True + action_good == False:
       print("Mute them, it seems like somethings up and you should give them time to reflect on that.")
elif like_good == True + friend_good == False + action_good == False:
        print("Block! They aren't a real-life friend and don't seem to have a set opinion on you.")
elif like_good == False + friend_good == False + action_good == False:
        print(Block! No one talks to you like that, especially someone who isn't a real-life friend.")
else:
        print("Incorrect input, I don't understand. Please try again.")
