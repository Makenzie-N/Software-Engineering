# author - your name
# title - your game title
# description - one sentence to explain your game to the player

import os
import colorama
import time
import sys

rooms = ["Abstract Art", "Stunning Sculptures", "Interactive Illusions", "Retro Redos"]
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

if tour_guide in tour_guides:
    print(f"Sounds great! {tour_guide} will be showing you around today.")
else:
    while tour_guide not in tour_guides:
        tour_guide = str(input(f"Tour guide not an options, please select one from the following 4: Tommy, Reece, Ben, Holly. ")).lower
        if tour_guide in tour_guides:
            print(f"Sounds great! {tour_guide} will be showing you around today. ")
            break