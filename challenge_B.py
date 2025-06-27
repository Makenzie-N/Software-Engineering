username = str(input("What is your Minecraft username?"))
woodblocks = int(input("How many wood blocks do you have?"))     
weight = float(input("How heavy is each block? (in kg's)"))
daytime = bool(input("Is it daytime?"))

while woodblocks <= 10:
collect = int(input("How many more woodblocks would you like to collect?"))
  woodblocks = woodblocks + 1
if woodblocks >= 10
break

print(f"Your username is {username}. You have collected {woodblocks}. The total weight of your woodblocks is {weight * woodblocks}kg.")

if daytime = yes:
  print("It is daytime, therfore it is safe to build.")
else:
  print("It is nighttime, therefore it is not safe to build.")
