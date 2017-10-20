import math
import matplotlib.pyplot as plt

g=9.8
omega=4000*math.pi/60
vd=35
v_wind=3
Delta=5
S0m=0.00041

class baseball:
    def __init__(self,v0,theta,yFinal=0):
        self.x0=0
        self.y0=1.8
        self.yFinal=yFinal
        self.v0=v0
        self.Theta=theta
        self.theta=theta*math.pi/180
        self.vx0=self.v0*math.cos(self.theta)
        self.vy0=self.v0*math.sin(self.theta)
        self.dt=0.01
        return None
    
    def B2m(self,v):
        return 0.0039+0.0058/(1+math.exp(v-vd/Delta))
    def F(self,vx,vy):
        vxy=math.sqrt(vx**2+vy**2)
        Fx=-self.B2m(vxy)*math.sqrt((vx-v_wind)**2+vy**2)*(vx-v_wind)-S0m*omega*vy
        Fy=-self.B2m(vxy)*math.sqrt((vx-v_wind)**2+vy**2)*vy+S0m*omega*vx
        return Fx,Fy
    def FF(self,vx,vy):
        vxy=math.sqrt(vx**2+vy**2)
        FFx=-self.B2m(vxy)*math.sqrt((vx-v_wind)**2+vy**2)*(vx-v_wind)
        FFy=-self.B2m(vxy)*math.sqrt((vx-v_wind)**2+vy**2)*vy
        return FFx,FFy
    def fly(self):
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        while not (self.Y[-1]<self.yFinal and self.Vy[-1]<0):
            newVx=self.Vx[-1]+self.F(vx=self.Vx[-1],vy=self.Vy[-1])[0]*self.dt
            newVy=self.Vy[-1]-g*self.dt+self.F(self.Vx[-1],self.Vy[-1])[1]*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            meanVx=0.5*(self.Vx[-1]+self.Vx[-2])
            meanVy=0.5*(self.Vy[-1]+self.Vy[-2])
            newX=self.X[-1]+meanVx*self.dt
            newY=self.Y[-1]+meanVy*self.dt
            self.X.append(newX)
            self.Y.append(newY)
        self.X[-1]=((self.Y[-2]-self.yFinal)*self.X[-1]+(self.yFinal-self.Y[-1])*self.X[-2])/(self.Y[-2]-self.Y[-1])
        self.Y[-1]=self.yFinal
        return 0
    def FFly(self):
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        while not (self.Y[-1]<self.yFinal and self.Vy[-1]<0):
            newVx=self.Vx[-1]+self.FF(vx=self.Vx[-1],vy=self.Vy[-1])[0]*self.dt
            newVy=self.Vy[-1]-g*self.dt+self.FF(self.Vx[-1],self.Vy[-1])[1]*self.dt
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            meanVx=0.5*(self.Vx[-1]+self.Vx[-2])
            meanVy=0.5*(self.Vy[-1]+self.Vy[-2])
            newX=self.X[-1]+meanVx*self.dt
            newY=self.Y[-1]+meanVy*self.dt
            self.X.append(newX)
            self.Y.append(newY)
        self.X[-1]=((self.Y[-2]-self.yFinal)*self.X[-1]+(self.yFinal-self.Y[-1])*self.X[-2])/(self.Y[-2]-self.Y[-1])
        self.Y[-1]=self.yFinal
        return 0
    def distance(self):
        return self.X[-1]
    def height(self):
        return max(self.Y)
    def plot_2d(self, color):
        plt.plot(self.X,self.Y,color,label="$%dm/s$,$%d\degree$, with backspin"%(self.v0,self.Theta))
        legend(loc='best')
        return 0

import numpy as np

theta=np.linspace(15,75,12)
f = []
L = []
for i in range (len(theta)):
    k=baseball(40,theta[i],0)
    j=baseball(40,theta[i],0)
    k.fly()
    j.FFly()
    plt.plot(k.X,k.Y,label=r'$\theta=%.2f^\circ$'%theta[i])
    plt.xlabel('x/m')
    plt.ylabel('y/m')
    plt.xlim(0,150)
    plt.ylim(0,70)
    plt.title('the trajectory of baseball at different initial angles')
    plt.legend(loc='best',frameon=False)
    f.append(k.X[-1])
    L.append(j.X[-1])
    
plt.show()

phi=np.linspace(15,75,12)
width=2
plt.bar(phi,f,width,color='B',alpha=0.5)
plt.bar(phi,L,width,color='r',alpha=0.5)
plt.xlabel('initial angles/$^\circ$')
plt.ylabel('the maximum range/m')
plt.title('the maximum ranges at different initial angles')
plt.show()