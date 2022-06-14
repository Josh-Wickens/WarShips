""" Welcome to Warships """
# Import random so that the random function can be used
import random

score = 0

def welcome():
    """ Prints welcome message &
    input for user to enter a username for the game
    """
    print("\nWelcome to Warships!")
    print("\nPlease tell me your name")
    print("\nBefore we get started, I need to know your name")
    print("\nSpeak friend and enter ;) ")
    username = input("\ninsert name: ")
    print(f"\nWelcome to WarShips {username}!\n")
    print("\nSelect a row coordinate from 0-5 and column coordinate from 0-5")
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
    An input for user to guess a row and column.
    If the guess is not within 0-5 it will make the user
    guess again until a valid number is chosen.
    """
    row = None
    col = None

    while True:
        print("\nPlease choose a number between 0-5")
        row = input("\nRow: ")

        if not row.isdigit() or int(row) >= 6:
            continue
        else:
            row = int(row)
            break

    while True:
        print("Please choose a number between 0-5")
        col = input("\nCol: ")

        if not col.isdigit() or int(col) >= 6:
            continue
        else:
            col = int(col)
            break
    return (row, col)


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
    if guess in ship1 and guess in ship2:
        print("\nWow! Two birds with 1 stone! You hit 2 ships with 1 bullet!")
        print("Great Shot!!")
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


def try_again(guesses, incorrect, ship1, ship2, username):
    print("Would you like to play again and increase your score?")
    print("type y for yes or n for no")
    again = input("\nY or N?")
    again = again.upper()
    if again != "Y" or "N":
        print("Error please type y for yes or n for no")
        try_again()
    elif again "Y":
        del (guesses)
        del (incorrect)
        del (ship1)
        del (ship2)
        main()
    else:
        print(f"\nThank you for playing {username}!")
        print("\nHope to see you again!!")
            



def main():
    """
    the main function for the game. This will call upon functions
    depending on where the game is up to.
    also provides the end to the game pending on guesses left or ships left
    """
    guesses = []
    incorrect = []
    welcome()
    board = build_board(6)
    ship1 = build_ship(4)
    ship2 = build_ship(4)
    print_board(board)
    print(ship1, ship2)
    while len(ship1 + ship2) > 0 and len(incorrect) < 6:
        board = update_board(
            user_guess(), board, ship1, ship2, guesses,
            incorrect)
        print_board(board)
        print("\nYou have guessed the following coordinates so far:")
        print(*guesses)
        if len(ship1) == 0 or len(ship2) == 0:
            print("\nYOU SANK A BATTLESHIP!")
    if len(ship1 + ship2) == 0:
        print('YOU SUNK THE WARSHIPS! CONGRATULATIONS YOU WIN!')
    else:
        print("\n you have run out of guesses! You Lose!")
    return


main()
