figure(1)
clf()
axis([-10, 10, -10, 10])

# Define properties of the "bouncing balls"
n = 50
pos = (20 * random_sample(n*2) - 10).reshape(n, 2)
vel = (0.1 * normal(size=n*2)).reshape(n, 2)
sizes = 100 * random_sample(n) + 100

# Colors where each row is (Red, Green, Blue, Alpha).  Each can go
# from 0 to 1.  Alpha is the transparency.
colors = random_sample([n, 4])
colors[:,3] = 0.0

# Draw all the circles and return an object ``circles`` that allows
# manipulation of the plotted circles.
circles = scatter(pos[:,0], pos[:,1], marker='o', s=sizes, c=colors)

for i in range(300):

    # Add a gravitational field towards the center
    d = np.sqrt(pos[:,0]**2 + pos[:,1]**2)
    ax = - 1. / (3. + d**2) * pos[:,0] / d / 5.
    ay = - 1. / (3. + d**2) * pos[:,1] / d / 5.
    vel[:,0] += ax
    vel[:,1] += ay

    # Slowly decrease the alpha
    colors[:,3] = 3. / (3. + d**2)
    
    # Update positions
    pos = pos + vel

    # Find balls that are outside walls
    bounce = abs(pos) > 10

     # Warp to other side
    pos[bounce] = -pos[bounce]
    
    circles.set_offsets(pos)    # Change the positions
    circles.set_facecolors(colors)    # Change the positions

    draw()
