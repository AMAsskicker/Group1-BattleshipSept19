"""
Board.py
"""

from ship import Ship

class Board:
    """Class for creating components of active player and opponent game boards
    and changing or checking the characteristics of the boards and displaying them.
    """

    # TODO: THEY HAVE THE BOARD GOING [Y][X], DO WE WANT TO CHANGE TO [X][Y] WHICH
    #       IS USED MORE OFFTEN IN 2D COORD SYSTEMS? - AMA
    def __init__(self):
        """Constructor method
        """
        # this is a list of ship objects. They will be checked to determine which
        # ship is hit, and update ship coord, sunk variables
        # TODO: make shipObjects a list of SHIPS -ama
        # self.shipObjects = []
        # self.shiplengths=[] # will probably remove after full ship class implement -AMA

        # this is a list of ship objects. They will be checked to determine which
        # ship is hit, and update ship coord, sunk variables
        # TODO: make shipObject
        self.shipObjects = []
        self.waterGrid = [[' ' for col in range(10)] for row in range(9)] # initialize board to be all 'O'
        self.oppGrid = [['*' for col in range(10)] for row in range(9)] # initialize board to be all '*'
        # self.spots = 0 # TODO: FIGURE OUT WHAT THIS DOES, will probably remove -AMA
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

    def checkShipOverlap(self, x, y, len, orient):
        start = 0
        for i in self.waterGrid[x]:
            for j in self.waterGrid[y]:
                if j != 'O' and j != '*':
                    print("There is already a ship here, please reenter coordinates. ")
                    return False
                else:
                    return True


    def isShipValid(self, orient, start_x, start_y, length):
        start = 0
        bool = True
        orient = orient.upper();
        checkArray = [' ', 'O', '*', '1', '2', '3', '4', '5'] # Added a check array to shorten if statements MT
        while start < length:
        # changed to match-case from if-else AMA 9-26-2021
            match orient:
            # TODO: should we start the bool as false and then change to true?
            # will be less in the if stnmt, i think
            # AMA
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
        # start = 0
        # shipcoords=[]
        # self.shiplengths.append(length)
        for start in range(length):
        # while start < length:
            match orient:
                case 'L':
                    self.waterGrid[start_y][start_x - start] = shipnumber
                    # shipcoords.append((start_y, start_x - start))
                    temp_ship.add_coord([start_x - start, start_y], shipnumber)
                case 'R':
                    self.waterGrid[start_y][start_x + start] = shipnumber
                    # shipcoords.append((start_y,start_x + start))
                    temp_ship.add_coord([start_x + start, start_y], shipnumber)
                case 'U':
                    self.waterGrid[start_y - start][start_x] = shipnumber
                    # shipcoords.append((start_y - start,start_x))
                    temp_ship.add_coord([start_x, start_y - start], shipnumber)
                case 'D':
                    self.waterGrid[start_y + start][start_x] = shipnumber
                    # shipcoords.append((start_y + start,start_x))
                    temp_ship.add_coord([start_x, start_y + start], shipnumber)
            # start += 1;
            # self.spots += 1;
        # self.shipObjects.append(shipcoords)
        # TODO:  try except here -AMA
        self.shipObjects.append(temp_ship)
        self.points += 1
        # TODO: POTENTIAL TRY EXECPT TO CHECK DELETE
        # del temp_ship

    def hit(self, coord_list: [int], compare_board):
        """
        Determines whether entered coordinates hit a ship, and gives
        feedback on whether ship is hit and if a ship is sunk.
        :edit AMA reimpmiment with ship object, some code reused
        :param coord_list: [X,Y]
        :param compare_board:
        :type compare_board: Board
        :return True: if move is a hit, false else
        """
        # TODO: NEEDS TESTING
        # TODO: WORKING, BUT COMPARING TO OWN SHIPS, NOT OPPONET SHIPS -AMA

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
                        # break
                # else:
        self.oppGrid[coord_list[1]][coord_list[0]] = 'M'
        compare_board.waterGrid[coord_list[1]][coord_list[0]] = 'M'
        print("\n MISS! \n")

        return False

        # row = len(self.shipObjects)
        # temp = self.spots
        # for z in range(row):
        #     for w in range(len(self.shipObjects[z])):
        #         # TODO: is comparing moove to its own ship placement, not opponents
        #         # AMA will fix
        #         if self.shipObjects[z][w] == (coord_list[1],coord_list[0]):
        #             self.waterGrid[coord_list[1]][coord_list[0]] = "x"
        #             self.oppGrid[coord_list[1]][coord_list[0]] = "x"
        #             self.spots -= 1
        #             self.shiplengths[z] -= 1
        #             print("\nHIT!\n")
        #             if self.shiplengths[z] == 0:
        #                 print("Ship is sunk!")
        #                 self.points -= 1
        #         else:
        #             print("\nMISS!\n")
        # if temp == self.spots:
        #     self.oppGrid[coord_list[1]][coord_list[0]] = "m"

    def score(self, opponent_board):
        """
        Keeps track of the ships remaining for each player, and
        determines when all ships are sunk for a player, and which player won
        :param opponent_board: the opponent's Board object, so it can be compared to self
        :type opponent_board: Board
        """
        print("Player 1 Ships Remaining: " + str(self.points))
        print("Player 2 Ships Remaining: " + str(opponent_board.points))
        #  MOVING TO STATE MACHINE -AMA
        # if self.points == 0:
        #     print("Player 2 Won!")
        #     self.allsunk=True
        # elif opp.points == 0:
        #     print("Player 1 Won!")
        #     opp.allsunk=True

    def getCoords(self):
        """
        Returns player coordinates
        """
        return self.shipObjects
