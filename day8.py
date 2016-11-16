#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/7

import sys
import re

def difference_calc(filename):
  #diff = # chars in the file - # chars in memory
  diff = 0
  file_count = 0
  mem_count = 0
  line_count = 0
  #create regex to filter out what isn't put into memory:
  #1) start and end quotes
  re_quotes = re.compile("[\"].*[\"]")
  #2) \\
  re_backslash = re.compile("[\\\\][\\\\]")
  #3) \"
  re_quote = re.compile("[\\\\][\\\"]")
  #4) \x00 (where 00 is any hexadecimal pair)
  re_hex = re.compile("[\\\\]x[0-9a-f][0-9a-f]")
  
  input = open(filename, 'rU')
  for line in input:
    #ignore whitespace the easy way: destroying all of it
    line = ''.join(line.split())
    #count no of chars in the file per line
    line_count = len(line)
    file_count += line_count
    #count no of chars put into memory
    
    #check regex 1
    if not re.match(re_quotes, line):
      print "Error: Data contains a non-string"
      break
    else:
      line = line[1:-1]
    
    print "Before: "+ line,
    #check regex 2. can have multiple matches
    line = re.sub(re_backslash, "\\\\", line)
    #check regex 3, same^
    line = re.sub(re_quote, "\"", line)
    #check regex 4
    line = re.sub(re_hex, "H", line)
    #debug
    #debug block
    print " and after: "+ line
    #print "line: " + str(line_count+2),
    #print "| backslash: " + str(len(re.sub(re_backslash, line))),
    #print "| quote: "+ str(len(re.sub(re_quote, line))),
    #print "| hex: "+ str(3*(len(re.sub(re_hex, line)))),
    
    #print "| total: " + str(line_count)
    #recalc line_count for the subbed string
    line_count = len(line)
    mem_count += line_count
    
  diff = file_count - mem_count
  return diff

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  a = difference_calc(sys.argv[1])
  print "(chars in the file) - (chars in memory) = " + str(a)
  
  #b = bobby_logic_2(sys.argv[1])
  #print "Wire A receives the signal " + str(a_signal)

if __name__ == '__main__':
  main()