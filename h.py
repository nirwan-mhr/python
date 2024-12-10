def main():
    # start=input("Hi! Welcome to tic tac toe\nWould you like to start the game?(Y,N)")

    # a1=a2=a3=b1=b2=b3=c1=c2=c3='  '
    board=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    

    # if(start.upper()=='Y'):
    #     print("Great, lets start")
    #    print (grid)
    #     player_symbol=input('''What Symbol do you want?
    # X or O (Enter X or O)''')
    #     if(player_symbol.upper() in ('O','0')):
    #         print("Great! You chose 'O' as your symbol, Now lets start the game")
    #     elif(player_symbol.upper() in ('X','x')):
    #         print("Great! You chose 'X' as your symbol, Now lets start the game")
    #     else:
    #         print("You entered an invalid symbol")
    
    # print(f'You will have to choose the position to place {player_symbol} which you can do by entering numbers 1-9 as showsn in the grid below')
    # print(f'''
    # 1 | 2 | 3 
    # ---------
    # 4 | 5 | 6
    # ---------
    # 7 | 8 | 9
    # ''')
    # user_input_position=int(input('Please enter position'))
    
    move='X'

    while True:
        grid=f'''
    {board[0][0]} | {board[0][1]} | {board[0][2]}
    ----------
    {board[1][0]} | {board[1][1]} | {board[1][2]}
    ----------
    {board[2][0]} | {board[2][1]} | {board[2][2]}
    '''
        print(grid)
        try:
            user_input=int(input('Enter position: '))
        except (ValueError):
            print('Invalid input')
            continue
        for row in range(3):
            for posn in range(3):
                if board[row][posn]==user_input:
                    board[row][posn]=move
        if(won(board)):
            rematch = input(f"{move} won the game")
            break
        if(game_end(board)):
            print("Game ended")
            break
        if (move=='X'):
            move='O'
        else:
            move='X'

def won(board):
    # Check rows
    if board[0][0] == board[0][1] == board[0][2]:
        return True
    if board[1][0] == board[1][1] == board[1][2]:
        return True
    if board[2][0] == board[2][1] == board[2][2]:
        return True

    # Check columns
    if board[0][0] == board[1][0] == board[2][0]:
        return True
    if board[0][1] == board[1][1] == board[2][1]:
        return True
    if board[0][2] == board[1][2] == board[2][2]:
        return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def game_end(board):
    for row in range(3):
        for posn in range(3):
            if (board[row][posn]!='X' and board[row][posn]!='O'):
                return False
    return True

if __name__=='__main__':
    main()