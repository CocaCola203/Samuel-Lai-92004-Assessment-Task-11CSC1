#create a score function
score=0
#dictionary function stores quesitons and answers
dictionary1={"Who is the protagonist of the movie ‘The Hobbit’?\n a) Gandalf\n b) Bilbo\n c) Thorin\n d) Smaug\n" : "b", "Where in New Zealand was the ‘shire region of Middle-Earth’ set and now a permanent attraction\n a) Auckland\n b) Matamata\n c) Queenstown\n d) Cape Reinga\n" : "b", "What mythology was ‘The Hobbit’ based on?\n a) Greek\n b) Roman\n c) Old Norse\n d) Japan\n" : "c", "What type of class does Gandalf belong to?\n a) Wizard\n b) Samurai\n c) Knight\n d) Assassin\n" : "a", "Who is the main antagonist of the film ‘The Hobbit’?\n a) Gandalf\n b) Bard\n c) Dwalin\n d) Smaug\n" : "d"}
#Greet the user and ask their name
print("Welcome to the Hobbit quiz!")
name=input("What's your name?\n")
print("Do you want to play this quiz", name,"?")
#beggining of the quiz
play=input("yes or no?\n")
if play=="no":
    exit()
while play=="yes": #Uses a while loop incase the user would like to play again
    print("Okay, let's start!")
#print corresponding questions and checking the user input if their are correct
    for x in dictionary1:
        user=input(x)
        user=user.lower()
        if user==dictionary1[x]:
            print("Correct!")
            score+=1
        else:
            print("Wrong, the correct answer was ",dictionary1[x]) 
    print("That was the end of the quiz! Your final score was",score,"!") #End of quiz, print their score and determine whether they passed or failed
    if int(score) >= 3:
        print("You pass The Hobbit Quiz!")
    if int(score) < 3:
        print("You failed the Hobbit Quiz")
    play=input("Would you want to try The Hobbit Quiz again? (yes or no?)\n") 
    if play=="no":
        print("Thank you for playing")
