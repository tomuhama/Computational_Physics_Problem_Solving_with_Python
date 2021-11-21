import vpython as vp

scene = vp.canvas(title='Motion of ball')
obj = vp.sphere(pos=vp.vector(-1,0,0),radius=0.1, color=vp.color.red, make_trail=True)

t=0
dt = 0.05
x0 = -1
v0 = 1.0

i =0
while t<2:
    vp.rate(10)
    x = x0+v0*t
    obj.pos=vp.vector(x,0,0)
    scene.capture('motion_of_ball00'+str(i).zfill(3))
    i+=1
    t+=dt

"""
import subprocess
subprocess.run("convert -delay 01 -loop 0 motion_of_ball*.png animation_mob.gif")
"""