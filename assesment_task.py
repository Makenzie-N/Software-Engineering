# author - your name
# title - your game title
# description - one sentence to explain your game to the player

import os
import colorama
import time
import sys

tour_guides = ["Tommy", "Reece", "Ben", "Holly"]
rooms = {"Abstract Art": "Walking into this room, you can see a wide variety of art, all of which you can barely make out the idea of the artwork. Now this, this is abstract art! You hear another tourist announce when they turn to a painting titled 'The Playground'. You are intrigued and hope that this one won't just look paint splattered across the canvas.", 
         "Stunning Sculptures": "As you walk in, you hear a nearby tour guide 'I've always loved sculptures... these ones are all natural, made entirely of leaves, sticks, rocks etc...' you hear him announce.", 
         "Interactive Illusions": "{tour_guide} begins explaining that this room is the only interactive room in the entire museum and therefore the most popular for browsing as well as art competition entries.", 
         "Retro Redos": "This is a new room according to a sign on the door. It says that a young artist came up with the idea when entering in the yearly art competition, she wanted her friend to enter as well but her friend wasn't confident enough so this young artist decide to let her friend copy her own artwork but in a different style and therfore inspired the room 'Retro Redos' for all the interpreted artworks."
        }
paintings = {"Abstract Art": ["The Playground", "Kookakoala", "Graffiti"],
             "Stunning Sculptures": ["Isaac Newton", "Taylor Swift", "Ablbert Einstein", "Mr Smith"],
             "Interactive Illusions": ["Stairway Hooray", "Jolly Jumps", "Dodge the Duck"]
            }
aa_paintings = {"The Playground": "Inspired by the artists favourite childhood playground a slide, monkey bars, swings and a firemans pole are all depicted in this painting.", 
               "Kookakoala": "Kookaburras and Koalas are this artists favourite animals so why not combine them to make a painting which has now become this museums most popular. This artwork eventually ended up as a gift to the artists friend as these 2 animals were her favourite too.", 
               "Graffiti": "This artist had always aspired to be a graffiti artist, he was mesmorized by the freedom and creativity of the works he saw around his hometown. After finally getting there and doing graffiti for 2 years he decided to become a full time artist and so his first piece was this. 'Graffiti' is a summary of a variety of all his graffiti he created over the years."
              }
questions_aa = {"The Playground": "What isn't shown in this artwork?: Monkey bars, swings, a slide, a climbing wall. ", 
                "Kookakoala": "A koala and another animal are combined in this artwork, what is the other animal? ", 
                "Graffiti": "How long did this artist do graffiti before becoming a full time artist? _ years"}
answers_aa = {"The Playground": "a climbing wall", 
              "Kookakoala": "Kookaburra", 
              "Graffiti": "2 years"}


wrong_answers = 0


def clearScreen():
    os.system('cls')

def colourText(text, colour):
    print(colour + text)

def first_room_aa():
    print("The first room today is 'Abstract Art'.")
    abstract_entry = rooms["Abstract Art"]
    print(abstract_entry)

def second_room_ss():
    print("The next room is 'Stunning Sculptures'.")
    sculptures_entry = rooms["Stunning Sculptures"]
    print(sculptures_entry)

def third_room_ii():
    print("This room is 'Interactive Illusions', our most popular!")
    illusions_entry = rooms["Interactive Illusions"]
    print(illusions_entry)

def fourth_room_rr():
    print("This is the last room today, 'Retro Redos'.")
    redos_entry = rooms["Retro Redos"]
    print(redos_entry)
         
def next_move():
    input("Would you like to view another artwork or move to the next room? (type artwork/room) ").lower()
 
def next_move_answer_room1():
    if next_move == "artwork":
        next_artwork = input("Which artwork would you like to view next? (The Playground, Kookakoala, Graffiti) ").lower
    elif next_move == "room":
        second_room_ss()
    else:
        while next_move not in ["artwork", "room"]:
            next_move = input(f"Selected move not an option, please select one of the following options: artwork, room. ")         

def all_art_viewed():
    input 


print("Welcome to the 'Museum of Mastery'!")
time.sleep(1)

clearScreen()

tour_guide = input(f"We have 4 very lovely and keen tour guides available at the moment (Tommy, Reece, Ben, Holly), who would you like to show you around today? ").lower()
if tour_guide in tour_guides:
    print(f"Sounds great! {tour_guide} will be showing you around today.")
else:
        while tour_guide not in tour_guides:
            tour_guide = input(f"Tour guide not an options, please select one from the following 4: Tommy, Reece, Ben, Holly. ").lower()
            if tour_guide in tour_guides:
                print(f"Sounds great! {tour_guide} will be showing you around today.")
                break

time.sleep(0.5)
clearScreen()


name = input(f"Hi, i'm {tour_guide} and I will be your tour guide for today. What is your name? ").lower()
print(f"Nice to meet you {name}!")

time.sleep(0.5)
clearScreen()


print("The first room today is 'Abstract Art'.")
abstract_entry = rooms["Abstract Art"]
print(abstract_entry)

print( )

print(f"You must view at least 1 artwork closely in order to get the full experience. - {tour_guide}")
abstract_paintings = paintings["Abstract Art"]
chosen_artwork = input(f"There are 3 artworks in this room: 'The Playground, Kookakoala, . Which picture would you like to veiw first? ").lower()
time.sleep(0.5)
clearScreen()


if chosen_artwork in abstract_paintings:
    print(chosen_artwork)
    artwork1_aa = aa_paintings[chosen_artwork]
    print(artwork1_aa)
else:
    while chosen_artwork not in abstract_paintings:
        chosen_artwork = input("Chosen artwork not an option, please select one of the following 3: (The Playground, Kookakoala, Graffiti). ").lower()
        if chosen_artwork in abstract_paintings:
            time.sleep(0.5)
            clearScreen()
            print(chosen_artwork)
            artwork1_aa = aa_paintings[chosen_artwork]
            print(artwork1_aa)
            break

input("Press enter to continue...")
clearScreen()

question1_aa = questions_aa[chosen_artwork]
answer1 = input(question1_aa)


correct_answer1 = answers_aa[chosen_artwork]
if answer1 == correct_answer1:
    print("Correct!")
else:
    print("Incorrect!")
    wrong_answers = 1
    answer_chances = 3 - wrong_answers
    print(f"You have gotten {wrong_answers} question wrong, only {answer_chances} more chances before I kick you out. - {tour_guide}")

time.sleep(0.5)
clearScreen()


