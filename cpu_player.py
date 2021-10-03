
#
# """

from Board import Board
import random

"""
cpu_player.py

created: sept 25 2021
by: Adam Abernathy

description:
cpu player for battleship
cpu to play against user, contains all the actions of a cpu in the game
"""
class CPU_Player :
    """
    cpu object used to decide moves for battleship

    Example::
        cpu_obj = CPU_Player()
        cpu_obj._(_)
    """
    def __init__ (self):
        # list of tuples of previous moves: (x, y)
        # MAY NOT NEED THIS AS BOARD CAN TRACK MOVES - AMA
        self.previous_moves = []
        #Keep coordinates for player 1
        self.opponent_coords = []
        self.previous_moves.append((99, 99));
        self.current_move = (99, 99);
        # track the totoal moves made, for parsing previous moves
        self.total_moves = 0;
        #Difficulty for CPU with 1 as default for easy (2 for med, 3 for hard)
        self.difficulty = 1;
        self.cheat = False
        print("cpu created")

    def make_move (self, cpu_board: Board):
        """ called when it is cpu turn in game.
        By: AMA & MT & ...

        :param cpu_board: Board object to use for making move
        :type cpu_board: Board
        :return coords: list/tuple of move to make
        :rtype: list of int
        """
        # check previous for a hits

        #author MT, if statement checks if cheat mode is activated
        if self.cheat:
            #Guess from opponent array
            #Remove guess from array
            print("Move made")


        if check_previous():
            # can prob do all these checks with one function
            #check above
            #check below
            #check left
            #check right

            # TODO: remove later
            print("previous checked")

        # if hit look around hit for other moves
        # make move
        else:
            # if no hit, random number
            # TODO: remove later
            print("move to some random") # statifiy compiler
        # check for previous move There
        # act accordingly

        if True:
            # TODO: remove later
            print("MOVE MADE")
        # increment move
        self.total_moves += 1;


    def check_previous (self):
        """
        checks previous move for a hit.
        By:

        :return True: if previous move was a hit
        :return False: else
        """
        boologna = True
        return boologna;

    def isValid_move (self, game_board: Board, move_2_check):
        """
        checks if a move has been made to space passed
        By:

        :param game_board: Board object to check move against
        :type game_board: Board
        :param move_2_check: list, x,y fomat to check
        :type move_2_check: list of int
        :return True: if move is valid
        :return False: else
        """
        booliever = True
        return booliever

    def add_opponent_coords(self, opp_coords):
        """
        Adds player 1 coordinates to array to allow for guessing.
        By: Michael Talaga

        :param opp_coords: 2d array of coords
        :type opp_coords: list of int

        """
        self.opponent_coords.append(opp_coords)

    def set_difficulty(self, dif):
        """
        Sets difficulty for CPU
        By: Michael Talaga

        :param dif: integer from 1-3

        """
        self.difficulty = dif
	#TODO: Will later change this as instructions state medium difficulty is only different from easy based on if a ship has been hit
	#Will likely change this to a boolean to indicate if the CPU will cheat or not for the hard difficulty
        if dif == 2:
            self.cheat_percentage = 15
        elif dif == 3:
            self.cheat_percentage = 100

    def set_ships(self, board: Board):
        """
        sets ships at the start of the game
        :author
        :pre
        :post
        :param board: Board obj to set ships in
        :return :True ships are set, false else
        """
        boollon = False
        return boollon
