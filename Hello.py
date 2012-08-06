#!/usr/bin/python2.7 -tt
# Copyright 2012 Space Systems/Loral Inc. All Rights Reserved.

import sys

def Hello(name):
  if name == 'Alice' or name == 'Nick':
    print 'Alert: Alice mode'
    name = name + '???'
  else:
    Doesnotexist(name)
  name = name + "!!!!!!"
  print "Hello", name
  
  
# Define a main() function that prints a greeting.
def main():
  Hello(sys.argv[1])
  
# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
  main()
  
  
  