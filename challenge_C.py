action = str(input("What did they do? (choose: insult, ignored, apologised, praised)"))
like = bool(input("Did they like your latest post?"))
friend = bool(input("Are they your real-life friend?"))

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
       print("Unfollow, what are they praising or apologising for?")
elif like_good == False + friend_good == True + action_good == False:
       print("Mute, ")