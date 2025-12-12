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
       self.freshmap = {}
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
        begin = int(y[0])
        end = int(y[1])
        self.fresh.append( [ begin , end + 1 ] ) #top of "range" is exclusive
    
        if begin in self.freshmap :
          end = max( self.freshmap[begin], end )
        self.freshmap[ begin ] = end

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

#################

  def map_to_freshness( self ) :
    # sort the keys - the start of ranges
    starts = [ k for k in self.freshmap.keys() ]
    starts.sort()

    full_range = [ ( starts[0 ], self.freshmap[ starts[0] ] ) ]

    # now we know each thing we see will be greater than the start range before it.
    # so we only care if it is less than the end range
    for s in starts[1:] :
      # check the largest number
      if s <= full_range[-1][1] :
        # check the top of this range
        if self.freshmap[s] > full_range[-1][1] :
          full_range[-1] = ( full_range[-1][0], self.freshmap[s] )
        # else do nothing - this falls entirely within the highest value's range
      else :
        full_range.append( ( s, self.freshmap[s] ) )

    # add up our numbers
    sum = 0
    for subtraction in full_range :
      sum += subtraction[1] - subtraction[0] + 1
    print(sum)


###############
  def main(self) :
    self.processArguments()
    #self.destroy_anchovies()
    self.map_to_freshness()

#######
if __name__ == "__main__":
  n = BadToppingDetector()
  n.main()
