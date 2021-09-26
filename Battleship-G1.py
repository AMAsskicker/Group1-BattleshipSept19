# Import class methods needed for the program
from Board import *
from cpu_player import CPU_Player
# libs
import string
import sys

'''
Responsible for executing the game.

edited: sept 24 2021
by: Adam Abernaty (AMA)
AMA note: no author or createion date when forked
'''

def setup_user(board, numberShips):
    """
    Interacts with player to set up a board with ships for a player
    :pre board objectmust have correct properties; numberShips must be in the proper range, 1 to 6
    :post the input board object is modified according to user input
    :param board: a newly-instantiated blank board object for creating game data for one player
    :type board: Board
    :param numberShips: the number of ships that each player will have for a game
    :type numberShips: int
    """
    for ship in range(numberShips):
        valid = False
        orientation = {'L', 'R', 'U', 'D', 'l', 'r', 'u', 'd'}
        shipLenTrack = 1
        while valid != True:
            #check for valid column input
            while True:
                start_x = input("\nWhat is the starting column of ship " + str(ship + 1) + "? (A-J)\n")
                start_x_num = (ord(start_x) % 32) - 1
                if len(start_x) == 1:
                    if start_x.isalpha() and start_x_num in range(0,10):
                        break
                    print("That's not a valid option. Please enter a letter between A through J.")
                else:
                    print("Please enter only one character.")

            #check for valid row input
            while True:
                start_y = input("\nWhat is the starting row of ship " + str(ship + 1) + "? (1-9)\n")
                if start_y.isnumeric():
                    start_y_num = int(start_y) - 1
                    if start_y_num in range(0,9):
                        break
                    else:
                        print("That's not a valid option! Please enter a number from 1 through 9.")
                else:
                    print("That's not a valid option! Please enter a number from 1 through 9.")

            #check for valid orientation
            while True:
                print_oreient_prompt()
                orientInput = input()
                orient = orientInput.upper()
                if orientInput in orientation:
                    if orient == 'L':
                        if ((ship - 1 <= start_x_num) and (start_x_num - shipLenTrack >= 0)):
                            break
                        else:
                            print("The ship will not fit here!")
                    elif orient == 'R':
                        if ((ship + start_x_num <= 10) and (start_x_num - shipLenTrack <= 10)):
                            break
                        else:
                            print("The ship will not fit here!")
                    elif orient == 'U':
                        if ((ship - 1 <= start_y_num) and (start_y_num - shipLenTrack >= 0)):
                            break
                        else:
                            print("The ship will not fit here!")
                    elif orient == 'D':
                        if ((ship + start_y_num <= 9) and (start_y_num + shipLenTrack <= 10)):
                            break
                        else:
                            print("The ship will not fit here!")
                else:
                    print("Invalid direction for ship.")
            shipLenTrack += 1
            if board.isShipValid(orient, start_x_num, start_y_num, ship + 1):
                board.createShip(start_x_num, start_y_num, orient, ship + 1, ship + 1)
                valid = True
            else:
                print("There is already a ship here, please reenter coordinates. ")
                valid = False
        
    playerCoordinates = board.getCoords() #2d Array of player coordinates 

""" method is not commented good and is hard to follow.  Doesn't lend itself to
adding a cpu player to the game
think we should implement a state machine
AMA 9-26-2021
"""



def playGame(board1, board2):
    """
    Asks players to enter the coordinates for shooting at ships,
    and then calls the board.hits method to check hits and if sunk, and
    calls the the board.score method to keep track of remaining ships.

    :param board1: the Board object created for Player 1 by setup method
    :type board1: Board
    :param board2: the Board object created for Player 2 by setup method
    :type board2: Board
    """
    turn = 1
    quit = False
    while board1.allsunk == False and board2.allsunk == False and quit == False:
        if printMenu(board1, board2, turn) == 3:
            quit = True
        else:
            #check for valid column input
            while True:
                x_hit = input("\nWhat column?\n")
                if x_hit.isalpha():
                    x_coord = (ord(x_hit) % 32) - 1
                    if x_coord in range (0, 10):
                        break
                    else:
                        print("Please enter a letter between A-J")
                else:
                    print("Please enter a valid column. (A-J)")

            #check for valid row input
            while True:
                y_hit = input("\nWhat row?\n")
                if y_hit.isnumeric():
                    y_coord = int(y_hit) - 1
                    if y_coord in range(0, 10):
                        break
                    else:
                        print("Please enter a number between 1-9.)")
                else:
                    print("Please enter a valid row. (1-9)")
                    # TODO: been trying to correct some miss match in boards below.
                    # think ist close but needs testing here
            if turn%2 == 1:
                board2.hit(y_coord,x_coord)
                board2.score(board2)
            elif turn%2 == 0:
                board1.hit(y_coord,x_coord)
                board1.score(board1)
            turn += 1

