import math # scientist
import matplotlib.pyplot as plt

x = 0   # distance horiziontale
y = 10   # hauteur
vx = 10   # on lance fort ?
vy = 1   # on jette fort ?
g = 10  # on est sur Terre ?
m = 10  # masse de l'objet
dt = 1  # have you buy the 12900ks ?
# if yes ur so dumb

def eval(x :int, y :int, vx :int, vy :int, g :int, m :int, dt :int):# -> also int
    """ renvoyer la position et la vitesse de l'objet 
    après chaque unité de temps """
    x = x + vx * dt
    y = y + vy * dt
    #vx+1 = vxi
    vy = vy - g * dt
    return (x,y,vx,vy)


t0 = 0  # big bang
t_fin = 10  # big boom 
tt = []   # it's better then that big rip anyway ok
xx = []
yy = []
for t in range(t0,t_fin,dt):
    tt.append(t)
    x, y, vx, vy = eval(x, y, vx, vy, g, m, dt)
    xx.append(x)
    yy.append(y)

plt.plot(xx,yy)
plt.show()
