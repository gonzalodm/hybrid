#!/bin/bash

file=diazi

for num in {1..20}
do
   echo "RUNNING NON-ADIABATIC DYNAMIC OF $num"
   cp inputs/init_structs.rst7.$num .
   mv init_structs.rst7.$num $file.rst7
   ./amber_to_hybrid.py $file > translate$num.log
   cp $file.XV $file.init.XV
   ./run.sh
   mkdir TRAJIN_$num
   mv $file.out $file.ene $file.init.pdb $file.last.pdb TRAJIN_$num
   mv $file.rce $file.rcg translate$num.log $file.init.XV TRAJIN_$num
   mv $file.XV $file.last.XV
   mv $file.last.XV TRAJIN_$num
   rm $file.rst7 $file.xyz mulliken out.fdf qm.xyz

done
