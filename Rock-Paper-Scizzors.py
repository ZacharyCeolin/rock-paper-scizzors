import random

choices =["Rock", "Paper", "Scizzors"]
computer = 0
user = 0
game =0 

while computer < 3 and user < 3 and game < 1:

    userchoice= input("Choose Rock, Paper, or Scizzors:")

    if userchoice.lower() != "rock" and userchoice.lower() != "paper" and userchoice != "scizzors":
        print("Invalid Input. Please choose Rock, Paper, or Scizzors")
    else:
        num= random.randint(0, 2)
        computchoice = choices[num]

    if userchoice.lower() == "rock":
        if computchoice.lower() == "rock":
            print("Computer chose Rock. Tie Game.")
            print(f"Score Computer: {computer} User: {user}")
        elif computchoice.lower() == "paper":
            print("Computer chose Paper. Computer Wins!")
            computer += 1
            print(f"Score Computer: {computer} User: {user}")
        else:
            print("Computer chose Scizzors.User Wins!")
            user += 1
            print(f"Score Computer: {computer} User: {user}")
    elif userchoice.lower() == "paper":
        if computchoice.lower() == "paper":
            print("Computer chose Paper. Tie Game")
            print(f"Score Computer: {computer} User: {user}")

        elif computchoice.lower() == "scizzors":
            print("Computer chose Scizzors. Computer Wins!")
            computer += 1
            print(f"Score Computer: {computer} User: {user}")

        else:
            print("Computer chose Rock. User Wins!")
            user += 1
            print(f"Score Computer: {computer} User: {user}")

    elif userchoice.lower() == "scizzors":
        if computchoice.lower() == "scizzors":
            print("Computer chose Scizzors. Tie Game")
            print(f"Score Computer: {computer} User: {user}")
    
        elif computchoice.lower() == "rock":
            print("Computer chose Rock. Computer Wins!")
            computer += 1
            print(f"Score Computer: {computer} User: {user}")

        else:
            print("Computer chose Paper. User Wins!")
            user += 1
            print(f"Score Computer: {computer} User: {user}")

    if user != 3 and computer != 3:
        end = input("Continue Playing? yes/no")
        if end.lower() != "yes" and end.lower() != "no":
            print("Invalid Entry. Please choose yes or no")
        elif end.lower() == "no":
            print(f"Game Over. Final score Computer: {computer} User: {user}")
            computer = 0
            user = 0
            game = 1

if game == 0:
    if user == 3:
        print(f"Congratulations, you win! Final score Computer: {computer} User: {user}")
        computer = 0
        user = 0
    elif computer == 3:
        print(f"Womp womp, you lost. Final score Computer: {computer} User: {user}")
        computer = 0
        user = 0