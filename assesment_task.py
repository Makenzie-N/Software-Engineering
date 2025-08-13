# author - your name
# title - your game title
# description - one sentence to explain your game to the player

import os
import colorama
import time
import sys

rooms = ["Abstract Art", "Stunning Sculptures", "Interactive Illusions"]
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

tour_guide = str(input("We have 4 very lovely and keen tour guides available at the moment (Tommy, Reece, Ben and Holly), who would you like to show you around today? "))
if tour_guide in tour_guides:
    print(f"Sounds great! {tour_guide} will be showing you around today. ")
else:
    while tour_guide not in tour_guides:
        str(input(f"Tour guide not an options, please select one from the following 4: Tommy, Reece, Ben, Holly. "))
        for tour_guide in tour_guides:
            print(f"Sounds great! {tour_guide} will be showing you around today. ")
            break
input()
clearScreen()

user_art = input(f"Before we get started we would like to offer you a position in our amazing art compition 'Time for Tales'. If you accept, {tour_guide} will take you there at the end of your session to create and submit your artwork.")













sys.exit()