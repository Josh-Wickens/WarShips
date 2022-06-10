# Import random so that the random function can be used
import random


# Intro to WarShips and enter players username


def welcome():
    # Prints welcome message, input for user to enter a username for the game
    print("\nWelcome to Warships!")
    print("\nPlease tell me your name")
    print("\nBefore we get started, I need to know your name")
    username = input("\ninsert name: ")
    print(f"\nWelcome to WarShips {username}!\n")


# Calls the welcome message function
welcome()


def build_board(dims):
    # Build board for the game using 0 for placements
    return [['O' for count in range(dims)] for count in range(dims)]


board = build_board(6)


def print_board(board):
    '''
    This function will get rid of the commas, quotations
    and brackets for the board.
    The * makes the list on one line
    '''
    for b in board:
        print(*b)


def build_ship(dims):
    len_ship = random.randint(2, dims)
    orientation = random.randint(0, 1)
    if orientation == 0:
        row_ship = [random.randint(0, dims - 1)] * len_ship
        col = random.randint(0, dims - len_ship)
        col_ship = list(range(col, col + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    else:
        col_ship = [random.randint(0, dims - 1)] * len_ship
        row = random.randint(0, dims - len_ship)
        row_ship = list(range(row, row + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    return list(coords)


print_board(board)
ship = build_ship(4)
print(ship)


def user_guess():
    # Subtract 1 to adjust for python 0-based indexing
    row = int(input('Row: ')) - 1
    col = int(input('Col: ')) - 1
    return (row, col)


x = user_guess()
print(x)


def update_board(guess, board, ship, guesses):
    if guess in guesses:
        print('You have already guessed that coordinate. Try a dfferent one')
        return board
    guesses.append(guess)
    if guess in ship:
        print('Good Hit!')
        # Update board with 'X' if hit
        board[guess[0]][guess[1]] = 'X'
        # Remove this value from ship coordinates to prevent mutiple hits on same ship cooridnate
        ship.remove(guess)
        return board
    print('You missed!')
    return board


guesses = []
our_guess = user_guess()
board = update_board(our_guess, board, ship, guesses)
print_board(board)
