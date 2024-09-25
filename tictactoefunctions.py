
def print_board(actual_board_state):
    
    print(f"{actual_board_state[0]}|{actual_board_state[1]}|{actual_board_state[2]}\n-----\n{actual_board_state[3]}|{actual_board_state[4]}|{actual_board_state[5]}\n-----\n{actual_board_state[6]}|{actual_board_state[7]}|{actual_board_state[8]}")

    

def check_player_win(abs, mark):
    
    if (abs[0] == mark and abs[1] == mark and abs[2] == mark):
        return True
    if (abs[3] == mark and abs[4] == mark and abs[5] == mark):
        return True
    if (abs[6] == mark and abs[7] == mark and abs[8] == mark):
        return True   
    if (abs[0] == mark and abs[3] == mark and abs[6] == mark):
        return True
    if (abs[1] == mark and abs[4] == mark and abs[7] == mark):
        return True
    if (abs[2] == mark and abs[5] == mark and abs[8] == mark):
        return True  
    if (abs[0] == mark and abs[4] == mark and abs[8] == mark):
        return True
    if (abs[2] == mark and abs[4] == mark and abs[6] == mark):
        return True
    else:
        return False


  

def assess_moves(actual_board_state, turn_player_mark, opponent_mark, player_turn, path_score, square_ref):

#loop through empty squares, try the next move there on a new copy of the board state
    
    hypo_board_state = actual_board_state.copy()
    hypo_board_state[int(square_ref) - 1] = turn_player_mark
    if (check_player_win(hypo_board_state, turn_player_mark) is True) and (player_turn == False):
        path_score += 1
    if (check_player_win(hypo_board_state, turn_player_mark) is True) and (player_turn ==True):
        path_score -= 1
    else:
        if turn_player_mark == 'X':
            turn_player_mark = 'O'
            opponent_mark = 'X'
        if turn_player_mark == 'O':
            turn_player_mark ='X'
            opponent_mark ='0'
        player_turn = not player_turn
        for square in hypo_board_state:
            if square == 'O' or square == 'X':
                pass
            else:
                path_score = assess_moves(hypo_board_state, turn_player_mark, opponent_mark, player_turn, path_score, square)
    return path_score
    
            
    

