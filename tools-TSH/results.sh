#!/bin/bash

file=diazi
awk '$1=="STATE" {print $0}' $file.out | awk '$2=="1" {print $4}' > E1exc.dat
awk '$1=="STATE" {print $0}' $file.out | awk '$2=="2" {print $4}' > E2exc.dat
awk '$1=="STATE" {print $0}' $file.out | awk '$2=="3" {print $4}' > E3exc.dat
awk '$1=="poblacion1" {print $2}' $file.out > pob1.dat
awk '$1=="poblacion2" {print $2}' $file.out > pob2.dat
awk '$1=="prob_normal" {print $2}' $file.out > prob.dat
grep Energy $file.out | grep SCF     | awk '{print $NF}' > scf.dat
grep Energy $file.out | grep Excited | awk '{print $NF}' > exc.dat
grep Energy $file.out | grep System  | awk '{print $NF}' > posta.dat
grep "Total Energy + Kinetic" $file.out | awk '{print $NF}' > Etot.dat
grep "Kinetic Energy (eV)" $file.out | awk '{print $NF}' > EKtot.dat
awk '$1=="Elio" {print $NF}' $file.out > EPtot.dat

