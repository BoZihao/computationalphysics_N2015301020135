import random as ra
import numpy as np
import pylab as plt
    
def flip():
    pu=np.exp(-(B+gamma*M0)/T)/(np.exp((B+gamma*M0)/T)+1+np.exp(-(B+gamma*M0)/T))
    p0=1/(np.exp((B+gamma*M0)/T)+1+np.exp(-(B+gamma*M0)/T))
    for i in range(N):
        r=ra.uniform(0,1)
        if 0<=r<pu:
            state[i]=1
        elif pu<=r<pu+p0:
            state[i]=0
        else:
            state[i]=-1

global state,B,T,N,M0,gamma,E
N=5000
gamma=0.1
state=[]
for i in range(N):
    state.append(-1)
B=0.9
T=0.1
dT=0.05
T0=[]
M=[]
Cm=[]
Ea=-N*B
for i in range(300):
    T0.append(T)
    Eold=1
    Enew=0
    k=0
    M0=0
    E=0
    while np.abs(Enew-Eold) > 5 or k < 3:
        k=k+1
        flip()
        for i in range(N):
            E=E+state[i]*(B+gamma*M0)
        Eold=Enew
        Enew=E
        for i in range(N):
            M0=M0+state[i]
    M.append(M0)
    Eb=E
    C_increase=np.abs((Eb-Ea)/dT)
    Cm.append(C_increase)
    Ea=Eb
    T=T+dT
plt.figure
plt.plot(T0,M,label="B=0.9")
plt.xlabel("T")
plt.ylabel("magnetic polarization")
plt.title("magnetic polarization versus Temerature")
plt.legend()
plt.show()

plt.figure
plt.plot(T0,Cm,label="B=0.9",color='orange')
plt.xlabel("T")
plt.ylabel("heat capacity")
plt.title("heat capacity versus Temerature")
plt.legend()
plt.show()    