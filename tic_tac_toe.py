#tic tac toe game
print("The tic-tac-toe rows are labelled A-C and the columns are labelled 1-3")

#need to make empty 3x3 board for tic tac toe using object
class Board:
  def __init__(self):
      self.board_positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
      self.board_occupied = {"A1":' ',"A2":' ', "A3": ' ', "B1":' ', "B2":' ', "B3":' ', "C1":' ', "C2":' ', "C3":' '}
  def print_board(self):
      print("\n")
      print("\t {} | {} |  {}".format(self.board_occupied["A1"], self.board_occupied["A2"], self.board_occupied["A3"]))
      print('\t___ ___ ___')
      print("\t {} | {} |  {}".format(self.board_occupied["B1"], self.board_occupied["B2"], self.board_occupied["B3"]))
      print('\t___ ___ ___')
      print("\t {} | {} |  {}".format(self.board_occupied["C1"], self.board_occupied["C2"], self.board_occupied['C3']))
      print("\n")

new_board = Board()
new_board.print_board()

board_positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
board_occupied = {"A1":' ',"A2":' ', "A3": ' ', "B1":' ', "B2":' ', "B3":' ', "C1":' ', "C2":' ', "C3":' '}
moves = []


#Player class 
class Players:
    def __init__(self, player, icon):
        self.player = player
        self.icon = icon
    def move(self):
        print("{} it is your turn, your icon is {}".format(self.player, self.icon))
        player_move = input("{} Where would you like to go? ".format(self.player))
        return player_move

def check_move(player_move, moves_list, positions_list):
    while player_move not in board_positions:
        print("This position does not exist")
        player_move = input("Where would you like to go instead? ")
        if player_move in board_positions:
            break
    while player_move in moves_list:
        print("This position is taken")
        player_move = input("Where would you like to go instead? ")
        if player_move not in moves_list:
            break
    return player_move

#Function to check if won game
def check_winner(board_occupied):
    #board describes what each row, column and diagonal currently looks like in the game
    board = [(board_occupied["A1"], board_occupied["A2"], board_occupied["A3"]),
    (board_occupied["B1"], board_occupied["B2"], board_occupied["B3"]),
    (board_occupied["C1"], board_occupied["C2"], board_occupied["C3"]),
    (board_occupied["A1"], board_occupied["B1"], board_occupied["C1"]),
    (board_occupied["A2"], board_occupied["B2"], board_occupied["C2"]),
    (board_occupied["A3"], board_occupied["B3"], board_occupied["C3"]),
    (board_occupied["A1"], board_occupied["B2"], board_occupied["C3"]),
    (board_occupied["C1"], board_occupied["B2"], board_occupied["A3"])]

    #compares line in board with winning combination to see if either player has won
    for line in board:
        if line == ("X","X","X"):
            print("Player 1 has won!")
            win = True
            if win == True:
                break
        if line == ("O","O","O"):
            print("Player 2 has won!")
            win = True
            if win == True:
                break
        #win condition not satisfied if none of the lines match winning combination
        else:
            win = False
    return win


def print_board(board_occupied):
    print("\n")
    print("\t {} | {} |  {}".format(board_occupied["A1"], board_occupied["A2"], board_occupied["A3"]))
    print('\t___ ___ ___')
    print("\t {} | {} |  {}".format(board_occupied["B1"], board_occupied["B2"], board_occupied["B3"]))
    print('\t___ ___ ___')
    print("\t {} | {} |  {}".format(board_occupied["C1"], board_occupied["C2"], board_occupied['C3']))
    print("\n")


while check_winner(board_occupied) == False:
  player_1 = Players("Player_1", "X").move()
  player_1_checked = check_move(player_1, moves, board_positions)
  moves.append(player_1_checked)
  board_occupied[player_1_checked] = 'X'
  print_board(board_occupied)

  if check_winner(board_occupied) == True:
      break
  else:
    player_2 = Players("Player_2", "O").move()
    player_2_checked = check_move(player_2, moves, board_positions)
    moves.append(player_2_checked)
    board_occupied[player_2_checked] = 'O'
    print_board(board_occupied)

  if len(moves) == 8:
      if check_winner(board_occupied) == False:
          print("It is a draw")
      break




#class Game:
   # def __init__(self, player, moves, board):




#Play again function
#def play_again():
    #Need to ask if playing again
    #if no end
    #if yes need to clear board and restart game