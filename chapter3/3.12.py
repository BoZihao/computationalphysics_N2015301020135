import math
import matplotlib.pyplot as plt  
import numpy as np

g=9.8
l=9.8
w0=0
x0=0.2
t0=0
q=0.5
dt=0.04
D=2/3

def Damped(omega0,theta0,q,l,T):
    dt=0.001
    t=0
    omega,theta = omega0,theta0
    motion=[[]for i in range(3)]
    motion[0].append(omega)
    motion[1].append(theta)
    motion[2].append(t)
    while t<= T:
        omega = omega+(-g*theta/l-q*omega)*dt
        theta = theta+omega*dt
        t = t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion

class pendulum:
    def __init__(self,F):
        self.F=F
        self.w=[w0]
        self.x=[x0]
        self.t=[t0]
        self.delta=[0.]

    def update(self):
        current_w=self.w[-1]
        current_x=self.x[-1]
        current_t=self.t[-1]
        self.next_w=current_w-(g/l*np.sin(current_x)+q*current_w-self.F*np.sin(D*current_t))*dt
        self.next_x=current_x+self.next_w*dt
        self.next_t=current_t+dt
        self.next_delta=self.next_x-current_x

    def fire(self):
        while (self.t[-1]<=60):
            self.update()
            self.w.append(self.next_w)
            self.x.append(self.next_x)
            self.t.append(self.next_t)
            self.delta.append(self.next_delta)

        plt.plot(self.t,self.delta,label="F="+str(self.F))

class Pendulum:
    def __init__(self,w,x,t,F):
        self.w=[w]
        self.x=[x]
        self.t=[t]
        self.F=F
    def update(self):
        global g,dt,l
        current_w=self.w[-1]
        current_x=self.x[-1]
        current_t=self.t[-1]
        self.next_w=current_w-(g/l*np.sin(current_x)+q*current_w-self.F*np.sin(D*current_t))*dt
        self.next_x=current_x+self.next_w*dt
        self.next_t=current_t+dt
		
    def fire(self):
        while (self.t[-1]<=1000):
            self.update()
            if self.next_x>np.pi:self.next_x+=-2*np.pi
            else:
                if self.next_x<-np.pi:self.next_x+=2*np.pi
                else:self.next_x=self.next_x
            self.w.append(self.next_w)
            self.x.append(self.next_x)
            self.t.append(self.next_t)

        plt.plot(self.x,self.w,',')

class pendulumm:
    def __init__(self,w,x,t,F):
        self.w=[w]
        self.x=[x]
        self.t=[t]
        self.F=F
        self.chosen_w=[]
        self.chosen_x=[]
        self.chosen_t=[]

    def update(self):
        global g,dt,l
        current_w=self.w[-1]
        current_x=self.x[-1]
        current_t=self.t[-1]
        self.next_w=current_w-(g/l*np.sin(current_x)+q*current_w-self.F*np.sin(D*current_t))*dt
        self.next_x=current_x+self.next_w*dt
        self.next_t=current_t+dt
		
    def fire(self):
        while (self.t[-1]<=10000):
            self.update()
            if self.next_x>np.pi:self.next_x+=-2*np.pi
            else:
                if self.next_x<-np.pi:self.next_x+=2*np.pi
                else:self.next_x=self.next_x
            self.w.append(self.next_w)
            self.x.append(self.next_x)
            self.t.append(self.next_t)
            test=((self.t[-1]*D)%np.pi)/np.pi
            test2=self.t[-1]-int(self.t[-1]/np.pi)*np.pi
            if (test<=0.01):
                if (test2<=1):
                    self.chosen_x.append(self.next_x)
                    self.chosen_w.append(self.next_w)
                    self.chosen_t.append(self.next_t)
                else:
                    pass
            else:
                pass

        plt.plot(self.chosen_x,self.chosen_w,',')

d=Damped(0,0.5,0.1,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=0.1')
d=Damped(0,0.5,1,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=1')
d=Damped(0,0.5,9.8,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q='+r'$2\sqrt{g/l}$')
d=Damped(0,0.5,20,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=20')
d=Damped(0,0.5,100,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=100')
plt.xlim(0,10)
plt.ylim(-0.5,1)
plt.grid(True,color='k')
plt.title('Damped Pendulum')
plt.xlabel('Time/s')
plt.ylabel(r'$\theta$/rad')
plt.legend()
plt.show()

d=Damped(0,0.5,0.1,1,80)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='q=0.1')
plt.xlim(0,80)
plt.ylim(-0.5,0.5)
plt.grid(True,color='k')
plt.title('Damped Pendulum')
plt.xlabel('Time/s')
plt.ylabel(r'$\theta$/rad')
plt.legend()
plt.show()

A=pendulum(0)
A.fire()
B=pendulum(0.5)
B.fire()
C=pendulum(1)
C.fire()
plt.xlim(0,60)
plt.legend(loc="best")
plt.xlabel("Time/s")
plt.ylabel(r'$\theta$/rad')
plt.show()
C=pendulum(1.2)
C.fire()
C=pendulum(1.4)
C.fire()
E=pendulum(1.6)
E.fire()
plt.xlim(0,60)
plt.legend(loc="best")
plt.xlabel("Time/s")
plt.ylabel(r'$\theta$/rad')
plt.show()
E=pendulum(2)
E.fire()
E=pendulum(2.1)
E.fire()
E=pendulum(2.2)
E.fire()
plt.xlim(0,60)
plt.legend(loc="best")
plt.xlabel("Time/s")
plt.ylabel(r'$\theta$/rad')
plt.show()
E=pendulum(3)
E.fire()
E=pendulum(5)
E.fire()
E=pendulum(10)
E.fire()
plt.xlim(0,60)
plt.legend(loc="best")
plt.xlabel("Time/s")
plt.ylabel(r'$\theta$/rad')
plt.show()

a=Pendulum(0,3,0,0.5)
a.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
b=Pendulum(0,3,0,1)
b.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
c=Pendulum(0,3,0,1.2)
c.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
o=Pendulum(0,3,0,1.5)
o.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
d=Pendulum(0,3,0,1.6)
d.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
e=Pendulum(0,3,0,1.8)
e.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
f=Pendulum(0,3,0,2)
f.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
h=Pendulum(0,3,0,2.1)
h.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
j=Pendulum(0,3,0,2.2)
j.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
k=Pendulum(0,3,0,3)
k.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
aa=Pendulum(0,3,0,5)
aa.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
bb=Pendulum(0,3,0,10)
bb.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()

a=pendulumm(0,3,0,0.5)
a.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
b=pendulumm(0,3,0,1)
b.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
c=pendulumm(0,3,0,1.2)
c.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
o=pendulumm(0,3,0,1.5)
o.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
d=pendulumm(0,3,0,1.6)
d.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
e=pendulumm(0,3,0,1.8)
e.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
f=pendulumm(0,3,0,2)
f.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
h=pendulumm(0,3,0,2.1)
h.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
j=pendulumm(0,3,0,2.2)
j.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
k=pendulumm(0,3,0,3)
k.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
aa=pendulumm(0,3,0,5)
aa.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()
aa=pendulumm(0,3,0,10)
aa.fire()
plt.xlabel(r'$\theta$(rad)')
plt.ylabel(r'$\omega$(rad/s)')
plt.show()