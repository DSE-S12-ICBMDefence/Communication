# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:54:42 2020

@author: Coen
"""
import numpy as np


def LinkMarginCalc(freq,rxAntennaGain,EbN0mod,CodeGain):
    # Boltzmann constant and speed of light
    kb = 1.3807e-23
    c = 2.998e8
    T0 = 290.
    
    distance = 1300e3                # Distance between satellites in meters
    lamb = c/(freq)                 # wavelenght in meters
    txAntennaGain = rxAntennaGain   # gain in dB
    polarizationLoss = 0.           # losses in dB
    transmitterLosses = 1.2         # losses in dB
    outputPower = 3.5                # power in W
    Ta = 790.                       # Antenna noise temperature in K
    L = 0.9                         # Cable length in meters
    F = 4.0                         # Noise figure of transceiver in dB
    SystemNoiseTemp = Ta + T0*((1-L)/L) + T0*(10**(F/10)-1) # System noise temperature in Kelvin
    GoverT = rxAntennaGain-(10*np.log10(SystemNoiseTemp)) # rx G/T in dB
    EbN0threshold = EbN0mod-CodeGain # Eb/N0 threshold for modulation + code with BER = 10^-6
    implementationLoss = 1.         # Losses in dB
    receiverLosses = 2.             # losses in dB
    bitrate = 20e3                  # bitrate in bit/s
    linkMargin = 3.                 # link margin in dB
    
    #Free space loss
    freeSpace = 20*np.log10(4 * np.pi * distance/lamb)
    # Signal transmitted by antenna
    txSignal = 10*np.log10(outputPower) - transmitterLosses + txAntennaGain
    # Signal received by antenna
    rxSignal = txSignal - freeSpace - polarizationLoss - receiverLosses
    # Signal received at the antenna port
    #rxSignalAntenna = rxSignal + rxAntennaGain
    
    # Signal to noise ratio (SNR)
    SNR = rxSignal + GoverT - 10*np.log10(kb)
    
    # Eb/N0 calculated at the receiver
    EbN0 = SNR - 10*np.log10(bitrate)
    
    # full link budget including link margin
    margin = EbN0 - EbN0threshold - implementationLoss - linkMargin
    return margin, bitrate, outputPower, SystemNoiseTemp



# caseX= [freq, bandwidth, gain]

#Sband
case1 = [2.4e9, 6e6 , 3.]
case2 = [2.4e9, 6e6 , 5.]
case3 = [2.4e9, 6e6 , 6.5]
case4 = [2.4e9, 6e6 , 8.]

#UHF
case5 = [500e6, 50e3 , 1.5]
case55 = [400e6, 50e3 , 0.]
case52 = [500e6, 30e3,0.]
case6 = [500e6, 50e3 , 5.]
case7 = [500e6, 50e3 , 8.]
## xband
case8 = [10e9, 70e6 , 5.]
case9 = [10e9, 70e6 , 6.5]
case10 = [10e9, 70e6 , 8.]

case11 = [10e9, 100e6 , 5.]
case12 = [10e9, 100e6 , 6.5]
case13 = [10e9, 100e6 , 8.]

caselst = [case55]
#caselst = [case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12, case13]

# Modulation schemes:

#modulation = [type, Spectral Efficency, Eb/No for given BER ]

mod1 = ['BPSK', 0.7 , 10.5 ]
mod2 = ['QPSK', 1.4 , 10.5 ]
mod3 = ['8-PSK', 2.1, 14.   ]

modlst = [mod1,mod2,mod3]

# Coding = [ type, rate, gain]
cod1 = [ 'No coding', 1, 0]
cod2 = [ 'Convulational1', 0.5, 5 ]
cod3 = [ 'Convulational2', 0.5, 6 ]
cod4 = [ 'Convulational-RS', 0.5, 7 ]
cod5 = [ 'Convulational-RS', 0.166667, 9 ]
cod6 = [ 'TURBO', 0.166667, 10 ]
cod7 = [ 'LDPC', 0.75, 10 ]


#codlst = [ cod1, cod2, cod3, cod4,cod5,cod6,cod7]
codlst = [ cod1, cod2, cod3, cod4, cod5]

count = 0
for i in range(len(caselst)):
    for j in range(len(modlst)):
        for k in range(len(codlst)):
            Freq, MaxBandwidth, AntennaGain = caselst[i]
            Modtype, SE, EbN0mod = modlst[j]
            Codetype, Coderate, CodeGain = codlst[k]
            Margin, Bitrate, OutputPower, SystemNoiseTemp = LinkMarginCalc(Freq, AntennaGain, EbN0mod, CodeGain)
            
            InfoBandwidth = Bitrate/SE
            TotalBandwidth = InfoBandwidth/Coderate
                                    
            if Margin > 0. and TotalBandwidth < MaxBandwidth:
                print("Link closed with margin of: ",np.round(Margin,3),"and bandwidth needed = :",np.round(TotalBandwidth*10**(-3),1),"kHz")
                print("Link properties:")
                print("Frequency: ",np.round(Freq*(10**(-9)),3),"GHz             Transmit power: ",OutputPower,"Watt")
                print("Antenna gain: ",AntennaGain)
                print("Modulation technique: ",Modtype)
                print("Error correction code: ",Codetype)
                print("")
                print("")
                count = count + 1
                
print("Number of budgets closed:",count,"of a total of",(len(caselst)*len(modlst)*len(codlst)),"budgets tested")
print("")
print("System noise temperature = ",np.round(SystemNoiseTemp,3),"K")           