import tic_tac_toe

def test_check_move():
    test_player_move = "A1"
    moves_list = ["A1"]
    board_positions = ["A1"]
    expected_output = "A1"
    assert tic_tac_toe.check_move(test_player_move, moves_list, board_positions) == expected_output

