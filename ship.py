"""
ship.py

by; Adam Abernathy (AMA)
date: sept 30 2021
"""

import string

"""
ship object for battleship

"""
class Ship(object):
    """
    Ship object that is placed on game board. stores the x,y coords and if has been hit

    Example::

        ship = Ship()
        ship._(_)

    :param ship_num: number to assign to ship
    :type ship_num: int 
    :param current_value: state of square of ship to assign
    """
    def __init__(self, ship_num, direction):
        self.ship_num = ship_num
        self.direction = direction
        self.coord_list = [] # list of [x: int,y: int,current: chr]

    def add_coord(self, coords, current_value: chr):
        """
        append to coord_list

        :param coords: coords of square to change
        :type coords: list of int
        :param current_value: new value to pass
        :type current_value: chr

        :return True: if succsesful
        :return False: else
        """
        temp = [coords[0], coords[1], current_value]
        try:
            self.coord_list.append(temp)
            return True
        except IndexError:
            return False

    def get_coord(self, position: int):
        """
        get coords

        :param position: square of ship, ie ship 2 has 0,1 coords
        :type position: int
        """
        return [self.coord_list[position][0], self.coord_list[position][1]]

    def change_current(self,coords: [int], new_current: chr):
        """
        changes the stored value of current, ie has been hit

        :param coords: coords of "square" to change
        :return True: if operation was valid
        :return False: operation was unsuccessful
        """
        for square in range(self.ship_num):
            if self.coord_list[square][0] == coords[0]:
                if self.coord_list[square][1] == coords[1]:
                    self.coord_list[square][2] = new_current
                    return True
        return False

    def is_sunk(self, control: int):
        """
        checks if ship is sunk

        :param control: control for recursive
        :type control: int
        :return True: if all current is 'X', false else
        """
        if control == self.ship_num:
            return True
        if self.coord_list[control][2] == 'X':
            if self.is_sunk(control + 1):
                return True
        return False

    def get_current(self, coord):
        """
        returns current value of this ship square

        :param coord: list of x, y coords
        :type coord: [int]
        :return chr of current ship space
        """
        for square in range(self.ship_num):
            if self.coord_list[square][0] == coord[0]:
                if self.coord_list[square][1] == coord[1]:
                    return self.coord_list[square][2]

    def get_num(self):
        """
        return ship number

        :return ship_num
        """
        return self.ship_num
