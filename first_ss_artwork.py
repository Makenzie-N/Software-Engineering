if ss == 1:
    next_ss_artwork = input(f"Which artwork would you like to view next? {Stunning_Sculptures} ")
    if next_ss_artwork in [Stunning_Sculptures]:
        artwork1ss = Stunning_Sculptures(next_ss_artwork)
        print(artwork1ss)
        painting1ss = ss_paintings(next_ss_artwork)
        print(painting1ss)
        input("Press enter to continue... ")
        clearScreen
        question1ss = questions_ss(next_ss_artwork)
        answer1ss = input(question1ss)
        trueanswer1ss = answers_ss(next_ss_artwork)
        if answer1ss == trueanswer1ss:
            print("Correct!")
        
