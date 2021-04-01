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
player_1_moves = []
player_2_moves = []

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

def check_winner(player_1_moves,player_2_moves):
    winning_combinations = (["A1","A2","A3"],["B1","B2","B3"],["C1","C2","C3"],["A1","B1","C1"],["A2","B2","C2"],["A3","B3","C3"],["A1","B2","C3"],["C1","B2","A3"])
    for individual_combination in winning_combinations:
        if individual_combination in player_1_moves:
            print("Player 1 has won")
        if individual_combination in player_2_moves:
            print("Player 2 has won")
        else:
            print("This game was a draw")

def print_board(board_occupied):
    print("\n")
    print("\t {} | {} |  {}".format(board_occupied["A1"], board_occupied["A2"], board_occupied["A3"]))
    print('\t___ ___ ___')
    print("\t {} | {} |  {}".format(board_occupied["B1"], board_occupied["B2"], board_occupied["B3"]))
    print('\t___ ___ ___')
    print("\t {} | {} |  {}".format(board_occupied["C1"], board_occupied["C2"], board_occupied['C3']))
    print("\n")


while len(moves) < 9:
  player_1 = Players("Player_1", "X").move()
  player_1_checked = check_move(player_1, moves, board_positions)
  moves.append(player_1_checked)
  player_1_moves.append(player_1_checked)
  board_occupied[player_1_checked] = 'X'
  print_board(board_occupied)

  if len(moves) == 9:
      check_winner(player_1_moves,player_2_moves)
      break

  player_2 = Players("Player_2", "O").move()
  player_2_checked = check_move(player_2, moves, board_positions)
  moves.append(player_2_checked)
  player_2_moves.append(player_2_checked)
  board_occupied[player_2_checked] = 'O'
  print_board(board_occupied)


#class Game:
   # def __init__(self, player, moves, board):


#check if won


#Play again function
#def play_again():
    #Need to ask if playing again
    #if no end
    #if yes need to clear board and restart game