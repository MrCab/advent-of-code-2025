import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

################################

class BadToppingDetector :
    
  DEFAULT_FILE = "day05\\input05.txt"
  #DEFAULT_FILE = "day05\\sample05.txt"

  def __init__(self ) :
       self.fresh = []
       self.toppings = []
       self.DAY = 5

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

    # split the good lines from the ingredient lines
    for x in lines :
      if '-' in x :
        y = x.split('-')
        self.fresh.append( [ int(y[0]) , int(y[1]) + 1 ] )
      elif x != '' :
        self.toppings.append(x)
    
  ############
  def destroy_anchovies( self ) :
    fresh = 0
    for t in self.toppings:
      for r in self.fresh :
        if int(t) in range( r[0], r[1] ) :
          fresh += 1
          break
    print( fresh )


###############
  def main(self) :
    self.processArguments()
    self.destroy_anchovies()

#######
if __name__ == "__main__":
  n = BadToppingDetector()
  n.main()
