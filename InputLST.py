# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:16:55 2020

@author: manta
"""
# caseX= [freq, bandwidth, gain]

#Sband
case1 = [2.4e9, 6e6 , 3.]
case2 = [2.4e9, 6e6 , 5.]
case3 = [2.4e9, 6e6 , 6.5]
case4 = [2.4e9, 6e6 , 8.]

#UHF
case5 = [500e6, 50e3 , 1.5]
case6 = [500e6, 50e3 , 5.]
case7 = [500e6, 50e3 , 8.]
## xband
case8 = [10e9, 70e6 , 5.]
case9 = [10e9, 70e6 , 6.5]
case10 = [10e9, 70e6 , 8.]

case11 = [10e9, 100e6 , 5.]
case12 = [10e9, 100e6 , 6.5]
case13 = [10e9, 100e6 , 8.]


caselst = [case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12, case13]

# Modulation schemes:

#modulation = [type, Spectral Efficency, Eb/No for given BER ]

mod1 = ['BPSK', 0.7 , 10.5 ]
mod2 = ['QPSK', 1.4 , 10.5 ]
mod3 = ['8-PSK', 2.1, 14   ]

modlst = [mod1,mod2,mod3]

# Coding = [ type, rate, gain]
cod1 = [ 'No coding', 1, 0]
cod1 = [ ' Convulational1', 0.5, 5 ]
cod1 = [ ' Convulational2', 0.5, 6 ]
cod1 = [ ' Convulational-RS', 0.5, 7 ]
cod1 = [ ' Convulational-RS', 0.166667, 9 ]
cod1 = [ 'TURBO', 0.166667, 10 ]
cod1 = [ 'LDPC', 0.75, 10 ]

#for i in range(len(caselst)):
