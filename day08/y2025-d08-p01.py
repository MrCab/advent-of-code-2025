import math
import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

################################

class HauntedWiring :
    
  DEFAULT_FILE = "day08\\input08.txt"

  def __init__(self ) :
    self.vertecies = []
    self.edges = {}   
    self.DAY = 8

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
      self.columns = [ list( l.strip() + " "  ) for l in lines ]
      lines = [ re.split( ",", l.strip() ) for l in lines ]

    self.vertecies = [(int (l[0]), int(l[1]), int(l[2]) ) for l in lines]
    
  ############

  #EVERY....edge...

  def find_every_edge( self ):
    i = 0
    while i < len(self.vertecies) :
      j = i + 1
      while j < len(self.vertecies) :
        self.edges[ ( self.vertecies[i], self.vertecies[j] ) ] = self.get_edge_weight( self.vertecies[i], self.vertecies[j])
        j += 1
      i += 1


  ###########

  def get_edge_weight(self, v1, v2) :
    return ( math.sqrt( math.pow(v1[0]-v2[0],2) + math.pow(v1[1]-v2[1],2) + math.pow(v1[2]-v2[2],2) ))

###############
  def main(self) :
    self.processArguments()
    self.find_every_edge()
    print ( self.edges )


#######
if __name__ == "__main__":
  n = HauntedWiring()
  n.main()
