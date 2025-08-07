rooms = ["Abstract Art", "Stunning Sculptures", "Interactive Illusions"]
paintings = {"Abstract art": ["The Playground", "Kookakoala", "Graffiti"],
             "Stunning Sculptures": ["Isaac Newton", "Taylor Swift", "Ablbert Einstein", "Mr Smith"],
             "Interactive Illusions": ["Stairway Hooray", "Jolly Jumps", "Dodge the Duck"]
}
tour_guides = ["Tommy", "Reece", "Ben", "Holly"]

print("Welcome to the 'Museum of Mastery'!")
tour_guide = str(input(f"We have 4 very lovely and keen tour guides available at the moment {tour_guides}, who would you like to show you around today? "))
if tour_guide in tour_guides:
    print(f"Sounds great! {tour_guide} will be showing you around today.")
else:
    print(f"Tour guide not an options, please select one of the following 4: {tour_guides}")
    
user_art = input(f"Before we get started we would like to offer you a position in our amazing art compition 'Time for Tales', this competition is in the last room of our museum so if you accept {tour_guide} will take you there at the end of your session.")
