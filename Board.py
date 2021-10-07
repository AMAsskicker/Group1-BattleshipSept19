# """
# Board.py
# """

from ship import Ship

class Board:
    """Class for creating components of active player and opponent game boards
    and changing or checking the characteristics of the boards and displaying them.

    Example::

        some_board = Board()
        some_board._(_)

    :param shipObjects: ``Ships`` placed by user/cpu
    :type shipObjects: Ship
    :param waterGrid: 2D player ships & opponent guess here
    :type waterGrid: list of list
    :param guess_grid: 2D player guess here
    :type guess_grid: list of list
    :param points: number ships remaining
    :param total_guess: total shots taken
    :type total_guess: int
    :param hits: total hits in game
    :type hits: int
    :param allsunk: True: all ships sunk, False: else
    :type allsunk: bool
    """
    def __init__(self):
        # list of ships placed by user
        self.shipObjects = []
# TODO: WHAT DO WE WANT THE BOARD TO BE?
#  THE 'O' WAS REALLY BUSY -AMA
        # initialize board to be all ' '
        self.waterGrid = [[' ' for col in range(10)] for row in range(9)]
        # initialize board to be all '*'\
        self.guess_grid = [['*' for col in range(10)] for row in range(9)]
        self.points = 0
        self.hits = 0
        self.total_guess = 0
        self.allsunk = False

    def printBoard(self):
        """
        Prints the active player's game board with a border to mark coordinates
        (A-J for columns and 1-9 for rows). The printed board shows all the ships
        because it uses the waterGrid 2D array for printing data.
        """
        topOfBoard = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        # print top of board
        for i in topOfBoard:
            print(" ", end="")
            print(i, "", end = "")
        print()
        # print the rest of the board
        for row in range(9):
            print(row+1, " ", end = " ")
            for col in range(10):
                print(self.waterGrid[row][col], " ", end = "")
            print()

    def printOpp(self):
        """
        Prints the opponent player's game board with a border to mark coordinates
        (A-J for columns and 1-9 for rows). The printed board hides all the ships
        because it uses the guess_grid 2D array for printing data.
        """
        topOfBoard = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        # print top of board
        for i in topOfBoard:
            print(" ", end="")
            print(i, "", end = "")
        print()
        # print the rest of the board
        for row in range(9):
            print(row+1, " ", end = " ")
            for col in range(10):
                print(self.guess_grid[row][col], " ", end = "")
            print()

    # def checkShipOverlap(self, x, y, len, orient):
    #     # THIS FUNC ISN'T USED-AMA
    #     start = 0
    #     for i in self.waterGrid[x]:
    #         for j in self.waterGrid[y]:
    #             if j != 'O' and j != '*':
    #                 print("There is already a ship here, please reenter coordinates. ")
    #                 return False
    #             else:
    #                 return True

    def isShipValid(self, orient, start_x, start_y, length):
        """
        checks if ship placement is valid

        :param orient: direction of ship relative to first ``square``
        :type orient: chr
        :param start_x: first x coord of ship
        :type start_x: int
        :param start_y: first y coord of ship
        :type start_y: int
        :param length: length of the ship to check
        :type length: int

        :return True: if placement is valid
        :return False: if invalid placement
        """
        bool_rtn = True
        orient = orient.upper();
        # Added a check array to shorten if statements MT
        checkArray = [' ', 'O', '*', '1', '2', '3', '4', '5', 6]
        for start in range(length):
            try:
                # changed to match-case from if-else AMA 9-26-2021
                match orient:
# TODO: maybe FIXED: need to test more.  added try except for the match statement,
# was getting an index error.  also change to for loop
# TODO: NEEDS MORE TESTING TO SEE IF ANY OF MY FIXES BROKE SOMETHING ELSE. -AMA
                    case 'L':
                        if self.waterGrid[start_y][start_x - start] not in checkArray:
                            bool_rtn = False
                    case 'R':
                        if self.waterGrid[start_y][start_x + start] not in checkArray:
                            bool_rtn = False
                    case 'U':
                        if self.waterGrid[start_y - start][start_x] not in checkArray:
                            bool_rtn = False
                    case 'D':
                        if self.waterGrid[start_y + start][start_x] not in checkArray:
                            bool_rtn = False
            except (IndexError):
                bool_rtn = False
        return bool_rtn

    def createShip(self, start_x, start_y, orient, length, shipnumber):
        """
        Creates a ship object to place on a game board.

        :param start_x: the column index in 2D array for start position for placing a ship
        :type start_x: int
        :param start_y: the row index in a 2D array for start position for placing a ship
        :type start_y: int
        :param orient: the orientation from the start position for building a ship
        :type orient: string
        :param length: the size of a ship
        :type length: int
        :param shipnumber: the number label used as a symbol to indicate a ship
        :type shipnumber: int
        """
        orient = orient.upper();
        # making ship class obj
        temp_ship = Ship(shipnumber, orient)
