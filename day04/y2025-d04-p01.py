import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

################################

class ForkLiftSweeper :
    
  DEFAULT_FILE = "day04\\input04.txt"
  #DEFAULT_FILE = "day04\\sample04.txt"

  def __init__(self ) :
       self.grid = []
       self.DAY = 4

  ##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2025 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=True )

    args = parser.parse_args()

    DebugPrinter.verbose = args.verbose

    # process the input file
    self.readInput( args.input )

  ##############
  def readInput( self, fileName ) :
    lines = []
    with open( fileName, 'r') as foo :
      lines = foo.readlines()
      lines = [ list(l.strip()) for l in lines ]

    self.grid = lines

  ############

  def rollup1( self, maxrolls ) :
    rolls = 0
    y = 0
    while y < len( self.grid ) :
      x = 0
      while x < len( self.grid[y] ) :
        if self.grid[y][x] == '@' and self.roll_for_contact( y, x ) < maxrolls :
            rolls += 1
        x += 1
      y += 1
    print(rolls)

  ############

  def rollup2( self, maxrolls, nulldot ) :
    rolls = 0
    y = 0
    while y < len( self.grid ) :
      x = 0
      while x < len( self.grid[y] ) :
        if self.grid[y][x] == '@' and self.roll_for_contact( y, x ) < maxrolls :
            rolls += 1
            self.grid[y][x] = nulldot
        x += 1
      y += 1
    return(rolls)


###############
  
  def roll_for_contact( self, y, x ) :
    contacts = 0
    for i in range( y-1, y+2) :
      for j in range(x-1, x+2 ) :
        if self.check_pos(i, j, 'X@') :
          contacts += 1
    return contacts-1 # this should always count itself, so removve that


##############
  def check_pos( self, y, x, target ) :
    if y >=0 and y < len( self.grid ) and x >= 0 and x < len( self.grid[y]) :
      return self.grid[y][x] in target
    else:
      return False

###############
  def main(self) :
    self.processArguments()
    self.rollup1(4)

    self.orig = self.grid
    rolls2=0
    x = self.rollup2(4,".")
    while x  > 0:
      rolls2 += x
      x = self.rollup2(4,".")
    print( rolls2 )
    # in theory reset lines here

#######
if __name__ == "__main__":
  n = ForkLiftSweeper()
  n.main()
