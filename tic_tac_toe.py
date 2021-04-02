#tic tac toe game
print("The tic-tac-toe rows are labelled A-C and the columns are labelled 1-3")

#need to make empty 3x3 board for tic tac toe using object
class Board:
  def __init__(self,board_occupied):
      self.board_positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
      self.board_occupied = board_occupied
  def print_board(self):
      print("\n")
      print("\t {} | {} |  {}".format(self.board_occupied["A1"], self.board_occupied["A2"], self.board_occupied["A3"]))
      print('\t___ ___ ___')
      print("\t {} | {} |  {}".format(self.board_occupied["B1"], self.board_occupied["B2"], self.board_occupied["B3"]))
      print('\t___ ___ ___')
      print("\t {} | {} |  {}".format(self.board_occupied["C1"], self.board_occupied["C2"], self.board_occupied['C3']))
      print("\n")
  def check_winning_board(self):
      #board describes what each row, column and diagonal currently looks like in the game
      board = [(self.board_occupied["A1"], self.board_occupied["A2"], self.board_occupied["A3"]),
      (self.board_occupied["B1"], self.board_occupied["B2"], self.board_occupied["B3"]),
      (self.board_occupied["C1"], self.board_occupied["C2"], self.board_occupied["C3"]),
      (self.board_occupied["A1"], self.board_occupied["B1"], self.board_occupied["C1"]),
      (self.board_occupied["A2"], self.board_occupied["B2"], self.board_occupied["C2"]),
      (self.board_occupied["A3"], self.board_occupied["B3"], self.board_occupied["C3"]),
      (self.board_occupied["A1"], self.board_occupied["B2"], self.board_occupied["C3"]),
      (self.board_occupied["C1"], self.board_occupied["B2"], self.board_occupied["A3"])]

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

#Player class 
class Players:
    def __init__(self, player, icon):
        self.player = player
        self.icon = icon
    def move(self):
        print("{} it is your turn, your icon is {}".format(self.player, self.icon))
        player_move = str(input("{} Where would you like to go? ".format(self.player)))
        return player_move.upper()

def check_move(player_move, moves_list, board_positions):
    while player_move.upper() not in board_positions:
        print("This position does not exist")
        player_move = input("Where would you like to go instead? ")
        if player_move.upper() in board_positions:
            break
    while player_move in moves_list:
        print("This position is taken")
        player_move = input("Where would you like to go instead? ")
        if player_move.upper() not in moves_list:
            break
    return player_move.upper()


#Defining valid positions of board
board_positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
#Defining 
moves = []

def start_game():
    #Defining empty board
  board_occupied = {"A1":' ',"A2":' ', "A3": ' ', "B1":' ', "B2":' ', "B3":' ', "C1":' ', "C2":' ', "C3":' '}
  #Printing empty board
  Board(board_occupied).print_board()
  return board_occupied

#tic-tac-toe game

board_occupied = start_game()

def tic_tac_toe_game(board_occupied, board_positions, moves):
  while Board(board_occupied).check_winning_board() == False:
    player_1 = Players("Player_1", "X").move()
    player_1_checked = check_move(player_1, moves, board_positions)
    moves.append(player_1_checked)
    board_occupied[player_1_checked] = 'X'
    Board(board_occupied).print_board()

    if Board(board_occupied).check_winning_board() == True:
        play_again(board_positions)
        break

    else:
      player_2 = Players("Player_2", "O").move()
      player_2_checked = check_move(player_2, moves, board_positions)
      moves.append(player_2_checked)
      board_occupied[player_2_checked] = 'O'
      Board(board_occupied).print_board()
      if Board(board_occupied).check_winning_board() == True:
        play_again(board_positions)

    if len(moves) == 9:
        if Board(board_occupied).check_winning_board() == False:
            print("It is a draw")
            play_again(board_positions)
        break

#Play again function
def play_again(board_positions):
    #Need to ask if playing again
    replay = input("Would you like to play again? Yes or No?")
    if replay.upper() == "YES":
        board_occupied = start_game()
        moves = []
        tic_tac_toe_game(board_occupied, board_positions, moves)


tic_tac_toe_game(board_occupied, board_positions, moves)