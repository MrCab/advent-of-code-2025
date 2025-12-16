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

class TheGraph :
  def __init__(self ) :
    self.vertecies = set()
    self.edges = {}
  
  def containsV( self, x ) :
    return x in self.vertecies
  
  def combine( self, g2 ) :
    self.vertecies = self.vertecies.union( g2.vertecies )
    for e in g2.edges.keys() :
      self.edges[ e ] = g2.edges[ e ]

#########################

class HauntedWiring :
    
  DEFAULT_FILE = "day08\\input08.txt"
  #DEFAULT_FILE = "day08\\sample08.txt"

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

  #############

  # n should default to 1000 for part 1
  def death_by_1000_edges( self, n ) :
    clever_algo = []
    all_edges_list = sorted( self.edges.items(), key=lambda item:item[1] )

    i = 0
    while i < n :
      e = all_edges_list[ i ]
      combine = []
      
      j = 0

      # check both vertecies against all graphs
      for g in clever_algo :
        if g.containsV( e[0][0] ) or g.containsV( e[0][1] ) :
          combine.append( j )
        j += 1

      # neither vertex is in a graph - then make a new graph
      if len( combine ) == 0  :
        newbie = TheGraph()
        newbie.edges[e[0]] = e[1]
        newbie.vertecies.add( e[0][0] )
        newbie.vertecies.add( e[0][1] )
        clever_algo.append( newbie )

      # only add the edge if the graph does not contain both vertecies  
      elif len( combine ) == 1 :
        # split out this if to keep the else at the end
        if not (clever_algo[combine[0] ].containsV(e[0][0]) and clever_algo[combine[0]].containsV(e[0][1] ) ) :
          clever_algo[ combine[0] ].edges[e[0]] = e[1]
          clever_algo[combine[0]].vertecies.add( e[0][0] )
          clever_algo[combine[0]].vertecies.add( e[0][1] )
        else :
          DebugPrinter.debugPrint( "Got both already" )

      # doomsday - one vertex is in two graphs
      # - combine them
      # - remove the edge
      # - remove the original graph from the list
      elif len( combine ) == 2 :
        clever_algo[combine[0]].combine( clever_algo[combine[1] ] )
        clever_algo[combine[0]].edges[e[0]] = e[1]
        del clever_algo[ combine[1] ]

        # the vertecies were already in both graphs
        
      # this is an error state
      else :
        print( 'How the heck did you get here?!?!?!' )
        exit (1)
      i += 1

    #print( clever_algo )

    answer = sorted( [len(x.vertecies) for x in clever_algo])
    print( str(answer[-1] * answer[-2] * answer[-3] ) )


###############
  def main(self) :
    self.processArguments()
    self.find_every_edge()
    self.death_by_1000_edges( 1000 )
    #print ( self.edges )


#######
if __name__ == "__main__":
  n = HauntedWiring()
  n.main()
