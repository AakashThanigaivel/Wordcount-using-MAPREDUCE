#!/usr/bin/python
import sys
# read line from STDIN
for line in sys.stdin:
 # remove whitespace in input
 line = line.strip()
 # split the line into words
 words = line.split()
 # looping over words array and
print words; increase counter
 for word in words:
 # write result to STDOUT; this
will be considered as input for
reducer.py
 print '%s\t%s' % (word, 1)