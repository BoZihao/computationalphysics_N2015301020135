import math
import matplotlib.pyplot as plt

a=10
b=8./3.

class Position():
    def __init__(self,_r,_x0=1,_y0=0,_z0=0,_t0=0,_time=60,_dt=0.0001):
        self.x=[_x0]
        self.y=[_y0]
        self.z=[_z0]
        self.t=[_t0]
        self.r=_r
        self.time=_time
        self.dt=_dt
        self.n=int(self.time/self.dt)
    def calculate(self):
        for i in range(self.n):
            self.x.append(self.x[-1]+a*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot(self,color):
        plt.plot(self.t,self.z,color,label='r=$%d$'%self.r)
'''
A=Position(10)
A.calculate()
A.plot('r')
B=Position(20)
B.calculate()
B.plot('b')
C=Position(30)
C.calculate()
C.plot('g')
plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.show()

A=Position(50)
A.calculate()
A.plot('y')
plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.show()

B=Position(80)
B.calculate()
B.plot('orange')
plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.show()

A=Position(110)
A.calculate()
A.plot('y')
plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.show()

B=Position(140)
B.calculate()
B.plot('orange')
plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.show()

A=Position(145)
A.calculate()
A.plot('purple')
plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.show()

B=Position(155)
B.calculate()
B.plot('black')
plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.show()

A=Position(160)
A.calculate()
A.plot('r')
plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.show()

B=Position(165)
B.calculate()
B.plot('b')
plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.show()

'''

class Posi():
    def __init__(self,_r,_x0=1,_y0=0,_z0=0,_t0=0,_time=60,_dt=0.0001):
        self.x=[_x0]
        self.y=[_y0]
        self.z=[_z0]
        self.t=[_t0]
        self.r=_r
        self.time=_time
        self.dt=_dt
        self.n=int(self.time/self.dt)
    def calculate(self):
        for i in range(self.n):
            self.x.append(self.x[-1]+a*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot_zx(self,color):
        plt.plot(self.x,self.z,color)
    def plot_zy(self,color):
        plt.plot(self.y,self.z,color)

'''
fig=plt.figure(figsize=(8,12))
ax1=plt.subplot(211)
A=Posi(30)
A.calculate()
A.plot_zx('r-')
plt.title('Phase space plot:z vetsus x')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()

ax2=plt.subplot(212)
B=Posi(30)
B.calculate()
B.plot_zy('r-')
plt.title('Phase space plot:z vetsus y')
plt.xlabel('y')
plt.ylabel('z')
plt.legend()

plt.show()

fig=plt.figure(figsize=(8,12))
ax1=plt.subplot(211)
A=Posi(80)
A.calculate()
A.plot_zx('r-')
plt.title('Phase space plot:z vetsus x')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()

ax2=plt.subplot(212)
B=Posi(80)
B.calculate()
B.plot_zy('r-')
plt.title('Phase space plot:z vetsus y')
plt.xlabel('y')
plt.ylabel('z')
plt.legend()

plt.show()

fig=plt.figure(figsize=(8,12))
ax1=plt.subplot(211)
A=Posi(140)
A.calculate()
A.plot_zx('r-')
plt.title('Phase space plot:z vetsus x')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()

ax2=plt.subplot(212)
B=Posi(140)
B.calculate()
B.plot_zy('r-')
plt.title('Phase space plot:z vetsus y')
plt.xlabel('y')
plt.ylabel('z')
plt.legend()

plt.show()

fig=plt.figure(figsize=(8,12))
ax1=plt.subplot(211)
A=Posi(150)
A.calculate()
A.plot_zx('r-')
plt.title('Phase space plot:z vetsus x')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()

ax2=plt.subplot(212)
B=Posi(150)
B.calculate()
B.plot_zy('r-')
plt.title('Phase space plot:z vetsus y')
plt.xlabel('y')
plt.ylabel('z')
plt.legend()

plt.show()

fig=plt.figure(figsize=(8,12))
ax1=plt.subplot(211)
A=Posi(165)
A.calculate()
A.plot_zx('r-')
plt.title('Phase space plot:z vetsus x')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()

ax2=plt.subplot(212)
B=Posi(165)
B.calculate()
B.plot_zy('r-')
plt.title('Phase space plot:z vetsus y')
plt.xlabel('y')
plt.ylabel('z')
plt.legend()

plt.show()
'''
class Bifujian():
    def __init__(self,_r,_x0=1,_y0=0,_z0=0,_t0=0,_time=500,_dt=0.001):
        self.x=[_x0]
        self.y=[_y0]
        self.z=[_z0]
        self.t=[_t0]
        self.r=_r
        self.time=_time
        self.dt=_dt
        self.n=int(self.time/self.dt)
    def calculate(self):
        for i in range(self.n):
            self.x.append(self.x[-1]+a*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot_zy(self):
        y_section=[]
        z_section=[]
        for i in range(len(self.t)):
            if abs(self.x[i]-0.)<4E-3:
                y_section.append(self.y[i])
                z_section.append(self.z[i])
        plt.plot(y_section,z_section,'ok',markersize=2)
    def plot_zx(self):
        x_section=[]
        z_section=[]
        for i in range(len(self.t)):
            if abs(self.y[i]-0.)<4E-3:
                x_section.append(self.x[i])
                z_section.append(self.z[i])
        plt.plot(x_section,z_section,'ok',markersize=2)
'''
plt.figure(figsize=(8,8))
a1=plt.subplot(211)
A=Bifujian(160)
A.calculate()
A.plot_zy()
plt.title('Phase space plot:r=160 z vetsus y when x=0')
plt.xlabel('y')
plt.xlim(-40,40)
plt.ylabel('z')
plt.legend()

a2=plt.subplot(212)
B=Bifujian(160)
B.calculate()
B.plot_zx()
plt.title('Phase space plot:r=160 z vetsus x when y=0')
plt.xlabel('x')
plt.ylabel('z')
plt.xlim(-40,40)
plt.legend()
'''

plt.figure(figsize=(8,8))
a1=plt.subplot(211)
A=Bifujian(150)
A.calculate()
A.plot_zy()
plt.title('Phase space plot:r=150 z vetsus y when x=0')
plt.xlabel('y')
plt.ylabel('z')
plt.xlim(-20,20)
plt.legend()

a2=plt.subplot(212)
B=Bifujian(150)
B.calculate()
B.plot_zx()
plt.title('Phase space plot:r=150 z vetsus x when y=0')
plt.xlabel('x')
plt.ylabel('z')
plt.xlim(-20,20)
plt.legend()