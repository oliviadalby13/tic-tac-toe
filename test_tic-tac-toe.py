import tic_tac_toe

def test_check_move(player_move, moves_list):
    test_player_move = "A1"
    moves_list = ["A1"]
    expected_output = "A2"
    assert check_move(test_player_move) == expected_output