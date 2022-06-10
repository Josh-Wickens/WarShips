# Import random so that the random function can be used
from random import randint


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
    

print_board(board)


