# see http://python4astronomers.github.com/contest/bounce.html
figure(1)
clf()
axis([-10, 10, -10, 10])

# Define properties of the "bouncing balls"
n = 10
pos = (20 * random_sample(n*2) - 10).reshape(n, 2)
vel = (0.3 * normal(size=n*2)).reshape(n, 2)
sizes = 100 * random_sample(n) + 100

# Colors where each row is (Red, Green, Blue, Alpha).  Each can go
# from 0 to 1.  Alpha is the transparency.
colors = random_sample([n, 4])

# Draw all the circles and return an object ``circles`` that allows
# manipulation of the plotted circles.
circles = scatter(pos[:,0], pos[:,1], marker='o', s=sizes, c=colors)

# gravity-like force in -y direction
grav = -0.1*ones(20).reshape(n,2)
grav[:,0] = 0.
dt = 0.2
dt2 = dt**2
ax = gca()
ax.set_xlim((-11.,11.))
ax.set_ylim((-11.,11.))
for i in range(1000):
    # repulsive force from walls at y = +11 and -11
    frep = 0.1*(-1./(pos[:,0] - 11.)**2 + 1./(11. + pos[:,0])**2)
    frep = array(zip(frep,zeros(n)))
    pos = pos + vel*dt + 0.5*(grav + frep)*dt2
    vel = vel + (grav + frep)*dt
    bounce = abs(pos) > 10      # Find balls that are outside walls
    vel[bounce] = -vel[bounce]  # Bounce if outside the walls
    circles.set_offsets(pos)    # Change the positions
    # circles change color after bouncing
    cc = where(bounce)[0]
    if len(cc) > 0:
        for j in cc:
            colors[j,0:3] = 1. - colors[j,0:3]
    draw()

