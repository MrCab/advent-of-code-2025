import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

################################

class ContraSpreadGun :
    
  DEFAULT_FILE = "day07\\input07.txt"
  #DEFAULT_FILE = "day07\\sample07.txt"

  def __init__(self ) :
       self.lines = []
       self.DAY = 7

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
    self.lines = lines

  ############
  
  def spread_bullets( self ) :
    fricken_laser_beams = { self.lines[0].index('S') }
    reflect = '^'
    count_splits = 0

    for l in self.lines[ 1: ] :
      new_lasers = fricken_laser_beams
      pos = 0
      while pos < len( l ) :
        try :
          pos = l.index( reflect, pos )
          if pos in fricken_laser_beams :
            new_lasers.remove( pos )
            new_lasers.add( pos-1 )
            new_lasers.add( pos+1 )
            count_splits += 1
          pos += 1
        except:
          break
      fricken_laser_beams = new_lasers
    print( count_splits )


###############
  def main(self) :
    self.processArguments()
    self.spread_bullets()

#######
if __name__ == "__main__":
  n = ContraSpreadGun()
  n.main()
