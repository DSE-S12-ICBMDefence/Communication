# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:17:30 2020

@author: Coen
"""

import numpy as np

# Boltzmann constant and speed of light
kb = 1.3807e-23
c = 2.998e8

distance = 900000               # Distance between satellites in meters
freq = 2.2e9                    # Frequency in GHz
lamb = c/(freq)                 # wavelenght in meters
rxAntennaGain = 5.              # gain in dB
txAntennaGain = 5.              # gain in dB
polarizationLoss = 0.           # losses in dB
transmitterLosses = 1.2         # losses in dB
outputPower = 2.                # power in W
SystemNoiseTemp = 1228          # System noise temperature in Kelvin
GoverT = rxAntennaGain-(10*np.log10(SystemNoiseTemp)) # rx G/T in dB
EbN0threshold = 2.5             # Eb/N0 threshold for concatenated code + BPSK with BER = 10^-6
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
rxSignalAntenna = rxSignal + rxAntennaGain

# Signal to noise ratio (SNR)
SNR = rxSignal + GoverT - 10*np.log10(kb)

# Eb/N0 calculated at the receiver
EbN0 = SNR - 10*np.log10(bitrate)

# full link budget including link margin
margin = EbN0 - EbN0threshold - implementationLoss - linkMargin

print("margin =",margin)