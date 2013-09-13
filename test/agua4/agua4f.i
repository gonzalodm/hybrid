&INT0 
 TITLE = 'NO3', 
 NATOM = 12,
 NOPT=2,
 NORM = T, 
 ANG = T, 
 EX = T, 
 COUL = F, 
 SCF1 = T, 
 PROP = F, 
 FIELD = F, 
 SOL = F, 
 RESP1 = F/
8 36.4999690237912 73.0255065872895 48.9729194456153
1 37.1342087683516 73.4160122737471 48.326408887848
1 36.1621612584882 72.213469795644 48.5278396193069
8 35.6586536008279 70.3566182161701 48.0233566863454
1 34.6972530387238 70.313388085386 48.1872403147024
1 36.0975960217802 69.9125620184236 48.8045013226303
8 37.9801606705981 71.7072931459075 50.8955682157623
1 37.4904201238255 72.3714781059498 50.3262943428027
1 38.9326003555581 71.945937630992 50.8302536686694
8 37.3326612712017 69.3799425736299 49.9345422708664
1 37.5408965338147 68.6831813414169 50.6049662042145
1 37.631211616953 70.2793147696215 50.3486096244272
&geo/
gaussian
 8  15   6
 6 2 1 4 1 1
 0 0 0 1 1 2
   5222.9022000             -0.0019364
    782.5399400             -0.0148507
    177.2674300             -0.0733187
     49.5166880             -0.2451162
     15.6664400             -0.4802847
      5.1793599             -0.3359427
     10.6014410              0.0788058
      0.9423170             -0.5676952
      0.2774746              1.0000000
     33.4241260              0.0175603
      7.6221714              0.1076300
      2.2382093              0.3235256
      0.6867300              0.4832229
      0.1938135              1.0000000
      0.8000000              1.0000000
 8 13 13
 1 1 1 1 1 1 1  1  1 1  1 1 1
 0 0 0 0 0 0 0  1  1 1  2 2 2
       2000.00000000             1.00000000
        400.00000000             1.00000000
        100.00000000             1.00000000
         25.00000000             1.00000000
          7.80000000             1.00000000
          1.56000000             1.00000000
          0.39000000             1.00000000
          7.80000000             1.00000000
          1.56000000             1.00000000
          0.39000000             1.00000000
          7.80000000             1.00000000
          1.56000000             1.00000000
          0.39000000             1.00000000
gaussian
 1   5   2
 4 1
 0 0
     50.9991780    0.0096604761
      7.4832181    0.073728860
      1.7774676    0.29585808
      0.5193295    0.71590532
      0.1541100    1.000000
 1 4 4
 1 1 1 1
 0 0 0 0
     45.0000000    1.000000
      7.5000000    1.000000
      1.5000000    1.000000
      0.3000000    1.000000
endbasis
&SCFINP
 OPEN = F, 
 NMAX=300
 NCO = 20,
 NUNP = 0,
 ATRHO = F, 
 VCINP = F, 
 DIRECT = T, 
 EXTR = F, 
 SHFT = F, 
 SHI =  1., 
 IDAMP = 0, 
 GOLD =  5., 
 TOLD =  1.E-06, 
 WRITE = F, 
 MEMO = T/
&EXCH 
 IEXCH=9
 INTEG = T, 
 DENS = T, 
 IGRID = 2, 
 IGRID2=2/


