#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/8

import sys
import re

def encode_sub(regex, subst, line):
  #separates the first 3 and last 3 chars, aka the special case of start and end quotes
  start = line[0:3]
  end = line[-3:-1] + line[-1]
  line = line[3:-3]
  line = re.sub(regex, subst, line)
  line = start + line + end
  return line
  
def difference_calc(filename):
  #diff = # chars in the file - # chars in memory
  diff = 0
  file_count = 0
  mem_count = 0
  line_count = 0
  #create regex to filter out what isn't put into memory:
  #1) start and end quotes
  re_start_end = re.compile('\A".*"\Z')
  #2) \\
  re_backslash = re.compile(r"\\\\")
  #3) \"
  re_quote = re.compile(r"\\\"")
  #4) \x00 (where 00 is any hexadecimal pair)
  re_hex = re.compile(r"\\x[0-9a-f][0-9a-f]")
  
  input = open(filename, 'rU')
  for line in input:
    #ignore whitespace the easy way: destroying all of it
    line = ''.join(line.split())
    #count no of chars in the file per line
    line_count = len(line)
    file_count += line_count
    #check regex 1
    if not re.match(re_start_end, line):
      print "Error: Data contains a non-string"
      break
    else:
      #there is no reason to overcomplicate things by using sub
      #to remove the first and last character but none of the rest.
      line = line[1:-1]
    #check regex 2. can have multiple matches
    line = re.sub(re_backslash, "b", line)
    #check regex 3, same^
    line = re.sub(re_quote, "q", line)
    #check regex 4
    line = re.sub(re_hex, "h", line)
    #recalc line_count for the subbed string
    line_count = len(line)
    mem_count += line_count
    
  diff = file_count - mem_count
  return diff
  
def encode_calc(filename):
  #diff = # encoded chars - # chars in string
  diff = 0
  file_count = 0
  encode_count = 0
  line_count = 0
  #create regex to match things that need encoding:
  #1) \ becomes \\
  re_backslash = re.compile(r"\\")
  #2) " becomes \"
  re_quote = re.compile(r"\"")
  #3) start/end quote case
  re_start_end = re.compile('\A".*"\Z')
  
  input = open(filename, 'rU')
  for line in input:
    #ignore whitespace the easy way: destroying all of it
    line = ''.join(line.split())
    #count no of chars in the file per line
    line_count = len(line)
    file_count += line_count
    #
    
    #check regex 1. can have multiple matches
    #line = re.sub(re_backslash, r"\\\\", line)
    #check regex 2, same^
    #line = re.sub(re_quote, r"\\\"", line)
    #recalc line_count for the subbed string
    #check regex 3
    print "Before: "+ line
    if not re.match(re_start_end, line):
      print "Error: Data contains a non-string"
      break
    else:
      #start and end quotes are special and must be preserved
      line = line[0] + "\\\"" + line[1:-1] + "\\\"" + line[-1]
    line = encode_sub(re_backslash, r"\\\\", line)
    #check regex 3, same^
    line = encode_sub(re_quote, r"\"", line)
    print "After:  "+ line
    encode_count += len(line)
  diff = encode_count - file_count
  return diff

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  #a = difference_calc(sys.argv[1])
  #print "(chars in the file) - (chars in memory) = " + str(a)
  
  b = encode_calc(sys.argv[1])
  print "(encoded chars) - (literal chars) = " + str(b)

if __name__ == '__main__':
  main()