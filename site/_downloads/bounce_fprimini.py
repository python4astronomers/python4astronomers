from numpy.random import random, normal
figure(4)
clf()
axis([-10, 10, -10, 10])

# Define properties of the "bouncing balls"
n = 10
pos = (20 * random(n*2) - 10).reshape(n, 2)
vel = (0.3 * normal(size=n*2)).reshape(n, 2)
sizes = normal(200, 100, size=n)

# Colors where each row is (Red, Green, Blue, Alpha).  Each can go
# from 0 to 1.  Alpha is the transparency.
colors = random([n, 4])

# Draw all the circles and return an object ``circles`` that allows
# manipulation of the plotted circles.
circles=scatter(pos[:,0], pos[:,1], marker=(5,0,1), s=sizes, c=colors)
   

for i in range(100):
    pos = pos + vel
    bounce = abs(pos) > 10      # Find balls that are outside walls
    vel[bounce] = -vel[bounce]  # Bounce if outside the walls
    clf()
    axis([-10, 10, -10, 10])
    scatter(pos[:,0], pos[:,1], marker=(5,0,i), s=sizes, c=colors)
    draw()
#    circles.set_offsets(pos)    # Change the positions
#    draw()
