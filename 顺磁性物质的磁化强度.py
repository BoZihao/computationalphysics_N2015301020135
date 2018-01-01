import random as ra
import pylab as plt
import numpy as np

def flip():
    pu=np.exp(-B/T)/(np.exp(B/T)+1+np.exp(-B/T))
    p0=1/(np.exp(B/T)+1+np.exp(-B/T))
    for i in range(N):
        r=ra.uniform(0,1)
        if 0<=r<pu:
            state[i]=1
        elif pu<=r<pu+p0:
            state[i]=0
        else:
            state[i]=-1

global state,B,T,N
N=50000
state=[]
for i in range(N):
    state.append(-1)
T=0.1
dT=0.05
B=1.5
T0=[]
M=[]
Cm=[]
Ea=-N*B
for i in range(300):
    E=0
    B0=0
    T0.append(T)
    flip()
    for i in range(N):
        B0=B0+state[i]
    M.append(B0)
    for i in range(N):
        E=E+state[i]*B
    Eb=E
    C_increase=np.abs((Eb-Ea)/dT)
    Cm.append(C_increase)
    Ea=Eb
    T=T+dT

plt.figure
plt.plot(T0,M,label="B=1.5")
plt.xlabel("T")
plt.ylabel("magnetic polarization")
plt.title("magnetic polarization versus Temerature")
plt.legend()
plt.show()

plt.figure
plt.plot(T0,Cm,label="B=1.5",color='orange')
plt.xlabel("T")
plt.ylabel("heat capacity")
plt.title("heat capacity versus Temerature")
plt.legend()
plt.show()