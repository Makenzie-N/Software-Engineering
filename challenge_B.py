username = str(input("What is your Minecraft username?"))
woodblocks = int(input("How many wood blocks do you currently have?"))     
weight = float(input("How much does one block weigh (kg)?"))
daytime = bool(input("Is it daytime in the game? (yes/no):"))

print(f"You have {woodblocks}. You need {10 - woodblocks} more.")
while woodblocks <= 10:
 want = int(input("How many more woodblocks would you like to collect?"))
 woodblocks += want
 if woodblocks >= 10:
   print("Collection complete!")
    break   

print(f"Your username is {username}. You have collected {woodblocks}. The total weight of your woodblocks is {weight * woodblocks}kg.")

if daytime:
  print("It is daytime.")
else:
  print("It's night. Watch out for mobs!")