# TODO: NEEDS TESTING -AMA
        for start in range(length):
            match orient:
                case 'L':
                    self.waterGrid[start_y][start_x - start] = shipnumber
                    temp_ship.add_coord([start_x - start, start_y], shipnumber)
                case 'R':
                    self.waterGrid[start_y][start_x + start] = shipnumber
                    temp_ship.add_coord([start_x + start, start_y], shipnumber)
                case 'U':
                    self.waterGrid[start_y - start][start_x] = shipnumber
                    temp_ship.add_coord([start_x, start_y - start], shipnumber)
                case 'D':
                    self.waterGrid[start_y + start][start_x] = shipnumber
                    temp_ship.add_coord([start_x, start_y + start], shipnumber)
        # TODO:  try except here -AMA
        self.shipObjects.append(temp_ship)
        self.points += 1
        # TODO: POTENTIAL TRY EXECPT TO CHECK DELETE and return a bool
        del temp_ship

    def hit(self, coord_list, compare_board):
        """
        Determines whether entered coordinates hit a ship, and gives
        feedback on whether ship is hit and if a ship is sunk. \n
        AMA Edit: reimpmiment with ship object, some code reused

        :param coord_list: [X,Y]
        :type coord_list: list of int
        :param compare_board: Board object to check ship placement vs move
        :type compare_board: Board
        :return True: if move is a hit
        :return False: else
        """
# TODO: WORKING,  NEEDS LOTS of TESTING -AMA
# FIXED: move in same space, NEEDS MORE TESTING -AMA
# ADDED: hit and total guess tracking, NEEDS MORE TESTING -AMA
        test_case = {'X', 'M'}
        if self.guess_grid[coord_list[1]][coord_list[0]] in test_case:
            # print("ALREADY MADE MOVE THERE")
            return False
        for ship in range(len(compare_board.shipObjects)):
            control = compare_board.shipObjects[ship].get_num()
            for square in range(control):
                if compare_board.shipObjects[ship].get_coord(square) == coord_list:
                    if compare_board.shipObjects[ship].get_current(coord_list) == control:
                        compare_board.shipObjects[ship].change_current(coord_list, 'X')
                        self.guess_grid[coord_list[1]][coord_list[0]] = 'X'
                        compare_board.waterGrid[coord_list[1]][coord_list[0]] = 'X'
                        self.hits += 1
                        self.total_guess += 1
                        print("\n HIT! \n")
                        if compare_board.shipObjects[ship].is_sunk(0):
                            print("Ship is sunk!")
                            self.points -= 1
                            self.allsunk = True if self.points == 0 else False
                        return True
        self.guess_grid[coord_list[1]][coord_list[0]] = 'M'
        compare_board.waterGrid[coord_list[1]][coord_list[0]] = 'M'
        self.total_guess += 1
        print("\n MISS! \n")
        return True

    def score(self, opponent_board):
        """
        Keeps track of the ships remaining for each player, and
        determines when all ships are sunk for a player, and which player won

        :param opponent_board: the opponent's Board object, so it can be compared to self
        :type opponent_board: Board
        """
        print("\n Player 1 Ships Remaining: " + str(self.points))
        print(" Player 2 Ships Remaining: " + str(opponent_board.points))

    def getCoords(self):
        """
        Author MT
        :return _: players ship coordinates as 2d array
        :rtype: list of coords
        """
        coordinates = []
        workingCoord = []
        for ship in self.shipObjects:
            coords = ship.get_raw_coords()
            for coord in coords:
                workingCoord = coord
                coordinates.append(workingCoord)
                #print(workingCoord)
        return coordinates
