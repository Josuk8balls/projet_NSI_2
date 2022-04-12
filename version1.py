import math
import matplotlib.pyplot as plt
 
m=int(input("masse :"))
v0=int(input("vitesse initiale :"))
g=int(input("pesanteur :"))
k=int(input("altitude :"))

def eqa_dx(angle):
    alpha = angle*math.pi/180
    v0x=v0*math.cos(alpha)
    v0y=v0*math.sin(alpha)
    dt = 0.01
    dx = 0
    dy = 0
    while True:
        vX=(-1/m)*(k*v0x)*dt
        vY=(-1/m)*(m*g+k*v0y)*dt
        v0x += vX
        v0y += vY
        dx += v0x*dt
        dy += v0y*dt
        if dy<0:
            return dx
 
xx = []
yy = []
for i in range(10,80,5):
    xx.append(i)
    yy.append(eqa_dx(i))
 
plt.plot(xx,yy)
plt.show()
