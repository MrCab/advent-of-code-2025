import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

################################

class WereNotInReversePolishNotationAnymore :
    
  DEFAULT_FILE = "day06\\input06.txt"
  #DEFAULT_FILE = "day05\\sample05.txt"

  def __init__(self ) :
       self.thedigits = []
       self.columns = []
       self.DAY = 6

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
      lines = [ re.split( " +", l.strip() ) for l in lines ]

    self.thedigits = lines
    
  ############
  def mathinator1 ( self ) :
    i = 0
    checksum = 0
    while i < len( self.thedigits[0] ) :
      checksum += eval( self.thedigits[-1][i].join( [ j[i] for j in self.thedigits[0:-1] ] ) )
      i += 1
    print( checksum )

###############

  def mathinator2( self ) :
    i = 0
    sum = 0
    symbols = self.columns[ -1 ]
    while i < len( symbols ) :
      if symbols[i] in "*+" :
        sum += self.do_some_math( i )
      i += 1
    print( sum )

################

  def do_some_math( self, startPos ) :
    nums = []
    i = startPos
     
    num_to_add = [ j[i] for j in self.columns[0:-1]  ] # ['1', '2', ' ']
    num_to_add = "".join( num_to_add ) # "12 "

    while not re.match( "^ +$", num_to_add ) :
      nums.append( num_to_add )
      i += 1
      num_to_add = [ j[i] for j in self.columns[0:-1]  ] # ['1', '2', ' ']
      num_to_add = "".join( num_to_add ) # "12 "

    return eval( self.columns[-1][startPos].join( nums ) )


###############
  def main(self) :
    self.processArguments()
    self.mathinator1()
    self.mathinator2()

#######
if __name__ == "__main__":
  n = WereNotInReversePolishNotationAnymore()
  n.main()
