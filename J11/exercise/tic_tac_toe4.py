from colorama import Fore , Back 
def show_board(board_game):
    # show the board
    for i in range(3):
        for j in range(3):
            print(board_game[i][j],end=' ')
        print()
    print()

def check_endgame():
    # if , 8 elif , else
    if board_game[0][0] and board_game[0][1] and board_game[0][2] == 'X':
        print('P1 WIN')
    elif board_game[1][0] and board_game[1][1] and board_game[1][2] == 'X':
        print('P1 WIN')
    elif board_game[2][0] and board_game[2][1] and board_game[2][2] == 'X':
        print('P1 WIN')
    elif board_game[0][0] and board_game[0][1] and board_game[0][2] == 'X':
        print('P1 WIN')
    elif board_game[1][0] and board_game[1][1] and board_game[1][2] == 'X':
        print('P1 WIN')
    elif board_game[2][0] and board_game[2][1] and board_game [2][2] == 'X':
        print('P1 WIN')   

    elif board_game[0][0] and board_game[0][1] and board_game[0][2] == 'O':
        print('P2 WIN')
    elif board_game[1][0] and board_game[1][1] and board_game[1][2] == 'O':
        print('P2 WIN')
    elif board_game[2][0] and board_game[2][1] and board_game[2][2] == 'O':
        print('P2 WIN')
    elif board_game[0][0] and board_game[0][1] and board_game[0][2] == 'O':
        print('P2 WIN')
    elif board_game[1][0] and board_game[1][1] and board_game[1][2] == 'O':
        print('P2 WIN')
    elif board_game[2][0] and board_game[2][1] and board_game [2][2] == 'O':
        print('P2 WIN') 
    
    else:
        print('equal!')
    


board_game = [['_','_','_'],
              ['_','_','_'],
              ['_','_','_']]

print(Fore.RED,'O',Fore.RESET,sep='')
print('or')
print(Fore.BLUE,'X',Fore.RESET,sep='')
player1 = input('P1 , please enter your choise: ')
if player1 == 'X':
    player2 = 'O'
elif player1 == 'O':
    player2 = 'X'

while True:
    while True:
        show_board(board_game)

        # player_1
        if player1 == 'X':
            print(Fore.RED,'#P1#',Fore.RESET,' ','row: ',sep='')
            player1_row = int(input()) -1
            print(Fore.RED,'#P1#',Fore.RESET,' ','column : ',sep='')
            player1_column = int(input()) -1
        elif player1 == 'O':
            print(Fore.BLUE,'#P1#',Fore.RESET,' ','row: ',sep='')
            player1_row = int(input()) -1
            print(Fore.BLUE,'#P1#',Fore.RESET,' ','column : ',sep='')
            player1_column = int(input()) -1

        if ( 0 <= player1_row <= 2) and ( 0 <= player1_column <= 2):
            pass
        else:
            print('#P1# your number is out of range (1-3)')
            continue

        if board_game[player1_row][player1_column ] == '_':
            board_game[player1_row][player1_column] = 'X'
            break
        else:
            print('This box is full')

    check_endgame()

    # show the board
    while True:
        show_board(board_game)

        # player_2
        if player2 == 'X':
            print(Fore.RED,'#P2#',Fore.RESET,' ','row: ',sep='')
            player2_row = int(input()) -1
            print(Fore.RED,'#P2#',Fore.RESET,' ','column : ',sep='')
            player2_column = int(input()) -1
        elif player2 == 'O':
            print(Fore.BLUE,'#P2#',Fore.RESET,' ','row: ',sep='')
            player2_row = int(input()) -1
            print(Fore.BLUE,'#P2#',Fore.RESET,' ','column : ',sep='')
            player2_column = int(input())

        if ( 0 <= player2_row <= 2) and ( 0 <= player2_column <= 2):
            pass
        else:
            print('#P1# your number is out of range (1-3)')
            continue

        if board_game[player2_row][player2_column ] == '_':
            board_game[player2_row ][player2_column ] = 'O'
            break
        else:
            print('This box is full')

    check_endgame()