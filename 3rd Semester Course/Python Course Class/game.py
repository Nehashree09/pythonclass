import random
print("##- Rule for the game:")
print("--> There are five rounds.")
print("--> For every win you get 1 point.")
print("--> Participant wins who has more number of points otherwise tied,")
possible_move=["rock","paper","scissors"]
while(True):
    user_point=0
    computer_point=0
    for i in range(5):
        user_move=input("Enter the choice (rock,paper,scissors): ")
        computer_move=random.choice(possible_move)
        print("You chose: ",user_move)
        print("Computer chose: ",computer_move)
        if user_move == computer_move:
            print("Both players selected ",user_move," get the points")
        elif user_move == "rock":
            if computer_move == "scissors":
                print("Yeah! You get 1 point.")
                user_point=user_point+1
            else:
                print("Computer get 1 point.")
                computer_point=computer_point+1
        elif user_move == "paper":
            if computer_move == "rock":
                print("Yeah! You get 1 point.")
                user_point=user_point+1
            else:
                print("Computer get 1 point.")
                computer_point=computer_point+1
        elif user_move == "scissors":
            if computer_move == "paper":
                print("Yeah! You get 1 point.")
                user_point=user_point+1
            else:
                print("Computer get 1 point.")
                computer_point=computer_point+1
        print("Your score: ",user_point,"|| Computer score: ",computer_point)
    if(user_point==computer_point):
        print("Game tied.")
    elif (user_point>computer_point):
        print("Congratulation! You win!")
    else:
        print("Oww! You lose!")
    choice=input("Do you want to play again(Yes/No): ")
    if(choice=="No" or choice=="NO" or choice=="no"):
        break