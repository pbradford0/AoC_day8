#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/7

import sys

def difference_calc(filename):
  diff = 0
  return diff

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  a = difference_calc(sys.argv[1])
  print "# of characters in the file minus # of characters in memory = " + str(difference_calc)
  
  #b = bobby_logic_2(sys.argv[1])
  #print "Wire A receives the signal " + str(a_signal)

if __name__ == '__main__':
  main()