import re
import argparse


class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

class LockPickingPython :
    
  DEFAULT_FILE = "day1\\input1.txt"
  START_NUMBER = 50

  def __init__(self) :
       self.startingNumber = 50
       self.instructions = []
       self.DAY = 1

##################

  def processArguments( self ) :
    # parse the input, if any
    parser = argparse.ArgumentParser(description=f'AOC2025 Puzzle Day { self.DAY }')
    parser.add_argument("-i", "--input", help="Input File if not default", action='store', default=self.DEFAULT_FILE )
    parser.add_argument("-v", "--verbose", help="Print verbose test output", action='store_true', default=True )

    parser.add_argument("-n", "--number", help="starting Number", action='store_true', default=50 )
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
    self.instructions = lines

#############
  def lockPicker( self ) :
    n = self.startingNumber
    passcode = 0

    for s in self.instructions:
      direction = s[0]
      dist = int( s[1:] ) # % 100 # we don't really care about 100s ... until part 2 hates us
      mult = 1
      if direction == 'L' : 
        mult = -1
      
      n = ( n + ( mult * dist ) ) % 100
      DebugPrinter.debugPrint( n )
      if n == 0 :
        passcode += 1
    return passcode


###############
  def main(self) :
    self.processArguments()
    print( self.lockPicker() )

#######
if __name__ == "__main__":
  p = LockPickingPython()
  p.main()

