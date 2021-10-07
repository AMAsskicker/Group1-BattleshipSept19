Accounting:
          9/20  9/21  9/22  9/23  9/24  9/25  9/26  9/27  9/28  9/29  9/30  10/1  10/2  10/3  10/4  10/5  10/6  10/7  10/8  10/9  10/10
Adam:			     1     1		5	    3     3     3    0.5    6     1
Divya:
Mason:
Michael:			   0.5          5					 3.5                    0.2
Morgan:     .5                                                                      2     1

Estimate of person-hours: 40
  The reason why we guessed that the project completion would take us 40 hours is because Project 1 took about 40 hours. Although this is project is less of a monumental burden (a.k.a. starting from scratch to build a several hundred lined code), we still need to factor in time to understand and interpret the previous group's code, add two major elements, and make a seamless transition between the previous group's code and ours.
  
Design Paradigm:  
  We think the Project 1 team used function-oriented design in their code. When looking through the Project 1 repo, we noticed a lot of function definitions (initialized by "def" in Python) such as "setup", "playGame", and "run" in Battleship-G1.py, which tells us this is function-oriented. Function-oriented design requires that the code be split up into components defined by their respective function, and we found plenty of examples of components being defined as functions. For example, an important component of Project 1 is to have a clean display of the current Battleship board. Group 1 makes "printBoard" it's own function, housing a 2D array to print data, as well as several smaller functions to set up the column and row headers. Python is known to support function-oriented programming, so we also see a justification as to what language they used, although we don't know what came first--the chicken (language) or the egg (design paradigm)!

          In addition to function-oriented design, we think Group 1 also properly utilized top-down functional decomposition. We could tell they took the "bigger picture" (aka the game of Battleship) and broke it into pieces, the board and the gameplay. Then, as they went through the requirements assigned to us via function-oriented design, they used aspect-oriented design to patch holes and create functions that improved multiple issues at once. We believe the function "isShipValid" stemmed from aspect-oriented design, as it solves multiple problems regarding the validity of ship placement, both in the beginning and during gameplay. We think Group 1 did a good job of using multiple design paradigms to create a functional code that we are excited to build upon!
