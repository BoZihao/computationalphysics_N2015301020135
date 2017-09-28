import matplotlib.pyplot as plt
import numpy as np

v=[]
t=[]
a=10
b=1
dt=0.05
endtime=15
v.append(0)
t.append(0)
t_theory = np.linspace(0,15,1000)
v_theory = -a/b*np.exp(-b*t_theory)+a/b
for i in range(int(endtime/dt)):
	v.append(v[i]+(a-b*v[i])*dt)
	t.append(t[i]+dt)
	print(t[-1] ,v[-1])

plt.figure(figsize=(10,5))
plt.plot(t_theory,v_theory,label="exact solution",color="red",linewidth=1)
plt.plot(t,v,label="Euler method",color="green",linewidth=2,linestyle='--')
plt.title('the velocity of a parachutist')
plt.xlabel('t(s)')
plt.ylabel('v(m/s)')
plt.show()