""" Welcome to Warships """
# Import random so that the random function can be used
import random

player_score = 0
comp_score = 0
username = ""
hint_left = 3


def welcome():
    """
    Prints welcome message &
    input for user to enter a username for the game
    """
    print("\nWelcome to Warships!")
    print("\nPlease tell me your name")
    print("\nBefore we get started, I need to know your name")
    global username
    username = input("\ninsert name: \n")
    print(f"\nWelcome to WarShips {username}!")
    print("\nSelect a row coordinate from 0-5 and column coordinate from 0-5")
    print("\nif you hit a boat. It will be marked with an X.")
    print("\nIf you miss it will be marked with M")
    print("\nThere are 2 boats to hit. They can be any length up to 4 spaces")
    print("\nif you miss 5 times the game is over and you lose.")
    print("\nIf you sink both boats. Then you WIN!\n")


welcome()
# Calls the welcome function once once programme opens


def build_board(dims):
    """ Build board for the game using 0 for placements -
    Creates a list of 0 by the length of dims which is
    defined in the main function. Then times/duplicate
    the amount of lists by the length of dims 
    so it will create a square of 0's
    """
    return [['O' for count in range(dims)] for count in range(dims)]


def print_board(board):
    """
    This function will get rid of the commas, quotations
    and brackets for the board.
    The * makes the list on one line.
    """
    for pos in board:
        print(*pos)


def build_ship(dims):
    """
    Builds ships using the random function for orientation and
    coordinates.
    This code is used from https://bigmonty12.github.io/battleship
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
    If the guess is not within 0-5 or the input is not a
    digit it will make the user guess again
    until a valid number is chosen.
    """
    row = None
    col = None

    while True:
        print("\nPlease choose a number between 0-5")
        row = input("\nRow: \n")

        if not row.isdigit() or int(row) >= 6:
            continue
        else:
            row = int(row)
            break

    while True:
        print("\nPlease choose a number between 0-5")
        col = input("\nCol: \n")

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
    will update the board depending on the outcome.
    If hit - O will be replaced by an X.
    If miss - O will be replaced by an M.
    """
    if guess in guesses:
        # If the coordinates have already been guessed
        print('You have already guessed that coordinate. Try a dfferent one')
        return board
    guesses.append(guess)
    if guess in ship1 and guess in ship2:
        # If the coordinates are in both ship 1 and ship 2
        print("\nWow! Two birds with 1 stone! You hit 2 ships with 1 bullet!")
        print("\nGreat Shot!!")
        board[guess[0]][guess[1]] = 'X'
        """
        Remove this value from ship coordinates to prevent
        mutiple hits on same ship cooridnate
        """
        ship1.remove(guess)
        ship2.remove(guess)
        return board
    if guess in ship1:
        print('\nGood Hit!\n')
        board[guess[0]][guess[1]] = 'X'
        ship1.remove(guess)
        return board
    if guess in ship2:
        print('\nGood Hit!\n')
        board[guess[0]][guess[1]] = 'X'
        ship2.remove(guess)
        return board
    if guess not in ship1 or ship2:
        board[guess[0]][guess[1]] = 'M'
        print('\nYou missed! Please try again!')
        print(f"\n you have {5 - len(incorrect)} guesses left!\n")
        incorrect.append(guess)
    return board


def try_again():
    """
    Try again function will give the user the option to play the game again.
    If user inputs Y then the main function will run again and replenish hints.
    If user selects N, then the progamme will finish.
    """
    print("\nWould you like to play again and increase your score?")
    print("\ntype y for yes or n for no")
    again = input("\nY or N?: \n")
    again = again.upper()
    if again == "N":
        print("\nThank you for playing!")
        print("\nHope to see you again!!")
        return
    if again == "Y":
        global hint_left
        hint_left = 3
        main()
    else:
        # To prevent the user from inputting anything other than Y or N
        print("\nError please type y for yes or n for no")
        try_again()


def main():
    """
    the main function for the game. This will call upon functions
    depending on where the game is up to.
    also provides the end to the game pending on guesses left or ships left
    """
    guesses = []
    incorrect = []
    all_alive = True
    board = build_board(6)
    ship1 = build_ship(4)
    ship2 = build_ship(4)
    print_board(board)
    while len(ship1 + ship2) > 0 and len(incorrect) < 6:
        """
        This while loop will run whilst the length of ship is more than 0
        and the length of incorrect answers is less than 6
        """
        board = update_board(
            user_guess(), board, ship1, ship2, guesses,
            incorrect)
        print_board(board)
        print("\nYou have guessed the following coordinates so far:")
        print(*guesses)
        global hint_left
        if (len(ship1) == 0 or len(ship2) == 0) and all_alive is True:
            """
            Run this only if a boat hasn't been sunk yet. 
            Set's the hint to 0 and all alive for false to prevent hints being used again 
            and states that not all the ships are alive so this if function isn't ran again.
            """
            print("\nYOU SANK A BATTLESHIP!")
            print("\nOnly 1 ship left! No more hints! Your on your own!")
            hint_left = 0
            all_alive = False
        while hint_left > 0:
            # Only run this while loop whilst there are hints left (more than 0)
            hint = input("\nWould you like a hint? Y for Yes N for No: \n")
            hint = hint.upper()
            if hint == "Y":
                # If user keys Y then the first coordinate for ship1 will be displayed
                if hint_left >= 1:
                    row_hint = [x[0] for x in ship1]
                    print(f"\nThere is a boat in row {row_hint[0]}!")
                    hint_left = hint_left - 1
                    print(f"\nYou have {hint_left} hints left")
                if hint_left == 0:
                    print("\nNo more hints left! Your on your own!")  
                break
            elif hint == "N":
                # If user keys n then it will break the while loop
                break
            else:
                # If user enters anything other than Y or N, then it will revert to the beginning of the while loop
                print("\nError! Please enter either Y or N\n")
                continue
            
    if len(ship1 + ship2) == 0:
        """
        Code for if both ships are sunk and user wins.
        Increment user score by 1 and display score.
        Then offer the user to try again with the try again function.
        """
        print('\nYOU SUNK THE WARSHIPS! CONGRATULATIONS YOU WIN!')
        global username
        global comp_score
        global player_score
        player_score = player_score + 1
        print("\nThe score is:\n")
        print(f"{username} = {str(player_score)}")
        print(f"COMPUTER = {str(comp_score)}\n")
        try_again()
    else:
        # Code for is player loses. Increment computer score and offer to play again
        print("\n you have run out of guesses! You Lose!")
        comp_score = comp_score + 1
        print("\nThe score is:")
        print(f"{username} = {str(player_score)}")
        print(f"COMPUTER = {str(comp_score)}\n")
        try_again()
    return


# Runs the main function once user has entered a username and the rest of the code has loaded.
main()
