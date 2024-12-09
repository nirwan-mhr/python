start=input("Hi! Welcome to tic tac toe\nWould you like to start the game?(Y,N)")

a1=a2=a3=b1=b2=b3=c1=c2=c3='  '

grid=f''' {a1} | {a2} | {a3}
----------
{b1} | {b2} | {b3}
----------
{c1} | {c2} | {c3}
'''

if(start.upper()=='Y'):
    print("Great, lets start")
    print (grid)
    player_symbol=input('''What Symbol do you want?
X or O (Enter X or O)''')
    if(player_symbol.upper() in ('O','0')):
        print("Great! You chose 'O' as your symbol, Now lets start the game")
    elif(player_symbol.upper() in ('X','x')):
        print("Great! You chose 'X' as your symbol, Now lets start the game")
    else:
        print("You entered an invalid symbol")
print(f'You will have to choose the position to place {player_symbol} which you can do by entering numbers 1-9 as showsn in the grid below')
print(f'''1 | 2 | 3 
---------
4 | 5 | 6
---------
7 | 8 | 9
''')
user_input_position=int(input('Please '))    
    
