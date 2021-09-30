"""
user_input.py

by; Adam Abernathy (AMA)
AMA note: most functions were in battleship-g1.py, moved here to condense
          user input and interacion
"""

import string

"""
user input object
"""
class User_Input :
    """docstring for User_Input."""

    def __init__(self):
        """ default constructor
        """
        super(User_Input, self).__init__()

    def get_num_ships(self):
        """
        prompts user for number of ships to use in the game
        :author AMA, code was already in program, moved and slight changes
        :date sept 28 2021
        :pre
        :return number of ships in the game
        """
        choice_made = False
        while not choice_made:
            print('How many ships per player for this game?\n')
            try:
                num_ships = input('Enter a number from 1 to 6:\n')
                if num_ships.isnumeric():
                    ship_num = int(num_ships)
                    if ship_num in range(1, 7):
                        choice_made = True
                    else:
                        print("Please enter a number between 1 and 6!\n")
                else:
                    print("Please enter a valid ship number.\n")
            except (ValueError, TypeError):
                print("Please enter a valid ship number.\n")
        return int(num_ships)

    def get_move_coord(self):
        """
        prompts user for row col of move
        :author code already in file just moved, AMA added try except
        :date
        :pre
        :return list of [row, col]
        """
        #check for valid column input
        while True:
            try:
                x_hit = input("\nWhat column?\n")
                if x_hit.isalpha():
                    x_coord = (ord(x_hit) % 32) - 1
                    if x_coord in range (0, 10):
                        break
                    else:
                        print("Please enter a letter between A-J")
                else:
                    print("Please enter a valid column. (A-J)")
            except (ValueError, TypeError):
                print("Please enter a valid column. (A-J)")
        #check for valid row input
        while True:
            try:
                y_hit = input("\nWhat row?\n")
                if y_hit.isnumeric():
                    y_coord = int(y_hit) - 1
                    if y_coord in range(0, 10):
                        break
                    else:
                        print("Please enter a number between 1-9.)")
                else:
                    print("Please enter a valid row. (1-9)")
            except (ValueError, TypeError):
                print("Please enter a valid row. (1-9)")
        coords = [x_coord, y_coord]
        return coords

    def play_again(self):
        """
        asks player if they would like to play another game
        :author AMA, some code already in project just removed
        :date 9-29-2021
        :pre
        :return :True if player wants to play another game, false else
        """
        selection = False
        while True:
            print("\nWould you like to play another game?\n")
            try:
                endgame = input('Enter "Y" for YES, "N" for NO: ')
                if endgame == 'Y' or endgame == 'y':
                    selection = True
                    break
                elif endgame == "N" or endgame == "n":
                    break
                else:
                    print("\nInvalid Input.")
            except (ValueError, TypeError):
                print("\nInvalid Input.")
        return selection
