#!/usr/bin/env python

from pylab import *

figure(1)
clf()
axis([-10, 10, -10, 10])

n = 10
pos = (20 * random(n*2) - 10).reshape(n, 2)
vel = (0.3 * normal(size=n*2)).reshape(n, 2)
colors = random([n, 4])
sizes = normal(200, 100, size=n)

circles = scatter(pos[:,0], pos[:,1], marker='o', s=sizes, c=colors)
for i in range(100):
    pos = pos + vel
    bounce = abs(pos) > 10
    vel[bounce] = -vel[bounce]
    circles.set_offsets(pos)
    draw()

    
