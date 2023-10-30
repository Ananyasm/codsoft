import random
userpoint=int(0)
comppoint=int(0)
while True:
    
    user = input("Enter a choice (rock, paper, scissors): ")
    possible = ["rock", "paper", "scissors"]
    computer = random.choice(possible)
    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
            userpoint+=1
        else:
            print("Paper covers rock! You lose.")
            comppoint+=1
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
            userpoint+=1
        else:
            print("Scissors cuts paper! You lose.")
            comppoint+=1
    elif user == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
            userpoint+=1
        else:
            print("Rock smashes scissors! You lose.")
            comppoint+=1
    print("Current points of user:",userpoint)
    print("Current points of computer:",comppoint)
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break