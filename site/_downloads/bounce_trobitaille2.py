from copy import deepcopy

figure(1)
clf()
axis([-10, 10, -10, 10])

# Define properties of the "bouncing balls"
n = 10
pos_start = (20 * random_sample(n * 2) - 10).reshape(n, 2)
vel_start = (0.1 * normal(size=n * 2)).reshape(n, 2)
sizes_start = 100 * random_sample(n) + 100
colors_start = random_sample([n, 4])
colors_start[:, 3] = 1.0

pos = []
vel = []

circles = []

n_groups = 0

for i in range(300):

    if i in range(0, 20, 3):
        n_groups += 1
        circles.append(scatter(pos_start[:, 0], pos_start[:, 1], \
                               marker='o', s=deepcopy(sizes_start),
                               facecolors=deepcopy(colors_start),
                               edgecolors='none'))
        pos.append(deepcopy(pos_start))
        vel.append(deepcopy(vel_start))
        colors_start[:, 3] *= 0.8
        sizes_start[:] *= 0.9

    for ic in range(n_groups):

        vel[ic][:, 1] += -0.01

        # Update positions
        pos[ic] = pos[ic] + vel[ic]

        # Find balls that are outside walls
        bounce = abs(pos[ic]) > 10

        # Bounce
        vel[ic][bounce] = -vel[ic][bounce]

        # Change the positions
        circles[ic].set_offsets(pos[ic])

    draw()
