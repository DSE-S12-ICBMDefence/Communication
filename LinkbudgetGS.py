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
    
    distance = 2400e3               # Distance between satellites in meters
    lamb = c/(freq)                 # wavelenght in meters
    txAntennaGain = 0.   # gain in dB
    polarizationLoss = 0.           # losses in dB
    transmitterLosses = 1.2         # losses in dB
    outputPower = 0.5               # power in W
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

case1 = [400e6, 50e3, 15.]

mod1  = ['QPSK', 1.4 , 10.5 ]

code1 = ['Convulational2', 0.5, 6]

Freq, MaxBandwidth, AntennaGain = case1
Modtype, SE, EbN0mod = mod1
Codetype, Coderate, CodeGain = code1
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

print("System noise temperature = ",np.round(SystemNoiseTemp,3),"K")