# Import class methods needed for the program
from Board import *
from cpu_player import CPU_Player
from user_input import User_Input
from os import system, name
# libs
import string
import sys
import random

'''
Responsible for executing the game.

edited: sept 24 2021
by: Adam Abernaty (AMA)
AMA edit: made class
AMA note: prior authors are noted in documentation/credits.txt

'''
class Battleship:
    """
    battleship game, responsible for game execution

    Example::

        battleship = Battleship()
        battleship.run()
    """
    def __init__(self):
        self.number_of_games = 0

    def setup_user(self, setup_board, numberShips):
        """
        Interacts with player to set up a board with ships for a player \n
        Pre: board objectmust have correct properties; numberShips must be in the proper range, 1 to 6
        Post: the input board object is modified according to user input \n

        :param board: a newly-instantiated blank board object for creating game data for one player
        :type board: Board
        :param numberShips: the number of ships that each player will have for a game
        :type numberShips: int
        :return True: user setup completed
        :return False: user was not setup
        """
        setup_board.printBoard() #Print blank board for reference
        shipLenTrack = 1
        for ship in range(numberShips):
            valid = False
            orientation = {'L', 'R', 'U', 'D', 'l', 'r', 'u', 'd'}
            while not valid:
                #check for valid column input
                while True:
                    start_x = input("\n What is the starting column of ship " + str(ship + 1) + "? (A-J)\n")
                    try:
                        start_x_num = (ord(start_x) % 32) - 1
                        if len(start_x) == 1:
                            if start_x.isalpha() and start_x_num in range(0, 10):
                                break
                            print("That's not a valid option. Please enter a letter between A through J.")
                        else:
                            print("Please enter only one character.")
                    except (ValueError, TypeError):
                        print("Please enter a letter between A-J")
                #check for valid row input
                while True:
                    start_y = input("\n What is the starting row of ship " + str(ship + 1) + "? (1-9)\n")
                    if start_y.isnumeric():
                        start_y_num = int(start_y) - 1
                        if start_y_num in range(0, 9):
                            break
                        else:
                            print("That's not a valid option! Please enter a number from 1 through 9.")
                    else:
                        print("That's not a valid option! Please enter a number from 1 through 9.")
                #check for valid orientation
                while True:
                    self.print_oreient_prompt_inst()
                    orientInput = input()
                    if orientInput.upper() in orientation:
                        match orientInput.upper():
                            case 'L':
                                if ((ship - 1 <= start_x_num) and (start_x_num - shipLenTrack >= 0)):
                                    break
                                else:
                                    print("The ship will not fit here!")
                            case 'R':
                                if ((ship + start_x_num <= 10) and (start_x_num + shipLenTrack <= 10)):
                                    break
                                else:
                                    print("The ship will not fit here!")
                            case 'U':
                                if ((ship - 1 <= start_y_num) and (start_y_num - shipLenTrack >= 0)):
                                    break
                                else:
                                    print("The ship will not fit here!")
                            case 'D':
                                if ((ship + start_y_num <= 9) and (start_y_num + shipLenTrack <= 9)):
                                    break
                                else:
                                    print("The ship will not fit here!")
                    else:
                        print("Invalid direction for ship.")
                if setup_board.isShipValid(orientInput, start_x_num, start_y_num, ship + 1):
                    setup_board.createShip(start_x_num, start_y_num, orientInput, ship + 1, ship + 1)
                    valid = True
                else:
                    print("There is already a ship here, please reenter coordinates. ")
                    valid = False
            shipLenTrack += 1
        # playerCoordinates = setup_board.getCoords() #2d Array of player coordinates
        return valid

    def setup_CPU(self, board, numberShips):
        """
        Generates CPU board (Designed like setup_user seen above but uses random for placement of ship) \n
        Author: Michael Talaga \n
        Pre: board object must have correct properties; numberShips must be in the proper range, 1 to 6 \n
        Post: Ships are created if the ship location and orientation satisfies the boundaries and collision requirements, and then CPU board object will have the ships included on it \n

        :param board: a newly-instantiated blank board object for creating game data for CPU
        :type board: Board
        :param numberShips: the number of ships that each player will have for a game
        :type numberShips: int
        """

        shipLenTrack = 1
        orientationArray = ['L', 'R', 'U', 'D']
        for ship in range(numberShips):
            valid, oriented = False, False

            while not valid:

                orientation = orientationArray[random.randrange(0,4)] #Choose rand orientation

                start_x_num = random.randrange(0,10) #choose rand x start point

                start_y_num = random.randrange(0, 9) #choose rand y start point

                #Orientation validation

                match orientation:
                    case 'L':
                        if (start_x_num - shipLenTrack >= 0):
                            oriented = True
                    case 'R':
                        if (start_x_num + shipLenTrack <= 10):
                            oriented = True
                    case 'U':
                        if (start_y_num - shipLenTrack >= 0):
                            oriented = True
                    case 'D':
                        if (start_y_num + shipLenTrack <= 9):
                            oriented = True

                if ((oriented) and (board.isShipValid(orientation, start_x_num, start_y_num, ship + 1))):
                    board.createShip(start_x_num, start_y_num, orientation, ship + 1, ship + 1)
                    valid = True
                else:
                    print("Calculating")
                    valid = False

            shipLenTrack += 1
        print("CPU has made selections\n")
        #board.printBoard() #Test for CPU board
        pause("cpu TESTING")

    def run(self):
        """
        Main gameplay state machine. Calls functions as needed \n
        Autor: AMA Date: sept 27 2021

        """
        run_game = True
        one_human = False
        game_state = "start"
        who_won = "none"
        # STATE MACHINE
        while run_game:
            match game_state:
                case "start":
                    print('\n*** WELCOME TO BATTLESHIP!! ***\n')
                    player1_board = Board()
                    second_board = Board()
                    cpu_obj = CPU_Player()
                    user_input = User_Input()
                    if self.is_cpu():
                        one_human = True
                    game_state = "set_ships"
                case "set_ships":
                    total_ships = user_input.get_num_ships()
                    print("\n TIME FOR PLAYER 1 TO PLACE THEIR SHIPS \n")
                    if self.setup_user(player1_board, total_ships):
                        player1_board.printBoard()
                        print("\n PLAYER 1 HAS SETUP THEIR SHIPS \n")
                        self.clear_screen_2_continue("player1")
                    else:
                        print("\n SHIP PLACE ERROR \n")
                        game_state = "end_game"
                        who_won = "ship_error"
                    # self.clear_screen()
                    if one_human:
                        print("\n CPU PLACING SHIPS \n")
                        cpu_obj.set_ships(second_board, total_ships)
                        print("CPU Ships Placed")
                    else:
                        print("\n TIME FOR PLAYER 2 TO PLACE THEIR SHIPS \n")
                        if self.setup_user(second_board, total_ships):
                            second_board.printBoard()
                            print("\n PLAYER 2 HAS SETUP THEIR SHIPS \n")
                        else:
                            print("\n SHIP PLACE ERROR \n")
                            game_state = "end_game"
                            who_won = "ship_error"
                    self.clear_screen_2_continue("player2")
                    game_state = "player1"
                case "player1":
                    if self.printMenu(player1_board, second_board, game_state) == 3:
                        who_won = "user_exit"
                        game_state = "end_game"
                        continue
                    else:
                        player1_board.hit(user_input.get_move_coord(), second_board)
                    self.print_current_board(player1_board, second_board, game_state)
                    player1_board.score(second_board)
                    if player1_board.allsunk:
                        who_won = "player1"
                        game_state = "end_game"
                    else:
                        game_state = "player2"
                        self.clear_screen_2_continue(game_state)

                case "player2":
                    if one_human:
                        second_board.hit(cpu_obj.make_move(second_board), player1_board)
                        print("CPU HAS MADE A MOVE")
                    else:
                        if self.printMenu(player1_board, second_board, game_state) == 3:
                            who_won = "user_exit"
                            game_state = "end_game"
                            continue
                        else:
                            second_board.hit(user_input.get_move_coord(), player1_board)
                    self.print_current_board(player1_board, second_board, game_state)
                    second_board.score(player1_board)
                    if second_board.allsunk:
                        who_won = "cpu" if one_human else "player2"
                        game_state = "end_game"
                    else:
                        game_state = "player1"
                        self.clear_screen_2_continue(game_state)
                case "end_game":
                    self.number_of_games += 1
                    self.announce_winner(who_won)
                    if user_input.play_again():
                        del player1_board, second_board, cpu_obj
                        try:
                            print(cpu_obj.difficulty)
                        except (NameError):
                            game_state = "start"
                            who_won = "none"
                    else:
                        del player1_board, second_board, cpu_obj
                        run_game = False

    def printMenu(self, board1, board2, turn):
        """
        Print menu items and boards for the players. \n
        Edit AMA: changed if else to match to use state machine

        :param board1: board from player 1 passed in from playGame method
        :type board1: Board
        :param board2: board for player 2 passed in from playGame method
        :type board2: Board
        :param turn: the turn number, passed in from playGame method
        :type turn: int
        """
        choice = 0
        self.print_current_board(board1, board2, turn)
        # print("\n")
        while choice != 3:
                print("\n Please select a menu option (1-3):")
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

    def print_rules(self):
        # removed from printMenu func for readability -AMA
        """
        Prints rules for user \n
        Author: AMA Date: sept 24 2021
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

    def print_oreient_prompt_inst(self):
        """ print the user instruciton for ship direction \n
        Author: AMA Date: sept 24 2021
        """
        print('What is the orientation of this ship? Enter\n')
        print('"L" for left of start (horizontal ship)\n')
        print('"R" for right of start (horizontal ship)\n')
        print('"U" for up from start (vertical ship)\n')
        print('"D" for down from start (vertical ship)\n')

    def pause(self, prompt):
        """
        Pauses game until something is typed \n
        Author: Michael & AMA (overload)

        :param prompt: what message to print at input
        :type prompt: string
        """
        waited = False
        while not waited:
            wait = input(prompt)
            if len(wait) >= 1 or wait == "":
                waited = True
        return (print("\nContinuing...\n"))

    def is_cpu(self):
        """
        ask if using cpu as second player \n
        Author: MXO

        :return True: if using cpu
        :return False: else
        """
        while True:
            playCPU = input("Play against CPU? Y/N: ")
            if playCPU == 'Y' or playCPU == 'y':
                return True
            elif playCPU == 'N' or playCPU == 'n':
                return False
            else:
                print("\nInvalid Input")

    def clear_screen_2_continue(self, turn):
        """
        clears screen and prints message to user \n
        Autor: AMA

        :param turn: whos turn just finished
        :type turn: string
        """
        output = "PLAYER 1'S TURN" if turn == "player2" else "PLAYER 2/CPU'S TURN"
        self.pause("PRESS ENTER TO CLEAR THE SCREEN BEFORE " + output)
        self.clear_screen()
        self.pause("PRESS ENTER TO START " + output)

        # prompt user to press enter to continue next players turn

    def announce_winner(self, who_2_announce):
        """
        outputs the winner \n
        Author: MXO

        :param who_2_announce: who won: player1, player2, cpu, user_exit
        :type who_2_announce: string
        """
        print("The winner is: ", who_2_announce)
        #print(who_2_announce)

    def clear_screen(self):
        """
        clears terminal/screen window to not show other players board \n
        Author: MXO
        """
        #this clears the terminal window right to the point to not show the other players board -MXO
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

        print("\n")

    def print_current_board(self, board1, board2, turn):
        # moved code from printMenu func -AMA
        """
        prints the current boards on the screen

        :param board1: Board object holding moves to print
        :type board1: Board
        :param board2: Board object holding moves to print
        :type board2: Board
        :param turn: active turn player
        :type turn: string
        """
        match turn:
            case "player1":
                print("     OPPONET/MOVES MADE BOARD:")
                board1.printOpp()
                print("\n         PLAYER 1 BOARD:")
                board1.printBoard()
                # print("\n")
            case "player2":
                print("         OPPONENT BOARD:")
                board2.printOpp()
                print("\n         PLAYER 2/CPU BOARD:")
                board2.printBoard()
                # print("\n")



"""
checks python version to see if can run game
:author AMA
:date 9-26-2021
"""
req_version = (3,10)
curr_version = sys.version_info
if curr_version >= req_version:
    if __name__ == '__main__':
    #     #*** Instantiate the ExampleModule class:
    #     example_module = ExampleModule()
    #     #*** Start ExampleModule:
    #     example_module.run()

        battleship = Battleship()
        battleship.run()
    # if version is compatable, start the game
    # run()
    # del battleship
else:
    # prompt user to update python
    print("Please update your python version to 3.10 or greater")
