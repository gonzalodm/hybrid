&INT0 
 TITLE = 'NO3', 
 NATOM = 30,
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
 8    37.5025977204376        70.9764315718504        46.6995426743825     
 1    37.1863916824397        71.2471048781045        45.8160380614876     
 1    38.4793362294105        71.2294887183951        46.7671117836209     
 8    42.5251173321169        69.3517535202149        48.8616316156561     
 1    41.9300244394091        69.9877436839870        49.3682130933955     
 1    43.3558139170039        69.2335242754766        49.3583218240896     
 8    39.9969584298881        70.8468635790133        47.3790519471089     
 1    39.5909367860038        69.9177960158517        47.5257934031584     
 1    40.9382013054248        70.6369539239785        46.8452910843924     
 8    39.7519881772295        66.9367965481654        46.1056487625603     
 1    40.1083034908870        66.2797139617005        46.7342957728922     
 1    39.2059185463619        67.5966412267509        46.6564785225914     
 8    41.6452989003131        68.1617551133103        44.9027377863586     
 1    40.8686904875368        67.6477181136673        45.3388606200519     
 1    41.4842459211753        68.1685151728829        43.9403507626882     
 8    38.1671737287599        70.9719581803820        50.4247404890632     
 1    37.7099369495072        71.5282005215658        49.7610603187570     
 1    39.1686650521796        71.0534336252471        50.2502965837835     
 8    40.6850491319977        71.1383499953450        49.7111202332128     
 1    40.3933840707856        71.1469879239253        48.6510474766891     
 1    41.0522214031268        72.0174928460143        49.9406009359995     
 8    37.5587600571201        68.5485484878644        49.8733850216389     
 1    37.8923559229077        67.9339570930280        50.5557742610562     
 1    37.7402204145398        69.5085628703244        50.2003567486486     
 8    42.1539249970546        70.2111725177180        46.3913509272738     
 1    42.5008304036293        69.8048127483650        47.2465700246220     
 1    42.0095506549802        69.4431102550286        45.7293756847803     
 8    38.5146976154099        68.7113221815113        47.5262640836045     
 1    38.1391541948352        68.5221481114013        48.4793794634830     
 1    37.8685695293505        69.3569119557067        47.0920659456146     
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
 NMAX=1
 NCO = 50,
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
 IGRID2=0/


