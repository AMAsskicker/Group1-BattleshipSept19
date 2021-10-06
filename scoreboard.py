# import files
import sys

'''
scoreboard.py

By: Adam Abernathy
Date: oct 5 2021

description:
'''
class Scoreboard(object):
    """
    Scoreboard class for use in battleship. will print only values passed

    Example::

        scoreboard = Scoreboard()
        scoreboard.printScoreboard(_)
    """
    def __init__(self):
        super(Scoreboard, self).__init__()

    def __str__(self):
        # self.printScoreboard(True, 1, 2, 3, 4, 5, 6, 7, 8)
        # self.printScoreboard(True, 1, 12, 11, 14, 2, 16, 17, 18)
        # self.printScoreboard(True, 1, 2, 13, 4, 6, 16, 7, 18)
        self.printScoreboard(False, 1, 12, 3, 14, 6, 6, 17, 8)

    def printScoreboard(self, is_cpu, p1_ships, p1_hits, p1_shots, p1_games,
                        p2_ships, p2_hits, p2_shots, p2_games):
        # TODO: read a board & battleship object
        """
        prints the whole scoreboard, calls functions as needed

        :param is_cpu: true if cpu player
        :type is_cpu: bool
        :param p1_ships: player 1 Remaining ships
        :type p1_ships: int
        :param p1_hits: player 1 total hits
        :type p1_hits: int
        :param p1_shots: player 1 total shots taken
        :type p1_shots: int
        :param p1_games: player 1 total games won
        :type p1_games: int
        :param p2_ships: player 2 Remaining ships
        :type p2_ships: int
        :param p2_hits: player 2 total hits
        :type p2_hits: int
        :param p2_shots: player 2 total shots taken
        :type p2_shots: int
        :param p2_games: player 2 total games won
        :type p2_games: int
        """
        self.print_top_bot()
        print(self.print_player(is_cpu))
        print(" || Ships Remaining  "+str(p1_ships)+" | | Ships Remaining  "+str(p2_ships)+" ||")
        print(self.format_hits(p1_hits, p2_hits))
        print(self.format_shots(p1_shots, p2_shots))
        print(self.format_games(p1_games, p2_games))
        self.print_top_bot()

    def format_hits(self, p1_h, p2_h):
        """
        :param p1_h: player 1 total hits
        :type p1_h: int
        :param p2_h: player 2 total hits
        :type p2_h: int
        :meta private:
        """
        if p1_h < 10:
            p1_out = " || Hits             " + str(p1_h)
        else:
             p1_out = " || Hits            " + str(p1_h)
        if p2_h < 10:
            p2_out = " | | Hits             " + str(p2_h) + " ||"
        else:
            p2_out = " | | Hits            " + str(p2_h) + " ||"
        return p1_out + p2_out

    def format_shots(self, p1_s, p2_s):
        """
        :param p1_s: player 1 total shots taken
        :type p1_s: int
        :param p2_s: player 2 total shots taken
        :type p2_s: int
        :meta private:
        """
        if p1_s < 10:
            p1_out = " || Shots Taken      " + str(p1_s)
        else:
            p1_out =  " || Shots Taken     " + str(p1_s)
        if p2_s < 10:
            p2_out = " | | Shots Taken      " + str(p2_s) + " ||"
        else:
            p2_out = " | | Shots Taken     " + str(p2_s) + " ||"
        return p1_out + p2_out


    def format_games(self, p1_g, p2_g):
        """
        :param p1_g: player 1 total games won
        :type p1_g: int
        :param p2_g: player 2 total games won
        :type p2_g: int
        :meta private:
        """
        if p1_g < 10:
            p1_out = " || Games Won        " + str(p1_g)
        else:
            p1_out = " || Games Won       " + str(p1_g)
        if p2_g < 10:
            p2_out = " | | Games Won        "+str(p2_g)+" ||"
        else:
            p2_out = " | | Games Won       "+str(p2_g)+" ||"
        return p1_out + p2_out

    def print_player(self, is_cpu):
        """
        :param is_cpu: true if cpu player
        :type is_cpu: bool

        :return _: string of player banner
        :rtype: string
        :meta private:
        """
        out1 = " ||     player 1       | |       cpu          ||"
        out2 = " ||     player 1       | |     player 2       ||"
        return out1 if is_cpu else out2


    def print_top_bot(self):
        """ prints top and bot of scoreboard

        :meta private:
        """
        print("   - - - - - - - - - - - - - - - - - - - - - - ")

req_version = (3,10)
curr_version = sys.version_info
if curr_version >= req_version:
    if __name__ == '__main__':
    #     #*** Instantiate the ExampleModule class:
    #     example_module = ExampleModule()
    #     #*** Start ExampleModule:
    #     example_module.run()

        test = Scoreboard()
        print(test)
        # test.printScoreboard(True, 1, 2, 3, 4, 5, 6, 7, 8)

    # if version is compatable, start the game
    # run()
    # del battleship
else:
    # prompt user to update python
    print("Please update your python version to 3.10 or greater")
