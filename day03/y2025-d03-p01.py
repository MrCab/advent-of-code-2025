import re
import argparse

class DebugPrinter :

  verbose = False

  @staticmethod
  def debugPrint( message ) :
    if DebugPrinter.verbose :
      print( message )

################################

class NumberMaximizer :
    
  DEFAULT_FILE = "day03\\input03.txt"
  #DEFAULT_FILE = "day03\\test03.txt"

  def __init__(self) :
       self.jolts = []
       self.DAY = 3

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

    self.jolts = lines

  ############

# part 2 would amount to implementing a loop of sorts here (perhaps recursive) to do this trick N times,
# where N is 12. Just replce the 1s below with N to some extent.
# I could do this, or I could watch The Glass Onion with Mrs Cab.
# I'm going to imbreviate the reclamation ov my evening with a minefield of malapropisms


  def line_joltage_1( self, line ) :

    # ignore the last number - a 2 digit number is always > a single digit number
    # also we have no 0s anyway for 0000000001
    biggestPos = self.biggest_number_position_in_string( line[0:len(line) - 1 ] )
    
    # search the line from the first largest number
    secondBiggestPos = 1 + biggestPos + self.biggest_number_position_in_string( line[ 1+biggestPos: ] )

    DebugPrinter.debugPrint( ( line[biggestPos] + line[secondBiggestPos] ) + "----" + line )
    return int( ( line[biggestPos] + line[secondBiggestPos] ) )

  def biggest_number_position_in_string( self, line ) :
    i = 0
    biggestPos = 0
    while i < len( line ) :
      # only look for bigger - we want as big a follow up string as possible
      if line[i] > line[biggestPos] :
        biggestPos = i
        if line[biggestPos] == '9' : #max single digit, so stop searching.
          break
      i += 1
    return biggestPos

#############

  # len is the number of digits in the number

  def line_joltage_2( self, line, digits ) :

    nextPos = []
    i = 0
    nextPos.append( self.biggest_number_position_in_string( line[ 0 :len(line) - ( digits - 1 ) ] ) )

    i = 1
    while i < digits:    

        # ignore the last number(S) - a 2 digit number is always > a single digit number
        # also we have no 0s anyway for 0000000001
        nextPos.append( 1 + nextPos[-1]+ self.biggest_number_position_in_string( line[ ( 1 + nextPos[-1] ) :len(line) - ( ( digits - i ) - 1 ) ] ) )
        i += 1        
    returnMe = "".join( [ str(line[x]) for x in nextPos ] )
    return int( returnMe )


  #############
  def become_jolted_1( self ) :
    # totalJolts = 0
    # for line in self.jolts :
    #   totalJolts += self.line_joltage_1( line )

    # print( totalJolts )

    # totalJolts = 0
    # for line in self.jolts :
    #   totalJolts += self.line_joltage_2( line, 2 )

    # print( totalJolts )

    totalJolts = 0
    for line in self.jolts :
      totalJolts += self.line_joltage_2( line, 12 )

    print( totalJolts )



###############
  def main(self) :
    self.processArguments()
    self.become_jolted_1()

#######
if __name__ == "__main__":
  n = NumberMaximizer()
  n.main()
