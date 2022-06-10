""" Welcome to Warships """
# Import random so that the random function can be used
import random


def welcome():
    """ Prints welcome message &
    input for user to enter a username for the game
    """
    print("\nWelcome to Warships!")
    print("\nPlease tell me your name")
    print("\nBefore we get started, I need to know your name")
    username = input("\ninsert name: ")
    print(f"\nWelcome to WarShips {username}!\n")
    print("\nSelect a row coordinate from 0-6 and column coordinate from 0-6")
    print("\nif you hit a boat. It will be marked with an X.")
    print("\nIf you miss it will be marked with #")
    print("\nThere are 2 boats to hit. They can be any length up to 4 spaces")
    print("\nif you miss 5 times the game is over and you lose.")
    print("\nIf you sink both boats. Then you WIN!\n")


def build_board(dims):
    """ Build board for the game using 0 for placements """
    return [['O' for count in range(dims)] for count in range(dims)]


def print_board(board):
    """
    This function will get rid of the commas, quotations
    and brackets for the board.
    The * makes the list on one line
    """
    for pos in board:
        print(*pos)


def build_ship(dims):
    """
    Builds ships using the random function for orientation and
    coordinates
    """
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


def user_guess():
    """
    provides an input for user to select guess.
    Will only allow an integer for an input
    and only 1 character long
    """
    try:
        row = int(input('\nROW: '))
        col = int(input('COL: '))
        if row or col <= 6:
            return (row, col)
        else:
            return None
            raise ValueError
    except ValueError:
        print("Please choose a number between 0-6")
        user_guess()


def update_board(guess, board, ship1, ship2, guesses, incorrect):
    """
    Function to check if the guess has already been guessed
    or if it is a hit or miss.
    will update the board depending on the outcome
    """
    if guess in guesses:
        print('You have already guessed that coordinate. Try a dfferent one')
        return board
    guesses.append(guess)
    if guess in ship1:
        print('\nGood Hit!\n')
        # Update board with 'X' if hit
        board[guess[0]][guess[1]] = 'X'
        # Remove this value from ship coordinates to prevent
        # mutiple hits on same ship cooridnate
        ship1.remove(guess)
        return board
    if guess in ship2:
        print('\nGood Hit!\n')
        # Update board with 'X' if hit
        board[guess[0]][guess[1]] = 'X'
        # Remove this value from ship coordinates to prevent
        # mutiple hits on same ship cooridnate
        ship2.remove(guess)
        return board
    if guess not in ship1 or ship2:
        board[guess[0]][guess[1]] = '#'
        print('\nYou missed! Please try again!')
        print(f"\n you have {5 - len(incorrect)} guesses left!\n")
        incorrect.append(guess)
    return board


def main():
    """
    the main function for the game. This will call upon functions
    depending on where the game is up to.
    also provides the end to the game pending on guesses left or ships left
    """
    welcome()
    board = build_board(6)
    ship1 = build_ship(4)
    ship2 = build_ship(4)
    guesses = []
    incorrect = []
    print_board(board)
    while len(ship1 + ship2) > 0 and len(incorrect) < 6:
        board = update_board(user_guess(), board, ship1, ship2, guesses, incorrect)
        print_board(board)
        print("\nYou have guessed the following coordinates so far:")
        print(*guesses)
    if len(ship1 + ship2) == 0:
        print('You sunk the Warship!')
    else:
        print("\n you have run out of guesses! You Lose!")
    return


main()
