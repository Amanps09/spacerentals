import random

print("Enter the player 1 name ")
player1 = input()
print('Press 1 to play with computer or 2 - two player games')
x = int(input())
if x == 2:
    print("Enter the player 2 name ")
    player2 = input()
    # player 1's chance
    print("Rock 👊\n")
    print("Paper 🤚\n")
    print("Scissor ✌\n")
    input1 = input()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    input2 = input()
    if input1 == "Rock" or input1 == "rock":
        if input2 == "Paper" or input2 == "paper":
            print(f"{player2} won the game.")
        elif input2 == "Scissor" or input2 == "scissor":
            print(f"{player1} won the game.")
        else:
            print(f"Its a tie.")

    if input1 == "Paper" or input1 == "paper":
        if input2 == "Scissor" or input2 == "scissor":
            print(f"{player2} won the game.")
        elif input2 == "Rock" or input2 == "rock":
            print(f"{player1} won the game.")
        else:
            print(f"Its a tie.")

    if input1 == "Scissor" or input1 == "scissor":
        if input2 == "Rock" or input2 == "rock":
            print(f"{player2} won the game.")

        elif input2 == "Paper" or input2 == "paper":
            print(f"{player1} won the game.")
        else:
            print(f"Its a tie.")

elif x == 1:
    print("Rock 👊\n")
    print("Paper 🤚\n")
    print("Scissor ✌\n")
    input1 = input()
    lists = random.randint(0, 3)
    if lists == 0:
        inputc = 'rock'
    elif lists == 1:
        inputc = 'scissor'
    else:
        inputc = 'paper'

    if input1 == "Rock" or input1 == "rock":
        if inputc == "Paper" or inputc == "paper":
            print(f"Computer won the game.")
        elif inputc == "Scissor" or inputc == "scissor":
            print(f"{player1} won the game.")
        else:
            print(f"Its a tie.")

    if input1 == "Paper" or input1 == "paper":
        if inputc == "Scissor" or inputc == "scissor":
            print(f"Computer won the game.")
        elif inputc == "Rock" or inputc == "rock":
            print(f"{player1} won the game.")
        else:
            print(f"Its a tie.")

    if input1 == "Scissor" or input1 == "scissor":
        if inputc == "Rock" or inputc == "rock":
            print(f"Computer won the game.")

        elif inputc == "Paper" or inputc == "paper":
            print(f"{player1} won the game.")
        else:
            print(f"Its a tie.")

else:
    print(f'Hello {player1} invalid input please try again')
