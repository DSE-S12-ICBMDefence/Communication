# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:45:42 2020

@author: Coen
"""
'''
Inputs needed:
    SNR 
    Transmitter gain Gt 
    Receiver gain Gr 
    distance d 
    frequency f 
    system noise temperatuer Ts
    3 Different data rates are used to calculate the required transmitter power:
        1 kbit/s
        250 kbit/s
        1 Mbit/s

The tool will spit out transmit power required to complete the link budget
for each data rate and gain you put in, aka the outputs:
    Transmit power

This tool is verified with the paper: 
Power Budgets for CubeSat Radios to Support Ground Communications and Inter-Satellite Links

'''
import numpy as np
import matplotlib.pyplot as plt

def SNRC(Eb,N0,R,Bw):
    SNR = 10*np.log10(Eb/N0) + 10*np.log10(R/Bw)
    return SNR

def Shannon(Bw,SNR):
    C = Bw*np.log2(1+(10**(SNR/10)))
    return C

def Gain(dant,c,f):
    A = np.pi/4*dant*dant
    lamb = c/f
    print(lamb)
    G = 4*np.pi*A/(lamb*lamb)
    return 10*np.log10(G)

def Pw2Pdbm(P):
    Pdbm = 10*np.log10(1000*P)
    return Pdbm

def tempc(Tant,Lr,T0,F):
    Tr = T0/Lr*(F-Lr)
    Ts = Tant + Tr
    return Ts

def Lpcalc(d,f,c):
    Lp = (4*np.pi*(d*1000)*f/c)**2
    return Lp


for i in [5.]:          #This is the list with gains you can change accordingly
    SNR  = 9.5          #[dB]       #All input parameter that are kept the same over-
#    Pt   = 4.0          #[W]       #- all different calculations.
    Gt   = i           #[dBi]
    Gr   = i           #[dBi]
    d    = 900.         #[km]
    f    = 2.2*10**9   #[Hz]
    Ts   = 1250.        #[K]
    #dant = 0.09        #[m]
    Bw   = 25000        #[HZ]

    Rl   = 20000       #[bit/s]     #Data rates can be altered as well
    Rm   = 250000       #[bit/s]
    Rh   = 1000000       #[bit/s]
    
    
    '''
    Tant = 150          #[K]    
    T0   = 290.         #[K]
    Lr   = 0.5
    F    = 5.           #[dB]
    '''
    k    = 1.38*10**(-23)    #[J/K]
    c    = 299792458.0       #[m/s] 
    
    
#    Ptdbm = Pw2Pdbm(Pt)
#    print("Pt =",np.round(Ptdbm,2)," dBm")
    
    Lp = 10*np.log10(Lpcalc(d,f,c)) #[dB]
#    print("Lp =",np.round(Lp,2)," dB")

#Gtr = Gain(dant,c,f)
#print("Gtr =",np.round(Gtr,2)," dB")

    Lo = 4 #dB --> 2 dB for all other propagation losses and 2 for the link margin
    
#    R = 10**((Ptdbm - 30 - 0.2 + Gt + Gr - Lp - Lo -(10*np.log10(k)+0.6) - 10*np.log10(Ts) - SNR)/10) #bit/s
#    print("R =",np.round(R/1000,3)," kbit/s")
    Rlim = Shannon(Bw,SNR)
#    print("Rlim =",np.round(Rlim/1000,3)," kbit/s")
    
    
    print("Gain =",i,"dB")
    Plow = 0.2 - Gt - Gr + Lp + Lo + (10*np.log10(k)+0.6) + 10*np.log10(Ts) + 10*np.log10(Rl) + SNR
    print("Low bitrate power: ",np.round(10**(Plow/10),5)," W")
    
    Pmed = 0.2 - Gt - Gr + Lp + Lo + (10*np.log10(k)+0.6) + 10*np.log10(Ts) + 10*np.log10(Rm) + SNR
    print("Med bitrate power: ",np.round(10**(Pmed/10),3)," W")
    
    Phigh =  0.2 - Gt - Gr + Lp + Lo + (10*np.log10(k)+0.6) + 10*np.log10(Ts) + 10*np.log10(Rh) + SNR
    print("High bitrate power: ",np.round(10**(Phigh/10),3)," W")
    
    print("")

'''
c    = 299792458.0       #[m/s]
Freqlst = np.arange(0.03,30.,0.1)

Pathloss = np.zeros(len(Freqlst))

for i in range(0,len(Freqlst)):
    Pathloss[i] = Lpcalc(1000,Freqlst[i]*10**9,c)

PathlossdB = -10*np.log10(Pathloss) #[dB]


plt.close("all")  

f2 = plt.figure()
plt.plot(Freqlst,-Pathloss)
plt.xlabel("Frequency in GHz")
plt.ylabel("Path loss absolute")
plt.grid()
  
f1 = plt.figure()
plt.plot(Freqlst,PathlossdB)
plt.xlabel("Frequency in GHz")
plt.ylabel("Path loss in dB")
plt.grid()
plt.show()


'''


'''
#------------------------Verification to table 7 of paper----------------------------------------------------
Uncomment this part to get the verification calculations that match up with the paper

SNR  = 9.6         #[dB]
Pt   = 0.03162      #[W]
Gt   = 5.          #[dBi]
Gr   = 5.        #[dBi]
d    = 10.         #[km]
f    = 2.45*10**9    #[Hz]
Ts   = 1250.        #[K]
#dant = 0.09         #[m]

'''
'''
Tant = 150          #[K]    
T0   = 290.         #[K]
Lr   = 0.5
F    = 5.           #[dB]
'''
''' 
k    = 1.38*10**(-23)    #[J/K]
c    = 299792458.0       #[m/s]  

def Gain(dant,c,f):
    A = np.pi/4*dant*dant
    lamb = c/f
    G = 4*np.pi*A/(lamb*lamb)
    return 10*np.log10(G)

def Pw2Pdbm(P):
    Pdbm = 10*np.log10(1000*P)
    return Pdbm

def tempc(Tant,Lr,T0,F):
    Tr = T0/Lr*(F-Lr)
    Ts = Tant + Tr
    return Ts

def Lpcalc(d,f,c):
    Lp = (4*np.pi*(d*1000)*f/c)**2
    return Lp

Ptdbm = Pw2Pdbm(Pt)
print("Pt =",np.round(Ptdbm,2)," dBm")

Lp = 10*np.log10(Lpcalc(d,f,c)) #[dB]
print("Lp =",np.round(Lp,2)," dB")

#Gtr = Gain(dant,c,f)
#print("Gtr =",np.round(Gtr,2)," dB")

Lo = 2 #dB --> all other propagation losses

R = 10**((Ptdbm - 30 - 0.2 + Gt + Gr - Lp - Lo -(10*np.log10(k)+0.6) - 10*np.log10(Ts) - SNR)/10) #bit/s
print("R =",np.round(R/1000000,3)," Mbit/s")

''' 

      