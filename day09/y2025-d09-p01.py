import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

################################

class BdubsTheLegendaryRedStoner :
    
  DEFAULT_FILE = "day09\\input09.txt"
  #DEFAULT_FILE = "day09\\sample09.txt"

  def __init__(self ) :
       self.redBlocks = {}
       self.candyCaneDust = []
       self.DAY = 9

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
      lines = [ l.strip().split(',') for l in lines ]

    self.candyCaneDust = [ ( int(x[0]), int(x[1]) ) for x in lines ]
    
  ############
  def redSquaresWithBdubs( self ):
    # make sure we only go through each pairing once
    i = 0
    while i < ( len( self.candyCaneDust ) - 1 ):
      climb10 = self.candyCaneDust[i]
      for pairing in self.candyCaneDust[ i+1 : ] :
        xDiff = abs( climb10[0] - pairing[0] ) + 1
        yDiff = abs( climb10[1] - pairing[1] ) + 1
        self.redBlocks[ (climb10,pairing) ] = ( xDiff * yDiff )
      i += 1
    
    # get the largest square. as a note, we don't care about the points in part 1
    mymax = 0
    for k in self.redBlocks :
      mymax = max( self.redBlocks[k], mymax )

    print( mymax )

###############
  def main(self) :
    self.processArguments()
    self.redSquaresWithBdubs()

#######
if __name__ == "__main__":
  b = BdubsTheLegendaryRedStoner()
  b.main()
