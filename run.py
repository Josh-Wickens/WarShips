# Import random so that the random function can be used
import random


# Intro to WarShips and enter players username


def welcome():
    # Prints welcome message, input for user to enter a username for the game
    print("\nWelcome to Warships!")
    print("\nPlease tell me your name")
    print("\nBefore we get started, I need to know your name \n")
    username = input("\ninsert name: ")
    print(f"\nWelcome to WarShips {username}!")


welcome()

# Build board for the game using 0 for placements
def build_board(dims):
    return [['O' for count in range(dims)] for count in range(dims)]


print(build_board(6))
