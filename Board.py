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
    """
    def __init__(self):
        # list of ships placed by user
        self.shipObjects = []
# TODO: WHAT DO WE WANT THE BOARD TO BE?
#  THE 'O' WAS REALLY BUSY -AMA
        # initialize board to be all ' '
        self.waterGrid = [[' ' for col in range(10)] for row in range(9)]
        # initialize board to be all '*'\
        self.oppGrid = [['*' for col in range(10)] for row in range(9)]
        self.points = 0
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
        because it uses the oppGrid 2D array for printing data.
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
                print(self.oppGrid[row][col], " ", end = "")
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
        start = 0
        bool = True
        orient = orient.upper();
        # Added a check array to shorten if statements MT
        checkArray = [' ', 'O', '*', '1', '2', '3', '4', '5']
        while start < length:
        # changed to match-case from if-else AMA 9-26-2021
            match orient:
                case 'L':
                    if self.waterGrid[start_y][start_x - start] not in checkArray:
                        bool = False
                case 'R':
                    if self.waterGrid[start_y][start_x + start]not in checkArray:
                        bool = False
                case 'U':
                    if self.waterGrid[start_y - start][start_x] not in checkArray:
                        bool = False
                case 'D':
                    if self.waterGrid[start_y + start][start_x] not in checkArray:
                        bool = False
            start += 1
        return bool

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
# TODO: HAVE ERROR WHERE CAN MAKE MOVE TO SAME SPOT OVER AND OVER -AMA WILL FIX
        for ship in range(len(compare_board.shipObjects)):
            control = compare_board.shipObjects[ship].get_num()
            for square in range(control):
                if compare_board.shipObjects[ship].get_coord(square) == coord_list:
                    if compare_board.shipObjects[ship].get_current(coord_list) == control:
                        compare_board.shipObjects[ship].change_current(coord_list, 'X')
                        self.oppGrid[coord_list[1]][coord_list[0]] = 'X'
                        compare_board.waterGrid[coord_list[1]][coord_list[0]] = 'X'
                        print("\n HIT! \n")
                        if compare_board.shipObjects[ship].is_sunk(0):
                            print("Ship is sunk!")
                            self.points -= 1
                            self.allsunk = True if self.points == 0 else False
                        return True
        self.oppGrid[coord_list[1]][coord_list[0]] = 'M'
        compare_board.waterGrid[coord_list[1]][coord_list[0]] = 'M'
        print("\n MISS! \n")
        return False

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
        Returns player coordinates as 2d array
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
