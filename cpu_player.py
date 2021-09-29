"""
cpu_player.py

created: sept 25 2021
by: Adam Abernathy

description:
cpu player for battleship

"""

import random

class CPU_Player :
    # MARK: Properties
    # list of tuples of previous moves: (x, y)
    previous_moves = []
    #Keep coordinates for player 1
    opponent_coords = []
    
    """ defalut constructor
    :pre
    :post
    """
    def __init__ (self):
        self.previous_move.append((f, f));
        self.current_move = (f, f);
        # track the totoal moves made, for parsing previous moves
        self.total_moves = 0;
        #Difficulty for CPU with 1 as default for easy (2 for med, 3 for hard)
        self.difficulty = 1;
        self.cheat = False
        print("cpu created")

    """ called when it is cpu turn in game
    :pre
    :post
    """
    def make_move (self):
        # check previous for a hits
        
        #author MT, if statement checks if cheat mode is activated
        if self.cheat:
            #Guess from opponent array
            #Remove guess from array
            print("Move made")
        
        
        if check_previous():
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

    """ checks previous move for a hit
    """
    def check_previous (self):
        return True;
    
    """ checks if a move has been made to space passed
    :pre
    :post
    :param move_2_check: tuple, x,y fomat to check
    """
    def isValid_move (move_2_check):
        return True;


    """ Adds player 1 coordinates to array to allow for guessing
    :pre
    :post
    :param opp_coords: 2d array of coords
    :author Michael Talaga
    """
    def add_opponent_coords(self, opp_coords):
        
        self.opponent_coords.append(opp_coords)

    """ Sets difficulty for CPU
    :pre 
    :post 
    :param dif: integer from 1-3
    :author Michael Talaga
    """  
    def set_difficulty(self, dif):
        self.difficulty = dif
        if dif == 3:
            self.cheat = True
            
        
