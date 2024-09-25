import random
import tictactoefunctions as func

actual_board_state = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
win_state = False

print("Hi! Let's play Tic Tac Toe!")

player_mark = input("Would you like to be X or O?").upper()

while player_mark not in ['X', 'x', 'O', 'o']:
    player_mark = input("I'm sorry, please choose X or O:").upper()

if player_mark == 'O':
    computer_mark = 'X'
    print(f"Great! You are {player_mark}s, I'll be {computer_mark}s!")
else:
    computer_mark = 'O'
    print(f"Great! You are {player_mark}s, I'll be {computer_mark}s!")


print("I'll randomly choose who goes first...")

coinflip = random.randint(0,1)

if coinflip == 0:
    player_turn = True
    print("You get to go first")
else:
    player_turn = False
    print("I'll go first!")

func.print_board(actual_board_state)

turn_count = 0

while win_state == False:

    if turn_count == 9:
        print("Game Over")
        win_state = True
        break

    if player_turn == True:
        turn_count +=1
        while True:
            try:    
                choice = int(input("Which square do you choose? "))
                break
            except:
                print("Please choose an empty square number!")
        while choice not in range(1,10) or actual_board_state[choice-1] == 'X' or actual_board_state[choice-1] =='0':
            choice = input("Please choose an empty square number:")

        choice = int(choice)
        
        print("Good move!")
        actual_board_state[choice -1] = player_mark
        func.print_board(actual_board_state)
        win_check = func.check_player_win(actual_board_state, player_mark)
        
        if win_check is True:
            print("You win!")
            win_state = True
        else:
            player_turn = False

    if turn_count == 9:
        print("Game Over")
        win_state = True
        break

    if player_turn == False:
        turn_count +=1
        for square in actual_board_state:
            if square == 'O' or square == 'X':
                pass
            else:                
                hypo_board_state = actual_board_state.copy()
                hypo_board_state[int(square) - 1] = computer_mark
                if (func.check_player_win(hypo_board_state, computer_mark) is True):
                    print(f"My turn! I want square number {actual_board_state[int(square)-1]}!")
                    actual_board_state[int(square) - 1] = computer_mark
                    func.print_board(actual_board_state)
                    print("I win!")
                    player_turn = True
                    win_state = True
                    break
    if player_turn == False:   
        for square in actual_board_state:
            if square == 'O' or square == 'X':
                pass
            else:
                    hypo_board_state = actual_board_state.copy()
                    hypo_board_state[int(square) - 1] = player_mark
                
                    if (func.check_player_win(hypo_board_state, player_mark) is True):
                        print(f"My turn! I'll choose square number {actual_board_state[int(square)-1]}!")
                        actual_board_state[int(square) - 1] = computer_mark
                        func.print_board(actual_board_state)
                        print("Your turn!")
                        player_turn = True
                
                        break
    
    if player_turn == False:
            path_scores = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            for square in actual_board_state:
                if square == 'O' or square == 'X':
                    pass
                else:
                    path_scores[square] = func.assess_moves(actual_board_state, computer_mark, player_mark, player_turn, 0, square)
            
            next_move = 0
            next_move_value = -1000


            for square, value in path_scores.items():
                if value > next_move_value:
                    next_move = square
            
            print(f"I'll choose square number {next_move}!")

            actual_board_state[int(next_move)-1] = computer_mark
            func.print_board(actual_board_state)

            player_turn = True
           

