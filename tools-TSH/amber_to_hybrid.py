#!/usr/bin/env python3

import sys
import os
import re
import itertools

# ==============================================
# This code converts a restart file of Amber to 
# XV file to run a molecular dynamic with Hybrid
# ==============================================



# ================================================================
# This function return a list with the order of atoms to run HYB
# ================================================================
def read_hybrid(NameFile):
#  Check if fdf exist
   is_file = os.path.isfile(NameFile)
   if is_file == False:
      print("The file " + NameFile + " doesn't exist")
      exit()

   file_in = open(NameFile,"r")

#  Read natoms and nspecies
   for line in file_in.readlines():
      m = re.match("NumberOfAtoms\s+([0-9.-]+)",line)
      if m:
         Natoms = int(m.group(1))
      m = re.match("NumberOfSpecies\s+([0-9.-]+)",line)
      if m:
         Nspecies = int(m.group(1))

   file_in.close()
   
#  Read Species
   file_in = open(NameFile,"r")
   start = "%block ChemicalSpeciesLabel"
   end = "%endblock ChemicalSpeciesLabel"
   for result in re.findall(start+"(.*?)"+end,file_in.read(),re.S):
      block = list(result.split(" "))

   block = map(lambda s: s.strip(), block) # Delete \n
   block = list(filter(None,block)) # Delete " "

   list_Species = []
   for i in range(Nspecies):
      list_Species.append(int(block[i*3+1]))

   if len(list_Species) != Nspecies:
      print("ERROR: Different number of Species")
      exit(-1)

#  Read Atoms
   file_in = open(NameFile,"r")
   start = "%block AtomicCoordinatesAndAtomicSpecies"
   end = "%endblock AtomicCoordinatesAndAtomicSpecies"
   for result in re.findall(start+"(.*?)"+end,file_in.read(),re.S):
      block = list(result.split(" "))

   block = map(lambda s: s.strip(), block) # Delete \n
   block = list(filter(None,block)) # Delete " "

   list_Natoms = []
   for i in range(Natoms):
      list_Natoms.append(int(block[i*4+3]))

   if len(list_Natoms) != Natoms:
      print("ERROR: Different number of Atoms")
      exit(-1)

   order_hyb = []
   for i in range(Natoms):
      ele = list_Natoms[i] - 1
      order_hyb.append(list_Species[ele])

   return order_hyb
# ================================================================

# ================================================================
# This function return a list with the order of atoms in Amber
# ================================================================
def read_amber(NameFile):
#  Check if prmtop exist
   is_file = os.path.isfile(NameFile)
   if is_file == False:
      print("The file " + NameFile + " doesn't exist")
      exit(-1)

   file_in = open(NameFile,"r")

   file_in = open(NameFile,"r")
   start = "%FLAG ATOM_NAME"
   end = "%FLAG CHARGE"
   for result in re.findall(start+"(.*?)"+end,file_in.read(),re.S):
      block = list(result.split(" "))

   block = map(lambda s: s.strip(), block) # Delete \n
   block = list(filter(None,block)) # Delete " "

   block.remove("%FORMAT(20a4)") # I think this is present in all prmtop files

#  Only works with H,C,N,O. TODO: Add new atoms
   order_amb = []
   for i in range(len(block)):
      if block[i][0] == "H":
         order_amb.append(1)

      elif block[i][0] == "C":
         order_amb.append(6)

      elif block[i][0] == "N":
         order_amb.append(7)

      elif block[i][0] == "O":
         order_amb.append(8)

      else:
         print("This atom was not specified")
         print("Please add the atomic number to: "+block[i][0])
         exit(-1)

   return order_amb
# ================================================================

# ================================================================
# This function return a list with the coordinates and velocities
#                    of atoms in Amber Format
# ================================================================
def read_coord_vel(NameFile):
#  Check if rst7 exist
   is_file = os.path.isfile(NameFile)
   if is_file == False:
      print("The file " + NameFile + " doesn't exist")
      exit(-1)

#  Read coordinates and velocities
   with open(NameFile) as file_in:
      block = file_in.readlines()

   block = map(lambda s: s.strip(), block) # Delete \n
   block = list(filter(None,block)) # Delete " "
   del block[0]            # Delete Name of Residue
   temp = block[0].split() # Natoms  Time in rst7
   Natoms = int(temp[0])
   del block[0]            # Delete Number of atoms from list

   all_array = []
   for i in range(len(block)):
      temp = block[i].split()
      all_array = all_array + temp
      
#  Read Coordinates
   coord = []
   for i in range(Natoms):
      coord.append(float(all_array[i*3]))
      coord.append(float(all_array[i*3+1]))
      coord.append(float(all_array[i*3+2]))

