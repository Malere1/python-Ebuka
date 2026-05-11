# Step 1: Start
# Step 2: Ask Player 1 to enter rock, paper, or scissors
# Step 3: Ask Player 2 to enter rock, paper, or scissors
# Step 4: Check if both players entered the same choice
# Step 5: If yes, print "Tie"
# Step 6: Otherwise, check Player 1's choice
# Step 7: If Player 1 chose rock:
#         - If Player 2 chose scissors, Player 1 wins
#         - Else, Player 2 wins
# Step 8: If Player 1 chose paper:
#         - If Player 2 chose rock, Player 1 wins
#         - Else, Player 2 wins
# Step 9: Else (Player 1 chose scissors):
#         - If Player 2 chose paper, Player 1 wins
#         - Else, Player 2 wins
# Step 10: End

player1 = input("Player 1 (rock/paper/scissors): ")
player2 = input("Player 2 (rock/paper/scissors): ")

if player1 == player2:
    print("Tie")
else:
    if player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    else:
        if player2 == "paper":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
