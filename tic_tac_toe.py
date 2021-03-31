#tic tac toe game
print("The tic-tac-toe rows are labelled A-C and the columns are labelled 1-3")

#need to make empty 3x3 board for tic tac toe using object

board = [A1, A2, A3, B1, B2, B3, C1, C2, C3]

class Players:



class Game:
    if len.moves() == 9



class Board:



#Player 1 Input (O)
moves = []
player_1_moves = []
player_2_moves = []

#Function to check if move already played
def check_move(moves, player_move):
    for position in moves:
      while position == player_move:
          print("This place is taken")
          player_move = input("Please choose another position: ")
    return player_move

#Player Input
def player_input():
    player_move = input("Where would you like to go? ")
    check_move(moves,player_move)
    moves.append(player_move)
    return moves


#check if won
def check_winner(player_1_moves,player_2_moves):
    winning_combinations = ([A1,A2,A3],[B1,B2,B3],[C1,C2,C3],[A1,B1,C1],[A2,B2,C2],[A3,B3,C3],[A1,B2,C3],[C1,B2,A3])
    for individual_combination in winning_combinations:
        if individual_combination in player_1_moves:
            print("Player 1 has won")
        if individual_combination in player_2_moves:
            print("Player 2 has won")
        else:
            print("This game was a draw")

#Play again function
#def play_again():
    #Need to ask if playing again
    #if no end
    #if yes need to clear board and restart game