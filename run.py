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

# Build board for the game using 0 for placements
def build_board(dims):
    return [['O' for count in range(dims)] for count in range(dims)]


board = build_board(6)

def print_board(board):
    # This function will get rid of the commas and brackets for the board
    for b in board:
        print(*b)


print_board(board)
