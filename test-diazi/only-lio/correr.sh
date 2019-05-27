#!/bin/bash

SALIDA=salida

export GFORTRAN_UNBUFFERED_ALL=1
export OMP_NUM_THREADS=1
#export LIOHOME=/opt/progs/LIOs/Excited
export LIOHOME=/opt/progs/LIOs/hybrid_tsh/lio
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LIOHOME/g2g:$LIOHOME/lioamber

${LIOHOME}/liosolo/liosolo -i diazi.in -c diazi.xyz -v > $SALIDA
