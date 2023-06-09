#!/usr/bin/python
from operator import itemgetter
import sys
current_word = None
current_count = 0
word = None
# read line from STDIN
for line in sys.stdin:
 # remove whitespace in input
 line = line.strip()
 # splitting the data; input we got from mapper.py
 word, count = line.split('\t', 1)
 # convert count to int
 try:
 count = int(count)
 except ValueError:
 # count was not a number, so silently
 # ignore/discard this line
 continue
 # this IF-switch only works because Hadoop sorts map
output
 # by key (here: word) before it is passed to the reducer
 if current_word == word:
 current_count += count
 else:
 if current_word:
 # write result to STDOUT
 print '%s\t%s' % (current_word, current_count)
 current_count = count
 current_word = word
# last word output
if current_word == word:
 print '%s\t%s' % (current_word, current_count)