#!/usr/bin/env python3

# TODO: poner una variable que indique cada cuantos frames se imprimio las coordenadas

import sys
import os
import re
import math

def help_print():
   print("This program must be executed with the following command:")
   print("./distances.py name_file N M step\n")
   print("name_file = file to read coordinates of atoms (only works with .rcg)")
   print("N, M      = Atoms number (integers)")
   print("step      = time step (in femtosec)\n")
   print("This program generates a file with distances between atom N and M in angstrom")

def distances(NameFile,N,M,td):
#  Check if .rcg exist
   is_file = os.path.isfile(NameFile)
   if is_file == False:
      print("The file " + NameFile + " doesn't exist")
      return -1

   file_in = open(NameFile,"r")

#  Wath is the first atom?
   if N < M:
      first = N
      second= M
   elif N > M:
      first = M
      second= N
   else:
      print("Something is WRONG, Distances only be calculated between two differents atoms")
      return -1

#  Read Coordinates of atoms
   print("# Time[fs]\tDistances[A]")
   common = "\s+\w+\s+\w+\s+\w+\s+\d+\s+([0-9.-]+)\s+([0-9.-]+)\s+([0-9.-]+)"
   count  = 0.0
   prep   = 0
   for line in file_in.readlines():
      calc = False
      patron = "ATOM      "
      patron = patron + str(first) + common
      m = re.match(patron,line)
      # Save coordinates of first atom
      if m:
         x1 = float(m.group(1))
         y1 = float(m.group(2))
         z1 = float(m.group(3))

      patron = "ATOM      "
      patron = patron + str(second) + common
      m = re.match(patron,line)
      # Save coordinates of second atom
      if m:
         x2 = float(m.group(1))
         y2 = float(m.group(2))
         z2 = float(m.group(3))
         calc = True

      # Print time and distance
      if calc:
        dist = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2)
        dist = math.sqrt(dist)
        print("%8.4f\t%8.4f" % (count,dist))
        count = count + td

   file_in.close()

if __name__ == "__main__":

#  Check inputs
   if len(sys.argv) <= 1: 
      help_print()
      exit(-1)

   if sys.argv[1] == "--help":
      help_print()
      exit(-1)

#  Save inputs
   name_file = sys.argv[1]
   N = int(sys.argv[2])
   M = int(sys.argv[3])
   step = float(sys.argv[4])

#  Read file and calculate distances
   error = distances(name_file,N,M,step)
   if error == -1:
      print("Something is Wrong. Error in distances")
 
   
