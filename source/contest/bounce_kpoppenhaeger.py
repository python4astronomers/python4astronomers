figure(1)
clf()
size = 15
axis([-size, size, -size, size])

# Define properties
n = 10
pos1 = (np.linspace(10,10,20)).reshape(n, 2) # the bubbles
pos2 = (np.linspace(-10,-10,20)).reshape(n, 2) # the thorns

vel1 = (0.2 * normal(size=n*2)).reshape(n, 2)
vel2 = (0.5 * normal(size=n*2)).reshape(n, 2)

sizes1 = 500 * random_sample(n) + 150
sizes2 = ones(n) * 50

# Colors where each row is (Red, Green, Blue, Alpha).  Each can go
# from 0 to 1.  Alpha is the transparency.
colors1 = random_sample([n, 4])
colors2 = random_sample([n, 4])

# Draw all the circles and return an object ``circles`` that allows
# manipulation of the plotted circles.
circles   = scatter(pos1[:,0], pos1[:,1], marker='o', s=sizes1, c=colors1)
triangles = scatter(pos2[:,0], pos2[:,1], marker='^', s=sizes2, c=colors2)

boom = np.array([False] * n)
gone = 0.
angle = 0.

while gone < 10:
    pos1 = pos1 + vel1
    pos2 = pos2 + vel2
    bounce1 = abs(pos1) > size      # Find objects that are outside walls
    bounce2 = abs(pos2) > size
    vel1[bounce1] = -vel1[bounce1]  # Bounce if outside the walls
    vel2[bounce2] = -vel2[bounce2]
    position = [[size+5], [size+5]]
    for j in np.arange(0,n):        # Check if target has been hit
    	boom_new = np.sqrt( (pos1[j,0] - pos2[:,0])**2 + (pos1[j,1] - pos2[:,1])**2 ) < (sizes1[j]/240)
	if np.sum(boom_new) == 1:
		position =  [pos1[j,0], pos1[j,1]] # remember position where it was hit
		boom[j] = True # and remember which bubble was hit
	
    
    sizes1[boom] = 0                # If target was hit, let it vanish
    plt.plot(position[0], position[1], 'o', color='r',  markeredgecolor='r', markersize=5) # draw red dot at position of collision
    gone = np.sum(boom)          # How many bubbles have been hit so far
    circles.set_offsets(pos1)    # Change the positions
    triangles.set_offsets(pos2)
    angle = angle + 20
    triangles.set_transform(matplotlib.transforms.Affine2D().rotate_deg(angle)) # Let thorns spin
    draw()
