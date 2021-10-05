# """
# user_input.py
#
# by; Adam Abernathy (AMA)
# AMA note: most functions were in battleship-g1.py, moved here to condense
#           user input and interacion
# """

import string

class User_Input :
    """
    User Input object used to prompt user for diffent control aspects of the game

    Example::

        user_input = User_Input()
        user_input._(_)
    """

    def __init__(self):
        super(User_Input, self).__init__()

    def get_num_ships(self):
        # Author: AMA, code was already in program, moved and slight changes
        # Date: sept 28 2021
        """
        prompts user for number of ships to use in the game

        :return _: number of ships in the game
        :rtype: int
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
        # Author: code already in file just moved, AMA added try except
        """
        prompts user for row col of move

        :return _: ``square`` to try move in
        :rtype: list of int, [x, y]
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
        # Author AMA, some code already in project just removed
        # Date: 9-29-2021
        """
        asks player if they would like to play another game

        :return True: if player wants to play another game
        :return False: else
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

    def get_difficulty(self):
        """
        Sets difficulty for CPU \n
        Author: Michael Talaga

        :return dif: user selected difficulty
        :rtype: int ``range(1,4)``
        """
        print("\nPlease choose CPU difficulty.\n")
        while True:
            dif = input("CPU Difficulty - (1 = easy, 2 = medium, 3 = impossible): ")
            if dif.isnumeric():
                dif = int(dif)
                if dif >= 1 and dif <= 3:
                    return dif
                else:
                    print("Please enter a number between 1 and 3.\n")
            else:
                print("Please enter a number")
