#!/bin/bash

file=diazi
HYB=/home/gonzalo/progs/LIOs/hybrid_tsh/bin/hybrid
export GFORTRAN_UNBUFFERED_ALL=1
export OMP_NUM_THREADS=1
export LIOHOME=/home/gonzalo/progs/LIOs/hybrid_tsh/lio
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LIOHOME/g2g:$LIOHOME/lioamber 

$HYB < $file.fdf > $file.out

