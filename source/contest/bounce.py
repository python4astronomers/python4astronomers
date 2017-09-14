import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
plt.clf()
plt.axis([-10, 10, -10, 10])

# Define properties of the "bouncing balls"
n = 10
pos = (20 * np.random.sample(n*2) - 10).reshape(n, 2)
vel = (0.3 * np.random.normal(size=n*2)).reshape(n, 2)
sizes = 100 * np.random.sample(n) + 100

# Colors where each row is (Red, Green, Blue, Alpha).  Each can go
# from 0 to 1.  Alpha is the transparency.
colors = np.random.sample([n, 4])

# Draw all the circles and return an object ``circles`` that allows
# manipulation of the plotted circles.
circles = plt.scatter(pos[:,0], pos[:,1], marker='o', s=sizes, c=colors)

for i in range(100):
    pos = pos + vel
    bounce = abs(pos) > 10      # Find balls that are outside walls
    vel[bounce] = -vel[bounce]  # Bounce if outside the walls
    circles.set_offsets(pos)    # Change the positions
    plt.pause(0.05)

    
