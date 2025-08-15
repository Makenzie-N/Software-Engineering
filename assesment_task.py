# author - your name
# title - your game title
# description - one sentence to explain your game to the player

import os
import colorama
import time
import sys

rooms = {"Abstract Art": "Walking into this room, you can see a wide variety of art, all of which you can barely make out the idea of the artwork. Now this is abstract art! You hear another tourist announce when they turn to a painting titled 'The Playground'. You are intrigued and hope that this one won't just look paint splattered across the canvas.", 
         "Stunning Sculptures": "As you walk in, you here a nearby tour guide 'I've always loved sculptures... these ones are all natural, made entirely of leaves, sticks, rocks etc...' you hear him announce.", 
         "Interactive Illusions": "{tour_guide} begins explaining that this room is the only interactive room in the entire museum and therefore the most popular for browsing as well as art competition entries.", 
         "Retro Redos": "This is a new room according to a sign on the door. It says that a young artist came up with the idea when entering in the yearly art competition, she wanted her friend to enter as well but her friend wasn't confident enough so this young artist decide to let her friend copy her own artwork but in a different style and therfore inspired the room 'Retro Redos' for all the interpreted artworks."
        }
paintings = {"Abstract art": ["The Playground", "Kookakoala", "Graffiti"],
             "Stunning Sculptures": ["Isaac Newton", "Taylor Swift", "Ablbert Einstein", "Mr Smith"],
             "Interactive Illusions": ["Stairway Hooray", "Jolly Jumps", "Dodge the Duck"]
            }
tour_guides = ["Tommy", "Reece", "Ben", "Holly"]


def clearScreen():
    os.system('cls')

def colourText(text, colour):
    print(colour + text)


print("Welcome to the 'Museum of Mastery'!")
input("Press enter to continue... ")

clearScreen()

tour_guide = str(input("We have 4 very lovely and keen tour guides available at the moment (Tommy, Reece, Ben and Holly), who would you like to show you around today? ")).lower
if tour_guide in tour_guides:
    print(f"Sounds great! {tour_guide} will be showing you around today.")
else:
    while tour_guide not in tour_guides:
        tour_guide = str(input(f"Tour guide not an options, please select one from the following 4: Tommy, Reece, Ben, Holly. ")).lower
        if tour_guide in tour_guides:
            print(f"Sounds great! {tour_guide} will be showing you around today.")
            break
input("Press enter to continue... ")
clearScreen()


name = input(f"Hi, i'm {tour_guide} and I will be your tour guide for today. What is your name? ").lower
print(f"Nice to meet you {name}!")

chosen_room = input(f"There are 4 rooms available today: {rooms}. Which room would you like to go to first? ").lower

if chosen_room in rooms:
    print("{chosen_room}")
    room_abstract = rooms["Abstract Art"]
else:
    while tour_guide not in tour_guides:
        tour_guide = str(input(f"Tour guide not an options, please select one from the following 4: Tommy, Reece, Ben, Holly. ")).lower
        if tour_guide in tour_guides:
            print(f"Sounds great! {tour_guide} will be showing you around today. ")
            break
