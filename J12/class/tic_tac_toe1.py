# ساخت صفحه برد گیم
#نمایش 
#  حلقه وایل ترو: 
# دریافت انتخاب از بازیکان اول
# نمایش
# دریافت از انتخاب از بازکین دوم
# نمایش
# شرط پایان

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
        
    pass

board_game = [['_','_','_'],
              ['_','_','_'],
              ['_','_','_']]

while True:
    while True:
        show_board(board_game)
        # زیبا ش کن
        # سطر و سطول بده کاربر اما میتونی توی جایگاه ها عدد بزاری که این مسیر دوم برای برنامه نویس سخت تر و برای کاربر بهتره

        # player_1 : X
        player1_row = int(input('#P1# row: ')) -1
        player1_column = int(input('#P1# column : ')) -1

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

        # player_2 = O
        player2_row = int(input('#P2# row: ')) -1
        player2_column = int(input('#P2# column: ')) -1

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