#  Read Velocities
   dim = Natoms*3
   vel = []
   for i in range(Natoms):
     ele = dim + i*3
     vel.append(float(all_array[ele]))
     vel.append(float(all_array[ele+1]))
     vel.append(float(all_array[ele+2]))

   return coord,vel
# ================================================================

# ================================================================
# This function return a list with the coordinates and velocities
#                      to run Hybrid
# ================================================================
def generate_list(amber,hybrid):
#  Check dimension of inputs
   if len(amber) != len(hybrid):
      print("ERROR: TWO LISTS HAVE DIFFERENT SIZE")
      exit(-1)
    
   order = []
   if amber == hybrid:
      for i in range(len(hybrid)):
         order.append(i)
   else:
      for i in range(len(hybrid)):
         element = hybrid[i]
         for j in range(len(amber)):
            if element == amber[j]:
               order.append(j)
               amber[j] = 1000 # NO coincidence with this
               break 

   return order
# ================================================================

# ================================================================
#  Obtain coordinates and velocities in Hybrid format
# ================================================================
def convert(order,cA,vA):
   cB = []
   vB = []

   Natoms = len(order)
   for i in range(Natoms):
      ele = order[i]
      x=cA[3*ele]
      y=cA[3*ele+1]
      z=cA[3*ele+2]
      cB.append(x)
      cB.append(y)
      cB.append(z)
      x=vA[3*ele]
      y=vA[3*ele+1]
      z=vA[3*ele+2]
      vB.append(x)
      vB.append(y)
      vB.append(z)

   return cB,vB
# ================================================================

# ================================================================
#                  This function form XV file
# ================================================================
def obtainXV(coord,vel,NameFile):
   file_in = open(NameFile,"w")

   # Write box parameters
   file_in.write("\t0.000000000\t0.000000000\t0.00000000\n")
   file_in.write("\t0.000000000\t0.000000000\t0.00000000\n")
   file_in.write("\t0.000000000\t0.000000000\t0.00000000\n")

   # Write number of atoms
   Natoms = int(len(coord) / 3)
   file_in.write("\t")
   file_in.write(str(Natoms))
   file_in.write("\n")

   # Coord in Amber = [angstrom]
   # Vel in Amber   = [angstrom/20.455ps]
   for num in range(len(coord)):
      coord[num] = coord[num] * 1.88973  # Angstrom -> Bohr
      temp = vel[num] * 20.455 * 1.88973 # Bohr/ps
      vel[num] = temp / 1000.0           # Bohr/fs
   # Coord in Hyb = [Bohr]
   # Vel in Hyb   = [Bohr/fs]

   # Write coordinates and velocities
   for i in range(Natoms):
      file_in.write("\t%f" % coord[i*3])
      file_in.write("\t%f" % coord[i*3+1])
      file_in.write("\t%f" % coord[i*3+2])
      file_in.write("\t%f" % vel[i*3])
      file_in.write("\t%f" % vel[i*3+1])
      file_in.write("\t%f" % vel[i*3+2])
      file_in.write("\n")
   file_in.write("\n")
   file_in.close()
   
   return 0
# ================================================================

# ================================================================
#                         MAIN PROGRAM
# ================================================================

if __name__ == "__main__":

#  Read name of files
   if (len(sys.argv) <= 1):
      print("This program must be executed with:")
      print("./amber_to_hybrid.py name")
      exit(-1)

#  File names of amber and hybrid programs
   prmtop = sys.argv[1] + ".prmtop"
   rst7   = sys.argv[1] + ".rst7"
   fdf    = sys.argv[1] + ".fdf"
   XV     = sys.argv[1] + ".XV"

   print("Amber Files: " + prmtop + " " + rst7)
   print("Hybrid Files: " + fdf + " " + XV)

#  Read order of atoms in Hybrid
   hyb = []
   hyb = read_hybrid(fdf)
   print("hybid order: ",hyb)

#  Read order of atoms in Amber
   amb = []
   amb = read_amber(prmtop)
   print("amber order: ",amb)

#  Read coordinates and velocites from Amber file
   coord_amb = []
   vel_amb = []
   coord_amb,vel_amb = read_coord_vel(rst7)

#  Obtain List to pass amber -> hyb
   order = []
   order = generate_list(amb,hyb)
   print("Global order:",order)

#  Obtain coordinates and velocities in Hybrid format
   coord_hyb = []
   vel_hyb = []
   print("amber coord:",coord_amb)
   print("amber vel:",vel_amb)
   coord_hyb,vel_hyb = convert(order,coord_amb,vel_amb)
   print("hybrid coord:",coord_hyb)
   print("hybrid vel:",vel_hyb)

#  Form input XV
   error = obtainXV(coord_hyb,vel_hyb,XV)
   if error != 0:
      print("Error in generate XV file")

