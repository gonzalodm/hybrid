#!/bin/bash

file=diazi
HYB=/home/gonzalo/progs/hybrid_TSH/bin/hybrid
export GFORTRAN_UNBUFFERED_ALL=1
export OMP_NUM_THREADS=1
export LIOHOME=/home/gonzalo/progs/hybrid_TSH/lio
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LIOHOME/g2g:$LIOHOME/lioamber 

$HYB < $file.fdf > $file.out
rm INPUT_*
