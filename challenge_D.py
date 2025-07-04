weapons = ["Sword", "Axe", "Gun"]
special_attacks = ["Talon Torrent", "Berserker Blast"]

print("Your weapons are: Sword, Axe, Gun. Your special attacks are: Talon Torrent, Berserker Blast.")

wanted_weapon = input("Choose yur weapon: ")
wanted_attack = input("Choose your special attack: ")

print(f"You grip your {wanted_weapon} ready to carve through chaos and trigger a {wanted_attack}.")

userWeapon = input("What weapon would you like to add to your inventory? ")
weapons.append(userWeapon)
userAttack = input("What special attack would you like to add to your inventory? ")
special_attacks.append(userAttack)

removeWeapon = input("What weapon would you like to remove from your inventory?")
weapons.remove(removeWeapon)
removeAttack = input("What special attack would you like to remove from your inventory?")
special_attacks.remove(removeAttack)

print(len(weapons))
print(len(special_attacks))

enemies = ["Maniacal Maya", "Frenzied Felix", "Amok Aria", "Barmy Benjamin"]

print(enemies)

wanted_turns = int(input("How many round would you like to play? "))
current_turn = 1

while current_turn < wanted_turns:
  wanted_enemy = input("Choose your enemy: ")
  wanted_weapon = input("Choose your weapon: ")
  wanted_attack = input("Choose your special attack: ")
  print(f"You point your {wanted_weapon} at {wanted_enemy}'s head and unleash a {wanted_attack}.")
  current_turn += 1
  if current_turn >= wanted turns:
    break
