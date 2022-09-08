import random as r
from math import isqrt


## This function’s role is to check if a certain move is valid for a certain board.
## It will take:
##  1. An integer list, board
##  2. An integer, turn
##  3. An integer, index representing the index of the cube played
##  4. A push direction string, push_from that represents the direction of the push.
## Returns False if the move is not allowed, and returns True if the move is allowed.


def check_move(board, turn, index, push_from):
    n = isqrt(len(board))
    index = int(index)
    # check if user is taking out the other player's token
    if board[index] != turn and board[index] != 0:
        return False
    else:
        ok = ['T', 'L', 'B',
              'R']  # represents the allowable direction
        if (index + 1) % n == 0:
            ok.remove('R')
        if index % n == 0:
            ok.remove('L')
        if index < n:
            ok.remove('T')
        if (n ** 2) - 6 < index < n ** 2:
            ok.remove('B')
        if push_from.upper() not in ok or len(ok) == 4:
            return False
        else:
            return True


f = [2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 2, 0, 1, 1]
##Test Cases
b = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 2]
c = [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1]

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bad = [2, 2, 2, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1, 1, 2, 0, 1, 1]
test = [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
test2 = [1, 2, 2, 2, 1, 1, 2, 0, 0, 2, 2, 1, 2, 1, 1, 1, 2, 0, 0, 1, 1, 2, 2, 0, 0]


## Apply a move to a game. Takes an integer list: board, an integer: turn,
## as well as an integer: index (that will represent the index of the cube played)
## and a push direction: string push_from as inputs. The move is always assumed to be allowable.
## Returns an updated board according to that move.


def apply_move(board, turn, index, push_from):
    index = int(
        index)  # changes any string input to int value
    new = board.copy()  # creates a new board to apply move on
    n = isqrt(len(board))
    row = index // n  # row number of index, starting from 0
    col = index % n  # column number of index, starting from 0
    # stores the blocks below/above/beside index to be shiftedand assigns them to
    # the new board, adding the new block to the top/bottom/left/right of the board
    if push_from == 'B':
        new[index:1 + n ** 2 - n + col:n] = board[index + n:n ** 2:n] + [turn]
    if push_from == 'T':
        new[col:index + n:n] = [turn] + board[col:index:n]
    if push_from == 'L':
        new[row * n:index + 1] = [turn] + board[row * n:index]
    if push_from == 'R':
        new[index:(row + 1) * n] = board[index + 1:(row + 1) * n] + [turn]
    return new[:]


print()


##dis(apply_move(a,1,1,'B'))

##dis(apply_move(a,1,19,'T'))


##dis(apply_move(a,1,24,'T'))

##dis(apply_move(a,1,10,'R'))

##apply_move(a,1,1,'R')
##apply_move(a,1,20,'R')
##apply_move(a,1,22,'R')
##apply_move(a,1,0,'R')
##apply_move(a,1,5,'R')
##apply_move(a,1,15,'R')


##  Check for a win. Takes an integer list: board and an integer: who_played as inputs. It will return:
##– 0 if no win is present
##– 1 if player 1 wins
##– 2 if player 2 wins


def check_victory(board, who_played):
    b = isqrt(len(board))
    rows = [board[b * j:b * (j + 1)] for j in range(b)]
    columns = list(zip(*rows))
    winner = [0]
    for i in rows:
        if len(set(i)) == 1:
            winner += [i[0]]
    for j in columns:
        if len(set(j)) == 1:
            winner += [j[0]]
    y = [rows[i][i] for i in range(b)]
    x = [rows[::-1][i][i] for i in range(b)]
    if len(set(y)) == 1:
        winner += [y[0]]
    if len(set(x)) == 1:
        winner += [x[0]]
    for i in winner:
        if i != who_played and i != 0:
            return i
    if who_played in winner:
        return who_played
    else:
        return 0

    ##n = int(input("Board size? "))


##for i in range(0,n**2,n):
##    if sum(board[i:i+n]) == n and not sum(board[i:i+n]) == 2*n:
##       print (True)
##    if sum(board[i:i+n]) == n:
##       return 1
##    if sum(board[i:i+n]) == 2*n:
##       return 2


##  Level 1: Choose a random move from all possible moves (cube index and push choices).
##  Level 2: Choose a move that leads to a direct win if such a move exists. If no such move exists, it will play to prevent a
##           direct win for player in the next round.
##           If again no such move exists, pick a random valid move.
##  Level 3: Take smarter decisions, whenever there is not an obvious move to do.
##           Instead of choosing a random move, you can assign a grade to each possible move, for example by giving points depending on the number of same-symbol
##           cubes of their color in the same row, column or diagonal (say 100 points for each 4 same-symbol cubes of their color in the same row, column or diagonal
##           10 points for each 3 same-symbol cubes of their color in the same row, column or diagonal, etc.). You can use negative values for the opponents cubes sym
##           Eventually, make the move that maximizes the grade.
##           Hence ensure computer will get its symbols aligned as much as possible, and avoid having the player's symbols aligned.


# takes in int list, int turn, int level
# 3 levels: 1(easy), 2(medium), 3(hard)
# return index of cube played and string push_form which is direction of push played by computer
# Idea: Perhaps make a mini check victory function inside the program and tweak it such that it checks if players are going to achieve victory.

# def gonnawin(board):#returns a dictionary of near-wins and steps to achieve that win
#     win={}
#     n = isqrt(len(board))
#     rows = [board[b * j:b * (j + 1)] for j in range(b)]
#     columns = list(zip(*rows))
#     d1 = [rows[i][i] for i in range(b)]
#     d2 = [rows[::-1][i][i] for i in range(b)]
#     for i in rows:


def computer_move(board, turn, level):
    n = isqrt(len(board))
    moves = ['B', 'T', 'L', 'R']
    opp = 1
    if turn == 1:
        opp = 2
    if level == 2:  # Brute force check for every situation for computer direct win
        for i in range(0, n ** 2):
            for m in moves:
                if check_move(board, turn, i, m) == True:
                    if check_victory(apply_move(board, turn, i, m), turn) == turn:
                        return (i, m)
        winningmoves = []
        for i in range(0,
                       n ** 2):  # Brute force check for every situation for human win
            for m in moves:
                if check_move(board, opp, i, m) == True:
                    if check_victory(apply_move(board, opp, i, m),
                                     opp) == opp:  # computer will apply enemy move to see if there is win
                        winningmoves.append((i, m))
                        for i in range(0, n ** 2):
                            for m in moves:
                                if check_move(board, turn, i, m) == True:
                                    for win in winningmoves:
                                        if check_victory(apply_move(apply_move(board, turn, i, m), opp, win[0], win[1]),
                                                         opp) != opp:
                                            return (i, m)

                    else:  # no winning moves for human
                        pass

    goodmoves = []
    count = 0
    while count < ((n - 1) ** 2) * 4:
        for i in range(0, n ** 2):
            for m in moves:
                if check_move(board, turn, i, m) == True:
                    goodmoves.append((i, m))
                    count += 1
    r.shuffle(goodmoves)
    # for i in goodmoves:
    #     for j in range(0,n**2):
    #                2

    #             if check_victory(apply_move(apply_move(board, 1, i[0], i[1]),2,j,m),1) == 1:
    #             pass
    if level == 2:
        for good in goodmoves:
            for i in range(0, n ** 2):
                for m in moves:
                    if not check_move(board, opp, i, m):
                        continue
                    if check_victory(apply_move(apply_move(board, turn, good[0], good[1]), opp, i, m), opp) != opp:
                        return good
    else:
        return goodmoves[0]


test3 = [2, 2, 1, 1, 2, 2, 2, 2, 0, 1, 1, 2, 1, 2, 0, 1, 2, 2, 0, 0, 1, 1, 1, 0, 2]
test4 = [1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
test5 = [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 1, 1, 2, 0, 1]
test6 = [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 2, 2, 0, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 1]
test7 = [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0, 1, 2, 2, 1, 1]

# [1, 1, 1, 0, 0]
# [1, 0, 0, 0, 0]
# [2, 2, 2, 2, 0]
# [2, 0, 0, 0, 0]
# [1, 2, 2, 1, 1]

# print(computer_move(test4, 1, 2))

test8 = [1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 2, 0, 0, 0, 0, 2, 1, 0, 0, 2, 2, 1, 1]

# [1, 0, 0, 0, 0]
# [0, 0, 2, 0, 1]
# [0, 0, 2, 0, 0]
# [0, 0, 2, 1, 0]
# [0, 2, 2, 1, 1]


print(computer_move(test8, 1, 2))


# display board. not much to say here
def display_board(board):
    matrix = []
    f = len(board)
    for i in board:
        if len(matrix) == isqrt(f):
            print(matrix)
            matrix = [i]
        else:
            matrix += [i]
    print(matrix)


# outside function to create a board of n size
def make(n):
    whole = []
    for i in range(0, n):
        whole += [0]
    return whole


def menu():
    q1 = 'Which index would you like to pop? Please give a value from 0-24. '  # stores query for index input
    q2 = 'From which direction? Select from the following: L, B, T or R. '  # stores query for direction input
    print('Welcome to Quixo!')
    print()
    while True:
        try:
            blen = int(input(
                'Please state the length of your desired board. '))  # length of board input
            if blen < 2:
                print('Board length must be at least 2. Please give another number.')
                continue
            new = make(blen ** 2)
            break
        except:
            print('Please enter a positive integer.', '\n')
    print()
    start_option = input('Enter 1 to play against against a friend, or 2 to play against the computer. ')
    if start_option == '2':
        # option to choose computer level
        diffi = int(input('Which level would you like to play against? '))
        # code for P1 Computer
        if input('Which player would you like to play as, 1 or 2? ') != '2':
            while True:
                display_board(new)
                print('Your move.', '\n')
                while True:
                    pop, direction = input(q1), input(q2)
                    try:
                        if not check_move(new, 1, pop, direction):
                            print('This move is not allowed! Please try again.', '\n')
                        else:
                            break
                    except:
                        print("You have entered an invalid input. Please try again!", '\n')
                new = apply_move(new, 1, pop, direction.upper())
                if check_victory(new, 1) != 0:
                    print('You won! Congratulations!')
                    break
                display_board(new)
                print()
                c_move = computer_move(new, 2, diffi)
                print('Computer move: index ', str(c_move[0]), ' direction ', str(c_move[1]))
                new = apply_move(new, 2, c_move[0], c_move[1])
                if check_victory(new, 2) != 0:
                    print('Computer won! Duration till the AI uprising has been shortened by: Two Months.')
                    break
                    # code for P2 Computer
        else:
            while True:
                print()
                c_move = computer_move(new, 1, diffi)
                new = apply_move(new, 1, c_move[0], c_move[1])
                print('Computer move: index ', str(c_move[0]), ' direction ', str(c_move[1]))
                if check_victory(new, 1) != 0:
                    print('Computer won! Duration till the AI uprising has been shortened by: Two Months.')
                    break
                display_board(new)
                print('Your move.')
                while True:
                    pop, direction = input(q1), input(q2)
                    try:
                        if not check_move(new, 2, pop, direction):
                            print('This move is not allowed! Please try again.', '\n')
                        else:
                            break
                    except:
                        print("You have entered an invalid input. Please try again!", '\n')
                new = apply_move(new, 2, pop, direction.upper())
                if check_victory(new, 2) != 0:
                    print('You won! Congratulations!')
                    break
                display_board(new)
    elif start_option == '1':
        while True:
            print('Player 1\'s move.', '\n')
            display_board(new)
            print()
            while True:
                pop, direction = input(q1), input(q2)
                try:
                    if not check_move(new, 2, pop, direction):
                        print('This move is not allowed! Please try again.', '\n')
                    else:
                        break
                except:
                    print("You have entered an invalid input. Please try again!", '\n')
            new = apply_move(new, 1, pop, direction.upper())
            if check_victory(new, 1) != 0:
                print('Player 1 won!')
                break
            print('Player 2\'s move.', '\n')
            display_board(new)
            print()
            while True:
                pop, direction = input(q1), input(q2)
                try:
                    if not check_move(new, 2, pop, direction):
                        print('This move is not allowed! Please try again.', '\n')
                    else:
                        break
                except:
                    print("You have entered an invalid input. Please try again!", '\n')
            new = apply_move(new, 2, pop, direction.upper())
            if check_victory(new, 2) != 0:
                print('Player 2 won!')
                break
    else:
        print('Sorry, you have entered an invalid input. Please try again!')


menu()







