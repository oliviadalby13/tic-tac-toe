#tic tac toe game
print("The tic-tac-toe rows are labelled A-C and the columns are labelled 1-3")

#need to make empty 3x3 board for tic tac toe using object



#Player 1 Input (O)
moves = []


#Function to check if move already played
def check_move(moves, player_move):
    for position in moves:
      while position == player_move:
          print("This place is taken")
          player_move = input("Please choose another position: ")
    if player_move not in moves:
        moves.append(player_move)
    return moves and player_move

#Player Input
def player_input():
    player_move = input("Where would you like to go? ")
    check_move(moves,player_move)

player_input()
player_input()

#check if won


#Play again function
#def play_again():
    #Need to ask if playing again
    #if no end
    #if yes need to clear board and restart game