def printMenu(board1, board2, turn):
    """
    Print menu items and boards for the players.
    :param board1: board from player 1 passed in from playGame method
    :type board1: Board
    :param board2: board for player 2 passed in from playGame method
    :type board 2: Board
    :param turn: the turn number, passed in from playGame method
    :type turn: int
    """
    choice = 0
    if turn % 2 == 1:
        print("OPPONENT BOARD:")
        board2.printOpp()
        print("\nPLAYER BOARD:")
        board1.printBoard()
    elif turn % 2 == 0:
        print("OPPONENT BOARD:")
        board1.printOpp()
        print("\nPLAYER BOARD:")
        board2.printBoard()
        print("\n")
    while choice != 3:
            print("\nPlease select a menu option (1-3):")
            # Added by Edina.
            # Edina note: probably need to add in option to hide boards,
            # to prepare for next player.I don't think we can make a call
            # to terminal to hide stuff, so maybe print a long vertical
            # line of stars, to hide boards.
            print("1) Take a Shot!\n2) Read rules \n3) Quit game")

            while True:
                choice = input()
                if choice.isnumeric():
                    choice = int(choice)
                    break
                else:
                    print("Sorry, invalid choice. Please pick again.\n")
                    print("\n1) Take a Shot!\n2) Read rules \n3) Quit game")
            # """ not useable till python 3.10 release, ~oct 4, 2021
            # changed to match-case from if-else AMA 9-26-2021
            match choice:
                case 1:
                    return 1;
                case 2:
                    print_rules();
                case 3:
                    print("\nGoodbye...")
                    return 3;
                case _:
                    print("Sorry, invalid choice. Please pick again.\n")
            # """

            # if choice == 1:
            #     return(1) # return this choice to playGame and start shootin'
            # elif choice == 2:
            #     print_rules()
            # elif choice == 3:
            #     print("\nGoodbye...")
            #     return(3)
            # else:
            #     print("Sorry, invalid choice! Please pick again.\n")



def run():
    """ Starts and ends the game, calling methods as appropriate.
    """
    stopgame = 0  # variable for giving option to quit game or play again, once a game is over
    while stopgame == 0:
        
        print('\n*** WELCOME TO BATTLESHIP!! ***\n')
        isCPU, firstSelection = False, False
        print("Would you like to play against another player?\n")
        while not firstSelection:
            selection = input("Enter '1' to play against a player and '2' for CPU.\n")
            if selection.isnumeric():
                if selection == 1:
                    firstSelection = True
                elif selection == 2:
                    firstSelection, isCPU = True, True
                else:
                    print("Please enter a 1 or 2.\n")

        choice = 0  # bool for marking acceptable choice for numberShips
        while choice == 0:
            print('How many ships per player for this game?\n')
            numberShips = input('Enter a number from 1 to 6:\n')
            if numberShips.isnumeric():
                ship_num = int(numberShips)
                if ship_num in range(1, 7):
                    choice = 1
                else:
                    print("Please enter a number between 1 and 6!\n")
            else:
                print("Please enter a valid ship number.\n")

        # player 1 board object
        player1_board = Board()
        print('\nReady to set up the board for Player 1!\n')


        """ TODO: remove comment
        2 line comment below is redundant, can look at the func to see what it does and
        is in the name

        # This step runs the setup method for Player 1. The method modifies
        # the waterGrid 2D array of boardPlayer1.
        """
        setup_user(player1_board, ship_num)

        #if isCPU:
        # CPU board object
        cpu_board = Board()
        # setup CPU board

        # TODO: think need diffent func for cpu setup
        setup_user(cpu_board, ship_num);


        """ TODO: Remove when cpu is implemented
        print('\nReady to set up the board for Player 2!\n')
        # This step runs the setup method for Player 2. The method modifies
        # the waterGrid 2D array of boardPlayer2.
        setup(boardPlayer2, ship_num)
        """

        # This now starts the shooting steps, printing printMenu() between each player's shot
        playGame(player1_board, cpu_board)

        # Once playGame method ends, give players the option to play again rather than exit program.
        while True:
            print("\nWould you like to play another game?\n")
            endgame = input('Enter "Y" for yes, "N" for no:\n')
            if endgame == "N" or endgame == "n":
                stopgame = 1
                break
            elif endgame == 'Y' or endgame == 'y':
                break
            else:
                print("\nInvalid Input.")

def print_rules():
    """ removed from printMenu func for readability
    :author AMA
    :date sept 24 2021
    """
    print("--------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("-----Rules of Battleship---------------------------------------------")
    print("---------------------------------------------------------------------")
    print("-----------------------------\n")
    print("Overview:\nBattleship is a two player game where both players secretly ")
    print("place 1 to 6 ships on a 9x10 grid. Taking turns each player announces ")
    print(" where on the opponents grid they wish to fire. The opponent must ")
    print("announce whether or not one of the ships was hit. The first player to ")
    print("sink all of the oponents ships wins\n ")
    print("1) Ship size will be dependent on number of ships chosen. If one ship ")
    print("is chosen each player will be given a 1x1 ship . If two ships are ")
    print("chosen each player will be given a 1x1 and a 1x2 ship and so on.\n")
    print("2) After the ships have been chosen, players will be able to place and ")
    print("orient their ships, you may place your ship anywhere within the board ")
    print("and orient it up, down, left or right. You may not orient it diagonally ")
    print("or intersect another ship.\n")
    print("3) Taking turns, the users pick a space on the opponent's board to fire ")
    print("at,each shot must be updated to indicate a hit or miss.\n")
    print("4) Once a ship has been hit in every space it occupies, it is sunk.\n")
    print("5) As the great Colonel Sanders once said \"I'm too drunk to taste this fried chicken.\"\n ")

def print_oreient_prompt():
    """ print the user instruciton for ship direction
    :author AMA
    """
    print('What is the orientation of this ship? Enter\n')
    print('"L" for left of start (horizontal ship)\n')
    print('"R" for right of start (horizontal ship)\n')
    print('"U" for up from start (vertical ship)\n')
    print('"D" for down from start (vertical ship)\n')

"""
checks python version to see if can runs
:author AMA
:date 9-26-2021
"""
req_version = (3,10)
curr_version = sys.version_info
if curr_version >= req_version:
    run()
else:
    # prompt user to update python
    print("Please update your python version to 3.10 or greater")
