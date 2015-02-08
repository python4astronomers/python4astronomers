figure(3)
clf()
axis([-10, 10, -10, 10])

# Define properties of the "bouncing balls"
n = 10
pos = (20 * random_sample(n*2) - 10).reshape(n, 2)
vel = (0.3 * normal(size=n*2)).reshape(n, 2)
sizes = normal(400, 100, size=n)

# Colors where each row is (Red, Green, Blue, Alpha).  Each can go
# from 0 to 1.  Alpha is the transparency.
colors = random_sample([n, 4])

# Draw all the circles and return an object ``circles`` that allows
# manipulation of the plotted circles.
circles = scatter(pos[:,0], pos[:,1], marker=[15,1,0], s=sizes, c=colors)
angle=0
grow=1
for i in range(300):
    pos = pos + vel
    bounce = abs(pos) > 10      # Find balls that are outside walls
    vel[bounce] = -vel[bounce]  # Bounce if outside the walls
    angle=angle+5
    #scalefactor=201/(1+pos[:,0]**2+pos[:,1]**2)
    grow=grow*1.01
    circles.set_transform(matplotlib.transforms.Affine2D().rotate_deg(angle).scale(grow))     
    circles.set_offsets(pos)    # Change the positions
    draw()
