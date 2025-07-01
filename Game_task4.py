import random
def game():
    #creating random choice from rock,paper and scissors:
    choices=["Rock","Paper","Scissors"]
    comppick=random.choice(choices)
    #taking the user input for game:
    userch=input("Please enter your choice out of Rock,Paper and Scissors: ")
    #designing the working of the game:
    if userch.lower() == "rock":
        if comppick.lower() == "scissors":
            print("YAY! You win! \nYour choice is: ",userch.upper(),"\n and computer's choice is: ",comppick.upper())
        elif comppick.lower() == "paper":
            print("OOPS! You lost the game! \nYour choice is: ",userch.upper(),"\n and computer's choice is: ",comppick.upper())
        elif comppick.lower() == "rock":
            print("Computer's choice is: ",comppick.upper(),"\n and the User's pick is: ",userch.upper())
            print("It's a tie!")
    elif userch.lower() == "paper":
        if comppick.lower() == "scissors":
            print("OOPS! You lost the game!\n Your choice is: ",userch.upper(),"\n and computer's choice is: ",comppick.upper())
        elif comppick.lower() == "rock":
            print("YAY! You win! \nYour choice is: ",userch.upper(),"\n and computer's choice is: ",comppick.upper())  
        elif comppick.lower() == "paper":
            print("Computer's choice is: ",comppick.upper(),"\n and the User's pick is: ",userch.upper())
            print("It's a tie!")
    elif userch.lower() == "scissors":
        if comppick.lower() == "paper":
                print("YAY! You win! \nYour choice is: ",userch.upper(),"\n and computer's choice is: ",comppick.upper())
        elif comppick.lower() == "rock":
            print("OOPS! You lost the game! \nYour choice is: ",userch.upper(),"\n and computer's choice is: ",comppick.upper())
        elif comppick.lower() == "scissors":
            print("Computer's choice is: ",comppick.upper(),"\n and the User's pick is: ",userch.upper())
            print("It's a tie!")
print("Welcome to the game of Rock,Paper and Scissors!")
game()
while True:
    a=int(input("Kindly press 1 to play again or 2 to exit the game: "))
    if a==1:
        game()
    elif a==2:
        print("Thank you for playing the game!")
        break
    else:
        print("Invalid choice! Please try again!")