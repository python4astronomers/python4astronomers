figure(2)
clf()
axis([-10, 10, -10, 10])

# Define properties of the "bouncing balls"
n = 14
pos = (20 * random_sample(n*2) - 10).reshape(n, 2)
vel = (0.3 * normal(size=n*2)).reshape(n, 2)
sizes = 100 * random_sample(n)+10  

# Colors where each row is (Red, Green, Blue, Alpha).  Each can go
# from 0 to 1.  Alpha is the transparency.
colors = random_sample([n, 5])

# Draw all the circles and return an object ``circles`` that allows
# manipulation of the plotted circles.
circles = scatter(pos[:,0], pos[:,1],marker='o',c=colors,s=sizes)

for i in range(200):
    if 80>i>60:
        sizes=sizes-(random_sample(n)*3)
    if i<60 | i >80:
        sizes=sizes+(random_sample(n)*3)+0.1
  
   
    #circles = scatter(pos[:,0], pos[:,1], marker='o', s=sizes, c=colors)
    pos = pos + vel
    bounce = abs(pos) > 10 # Find balls that are outside walls
    vel[bounce] = -1.2*vel[bounce]  # Bounce if outside the walls
    circles.set_edgecolor(colors)
    circles.set_facecolor('none')
    circles.set_offsets(pos)    # Change the positions
    circles.set_lw(sizes)
   
    draw()
