from vpython import *

string = 'blue : sin^2(x), white: cos^2(x)/3, red: sin(x)*cos(x)'
graph1 = graph(title=string, xtitle='x', ytitle='y')

y1 = gcurve(color=color.yellow)
y2 = gvbars(color=color.green)
y3 = gdots(color=color.red, radius=1)

for x in arange(-5,5,0.1):
    y1.plot(pos=(x, sin(x)*sin(x)))
    y2.plot(pos=(x, cos(x)*cos(x)/3.0))
    y3.plot(pos=(x, sin(x)*cos(x)))