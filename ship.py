"""
ship.py

by; Adam Abernathy (AMA)
date: sept 30 2021
"""

import string

"""
ship object for battleship

"""
class Ship :
    """docstring for Ship."""
    coord_list = [] # list of [x: int,y: int,current: chr]

    def __init__(self, ship_num: int, direction):
        """ defalut constructor
        """
        self.ship_num = ship_num
        self.direction = direction

    def add_coord(self, coords: [int, int], current_value: chr):
        """
        append to coord_list
        :pre none
        :return True: if succsesful, false else
        """
        temp = [coords[0], coords[1], current_value]
        try:
            self.coord_list.append(temp)
            return True
        except IndexError:
            return False

    def get_coord(self, position: int):
        """
        return ship coords
        :pre
        :post
        :return coords in [x, y] format
        """
        # coord_return = [self.coord_list[position][0], self.coord_list[position][1]]
        return [self.coord_list[position][0], self.coord_list[position][1]]

    def change_current(self,coords: [int], new_current: chr):
        """
        changes the stored value of current, ie has been hit
        :pre
        :post
        :return True: if operation was valid, false else
        """
        for square in range(self.ship_num):
            if self.coord_list[square][0] == coords[0]:
                if self.coord_list[square][1] == coords[1]:
                    self.coord_list[square][2] = new_current
                    return True
        return False

    def is_sunk(self, control: int):
        """ checks if ship is sunk
        :pre
        :post
        :return True: if all current is 'X', false else
        """
        if control == self.ship_num:
            return True
        if self.coord_list[control][2] == 'X':
            if self.is_sunk(control + 1):
                return True
        return False

    def get_current(self, coord: [int]):
        """ returns current value of this ship square
        :pre
        :post
        :return chr of current ship space
        """
        for square in range(self.ship_num):
            if self.coord_list[square][0] == coord[0]:
                if self.coord_list[square][1] == coord[1]:
                    return self.coord_list[square][2]

    def get_num(self):
        return self.ship_num
