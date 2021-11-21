import vpython as vp
import numpy as np
from vpython.vpython import color

dx = 0.04
dx2 = dx*dx
k0 = 5.5*vp.pi
dt = dx2/20.0
xmax = 6.0
xs = vp.arange(-xmax,xmax+dx/2,dx)                     

g = vp.graph(width=500, height=250, title='Wave packet in HO Well')
PlotObj = vp.curve(x=xs, color=vp.color.red, radius=3, graph=g)
#g.center = (0,2,0) # Scene center

psr = np.exp(-0.5*(xs/0.5)**2)*np.cos(k0*xs)
psi = np.exp(-0.5*(xs/0.5)**2)*np.sin(k0*xs)
# psr = vp.exp(-0.5*(xs/0.5)**2) * vp.cos(k0*xs)                # Initial RePsi
# psi = vp.exp(-0.5*(xs/0.5)**2) * vp.sin(k0*xs)                # Initial ImPsi
v = 15.0*xs**2

i=0
while i<500:
    vp.rate(500)
    psr[1:-1] = psr[1:-1] - (dt/dx2)*(psi[2:] + psi[:-2]\
                        - 2*psi[1:-1]) + dt*v[1:-1]*psi[1:-1]
    psi[1:-1] = psi[1:-1] + (dt/dx2)*(psr[2:] + psr[:-2]\
                        - 2*psr[1:-1]) - dt*v[1:-1]*psr[1:-1]
    PlotObj.x = xs
    PlotObj.y = 4*(psr**2 + psi**2)
    i+=1