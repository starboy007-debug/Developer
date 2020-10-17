# printing  board
def boardt(board):
    print('\n'*20)
    print('   |   |')
    print(' ' + board[7] + ' | ' + '' + board[8] + ' |' + ' ' + board[9])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + '' + board[5] + ' | ' + ' ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + '' + board[2] + ' | ' + ' ' + board[3])
    print('   |   |')
x=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
yes=False
def win_check(board,m):
    return(board[1]==board[2]==board[3]==m or
           board[4]==board[5]==board[6]==m or
           board[7]==board[8]==board[9]==m or
           board[1]==board[4]==board[7]==m or
           board[2]==board[5]==board[8]==m or
           board[3]==board[6]==board[9]==m or
           board[7]==board[5]==board[3]==m or
           board[1]==board[5]==board[9]==m)
def board_check(board):
    if ' ' in board[1:]:
        return False
    else:
        return True
i=0
p1=input('Please select your marker X or O').capitalize()
if p1 == 'X':
    p2 = 'O'
else:
    p2 = 'X'
while i<=3:
    position1=int(input('Player 1:: Where Do you wanna Mark your Marker'))
    x[position1]=p1
    boardt(x)



    if win_check(x,'X')==True:
        print('Player 1 wins!!')

    else:
        if win_check(x,'O')==True:
            print('Player 2 wins!!')

        else:
            print('Match is a tie')


    if win_check(x,'O')==True or win_check(x,'X')==True:
        play = input('Do you wanna play again (y/n)')
        if play=='y':
            yes=True
            i=0
        else:
            print('Thanks for playing :-)')
            break


    position2 = int(input('Player 2:: where do you wanna mark your marker'))
    x[position2] = p2
    boardt(x)
    i += 1