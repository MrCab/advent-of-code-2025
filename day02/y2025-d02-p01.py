import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

################################

class KrampusInventoryTaker :
    
  DEFAULT_FILE = "day02\\input02.txt"

  def __init__(self) :
       self.ranges = []
       self.DAY = 2

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
      lines = [ l.strip() for l in lines ]

    # I kept typing rangers so I stuck with it
    # sports puck
    linerangers = lines[0].split( "," )

    self.ranges = [ x.split("-") for x in linerangers ]

  #############
  def take_inventory_1( self ) :
    sum_of_invalid = 0
    for henriq in self.ranges :
      mika = int( henriq[0] )
      fox = int( henriq[1] )

      for ebug in range(mika,fox+1) :
        x = len(str(ebug))
        if x % 2 == 1 :
          continue
        g = str(ebug)
        y = int(x/2)
        if g[0:y] == g[y:] :
          sum_of_invalid += ebug
    return sum_of_invalid



###############
  def main(self) :
    self.processArguments()
    print( self.take_inventory_1() )

#######
if __name__ == "__main__":
  k = KrampusInventoryTaker()
  k.main()
