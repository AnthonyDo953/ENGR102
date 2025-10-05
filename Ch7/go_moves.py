# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: William Gipson
# Anthony Do
# Simon O'brien
# Michaela Gutermuth
# Section: 217
# Assignment: Go Moves
# Date: 04 10 2025

rows = 9
cols = 9

# Create a 9x9 board
board = [['.' for i in range(cols)] for i in range(rows)]

blackTurn = ''
whiteTurn = ''

# Display the current state of the board
def displayBoard():
    for row in board:
        for coordinate in row:
            print(coordinate, end=" ")
        print()

# Update the board according to white's turn
def updateBoardWT(wt):
    wc = int(wt.split()[0])
    wr = int(wt.split()[1])

    if board[9 - wc][wr - 1] == '.':
        board[9 - wc][wr - 1] = chr(9679)
        return True
    else:
        return False

# Update the board according to black's turn
def updateBoardBT(bt):
    bc = int(bt.split()[0])
    br = int(bt.split()[1])

    if board[9 - bc][br - 1] == '.':
        board[9 - bc][br - 1] = chr(9675)
        return True
    else:
        return False

# Keep playing until one of the players says to stop
while True: 
    # Display the board after every move
    displayBoard()
    # Black's turn
    blackTurn = input('Black Turn!\nEnter the coordinate you wish to place a stone: ')
    # Keep playing unless black says to stop
    if blackTurn.lower() != 'stop':
        # If the black player puts in an invalid move, ask them to try again until they do
        while not updateBoardBT(blackTurn):
            print('There is already a stone at that coordinate. Try again.')
            blackTurn = input('Black Turn!\nEnter the coordinate you wish to place a stone: ')
    else:
        print("Game stopped")
        break

    # Display the board after every move
    displayBoard()
    # White's turn
    whiteTurn = input('White Turn!\nEnter the coordinate you wish to place a stone: ')
    # Keep playing unless white says to stop
    if whiteTurn.lower() != 'stop':
        # If the black player puts in an invalid move, ask them to try again until they do
        while not updateBoardWT(whiteTurn):
            print('There is already a stone at that coordinate. Try again.')
            whiteTurn = input('White Turn!\nEnter the coordinate you wish to place a stone: ')
    else:
        print("Game stopped")
        break