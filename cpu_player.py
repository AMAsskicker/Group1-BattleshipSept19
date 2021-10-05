
#
# """

# from Board import Board
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
        self.current_move = []
        # track the totoal moves made, for parsing previous moves
        self.total_moves = 0;
        #Difficulty for CPU with 1 for easy, 2 for med, 3 for hard. 0 gets changed by set difficulty
        self.difficulty = 1;
        self.cheat = False
        print("cpu created")

    def make_move (self, cpu_board):
        """
        Called when it is cpu turn in game. \n
        By: AMA & MT & ...

        :param cpu_board: Board object to use for making move
        :type cpu_board: Board
        :return coords: list/tuple of move to make
        :rtype: list of int, [x, y]
        """
        # check previous for a hits

        #author MT, if statement checks if cheat mode is activated, it is a little redundant now
        if self.cheat:
            print(self.opponent_coords)
            for coord in self.opponent_coords:
                if coord not in self.previous_moves:
                    move = coord
                    self.previous_moves.append(move)
                    #self.opponent_coords.pop()
                    break
            else:
                print("Empty list")
            print("Move: ", move)
            #Guess from opponent array
            #Remove guess from array
            print("Move made")
            self.total_moves += 1;
            return move #return early if cheat mode is activated

        if self.check_previous: #for medium dif
            # can prob do all these checks with one function
            #check above
            #check below
            #check left
            #check right
            #finished with this -MXO
            #TODO: Testing (works well so far however duplicate moves can be made)

            fired = False
            if self.total_moves == 0:
                x_guess = random.randrange(0,10)
                y_guess = random.randrange(0, 9)
                guess_coord = [x_guess, y_guess]
                fired = True
                print("first cpu move")
                self.total_moves += 1
                self.previous_moves.append(guess_coord)
                return guess_coord
            while not fired:
                print(self.opponent_coords)
                print(self.previous_moves[self.total_moves])

                if  self.previous_moves[self.total_moves] not in self.opponent_coords: #checks if previous move was a miss
                    #fires randomly
                    print("entering else")
                    x_guess = random.randrange(0,10)
                    y_guess = random.randrange(0, 9)
                    guess_coord = [x_guess, y_guess]
                    if guess_coord not in self.previous_moves:
                        fired = True
                        print("fired is true")
                    self.total_moves += 1
                    self.previous_moves.append(guess_coord)
                    return guess_coord
                #this goes up, down, right, left after previous move was a hit
                #once hit it will strategically destroy the ship
                #-MXO
                else:
                    x_guess, y_guess = self.previous_moves[self.total_moves]
                    print (x_guess, ", ", y_guess)
                    guess_coord = [x_guess, y_guess + 1] #fires up
                    if guess_coord not in self.previous_moves and guess_coord in self.opponent_coords:
                        fired = True
                        self.previous_moves.append(guess_coord)
                        self.total_moves += 1
                        return guess_coord
                    guess_coord = [x_guess, y_guess - 1] #fires down
                    if guess_coord not in self.previous_moves and guess_coord in self.opponent_coords:
                        fired = True
                        self.previous_moves.append(guess_coord)
                        self.total_moves += 1
                        return guess_coord
                    guess_coord = [x_guess + 1, y_guess] #fires right
                    if guess_coord not in self.previous_moves and guess_coord in self.opponent_coords:
                        fired = True
                        self.previous_moves.append(guess_coord)
                        self.total_moves += 1
                        return guess_coord
                    guess_coord = [x_guess - 1, y_guess] #fires left
                    if guess_coord not in self.previous_moves and guess_coord in self.opponent_coords:
                        fired = True
                        self.previous_moves.append(guess_coord)
                        self.total_moves += 1
                        return guess_coord
                    x_guess = random.randrange(0,10)
                    y_guess = random.randrange(0, 9)
                    guess_coord = [x_guess, y_guess]
                    fired = True
                    print("first cpu move")
                    self.total_moves += 1
                    self.previous_moves.append(guess_coord)
                    return guess_coord
            # TODO: remove later
            print("previous checked")
        # if hit look around hit for other moves
        # make move
        else:
            # if no hit, random number
            fired = False
            while not fired:
                x_guess = random.randrange(0,10)
                y_guess = random.randrange(0, 9)
                guess_coord = [x_guess, y_guess]
                if guess_coord not in self.previous_moves:
                    fired = True


            # TODO: remove later
            print("move to some random") # statifiy compiler
            self.total_moves += 1;
            return guess_coord
        # check for previous move There
        # act accordingly

        if True:
            # TODO: remove later
            print("MOVE MADE")
        # increment move
        #self.total_moves += 1;

    def check_previous (self):
        """
        checks previous move for a hit.
        By:

        :return True: if previous move was a hit
        :return False: else
        """
        boologna = False
        return boologna

    def isValid_move (self, game_board, move_2_check):
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
        Adds player 1 coordinates to array to allow for guessing. \n
        Author: Michael Talaga

        :param opp_coords: 2d array of coords
        :type opp_coords: list of int, [x, y]

        """
        self.opponent_coords = opp_coords

    def set_difficulty(self, dif):
        """
        Sets difficulty for CPU \n
        Author: Michael Talaga

        :param none
        :type dif: int
        """
        self.difficulty = dif
        if dif == 3:
            self.cheat = True
        if dif == 2:
            self.check_previous = True

    #def set_ships(self, board):
    #TODO: Can be deleted? MT
        """
        sets ships at the start of the game \n
        Author: xxx Date: xx xx xx

        :param board: Board obj to set ships in
        :type board: Board
        :return True: ships are set
        :return False: else
        """
        #boollon = False
        #return boollon

    def set_ships(self, board, numberShips):
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
        completed = False
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
        completed = True
        return completed
        #board.printBoard() #Test for CPU board
        #pause("cpu TESTING")
