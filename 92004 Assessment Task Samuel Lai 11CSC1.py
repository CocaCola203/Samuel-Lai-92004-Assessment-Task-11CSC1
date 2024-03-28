#Any yes answers will be accepted when asking user if they want to play again to create flexibility
yes_answers=["yes","ye","y","ok","sure","k","alright","alr","of course","absolutely"]
#Any no answers will be accepted when asking user if they want to play again to create flexibility
no_answers=["no","n","nah","no thanks"]
#define score function
def score1():
    #Specialised message for individual scores
    if int(score) >= 3: #if score is greater or equal to 3 they pass
        print("You pass The Hobbit Quiz!")
    if int(score) < 3: #if score is less than 3 they fail
        print("You failed the Hobbit Quiz")
    if int(score) == 0: #if they have no answer correct ask the user if they want to watch the movie
        print("You clearly haven't watched the movie")
        url=input("Do you want to watch the movie (y,n)\n")
        while url not in yes_answers and url not in no_answers:
            url=input("Please put in an valid answer\n").lower().strip()
        if url in yes_answers:
            print("https://www.youtube.com/watch?v=SDnYMbYB-nU&ab_channel=WarnerBros.Pictures")
            #if their answer is in no_answer print goodbye to console and exits
        if url in no_answers:
            print("Goodbye")
    if int(score) == 5: #if answer is all correct 
        print("Amazing! You are a Hobbit Master")
#dictionary function stores quesitons and answers
dictionary1={"Who is the protagonist of the movie ‘The Hobbit’?\n a) Gandalf\n b) Bilbo\n c) Thorin\n d) Smaug\n" : "b",
             "Where in New Zealand was the ‘shire region of Middle-Earth’ set and now a permanent attraction\n a) Auckland\n b) Matamata\n c) Queenstown\n d) Cape Reinga\n" : "b",
             "What mythology was ‘The Hobbit’ based on?\n a) Greek\n b) Roman\n c) Old Norse\n d) Japan\n" : "c",
             "What type of class does Gandalf belong to?\n a) Wizard\n b) Samurai\n c) Knight\n d) Assassin\n" : "a",
             "Who is the main antagonist of the film ‘The Hobbit’?\n a) Gandalf\n b) Bard\n c) Dwalin\n d) Smaug\n" : "d"}
#Greet the user and ask their name and ask if they want to pay the quiz
print("Welcome to the Hobbit quiz!")
name=input("What's your name?\n")
print("Do you want to play this quiz", name,"?")
play=input("yes or no?\n").lower().strip()
#if answer of their input is not in any yes_answers or no_answers it would re-question the user 
while play not in no_answers and play not in yes_answers:
    play=input("Please put in an valid answer\n").lower().strip()
#if their answer is no, it would say goodbye to user
if play in no_answers:
    print("Goodbye")
while play in yes_answers: #Uses a while loop incase the user would like to play again
    #beggining of quiz
    #create a score function
    score=0
    print("Okay, let's start!")
#print corresponding questions and checking the user input if their are correct
    #stores list of answers that are only acceptable
    acceptable=["a","b","c","d"]
    for x in dictionary1:
        user=input(x)
        #removes any spaces in between answers and any capitilised answer will be converted to lower case
        user=user.lower().strip()  
        #if their answer is not (a,b,c,d) question is printed again and gives them the opportunity to retry
        while user not in acceptable: #uses a while loop until they type in a valid that is in acceptable list
            if user.isdigit():
                print("Integers can't be used! Try again")
            elif user=="":
                print("Blank space not accepted! Try again")
            elif user not in acceptable:
                print("Invalid answer, please type only a, b, c, d! Try again")
            user=input(x)  
        if user==dictionary1[x]: #if their value is matching the key in the dictionary, 1 score is added to collection and prints correct
            print("Correct!")
            score+=1
        else:
            print("Wrong, the correct answer was ",dictionary1[x]) #if their value was not matching the key in the dictionary, it would state the value for the key(question)
    print("That was the end of the quiz! Your final score was",score,"!") #End of quiz, print their score and determine whether they passed or failed
    score1( )
        #Ask user if they would want to play again
    play=input("Would you want to try The Hobbit Quiz again? (yes or no?)\n").lower().strip()
    if play in no_answers:
        print("Thank you for playing")
    while play not in no_answers and play not in yes_answers: #uses while loop until they put in a valid answer if they want to play again
        play=input("Please put in an valid answer\n").lower().strip() 
