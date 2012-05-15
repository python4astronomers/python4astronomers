#from matplotlib.pyplot import *
#from numpy.random import *
#from numpy import *

# K. Rosenfeld 5/11/12:
# This script visualizes a parallelized Metropolis-Hastings algorithm as 
# it samples a 2D Gaussian (or whatever function your heart desires).
# Just chose the number of chains (or "sampling balls"), the average jump size
# and let it run. The (arbitrary) contours that appear after a burn in time 
# (burn = NN) show the resulting samples. 

#Some tuning and patience may be required.

# Define the potential
def mypotential(x,y):
	x0 = 0
	y0 = 0
	potent = 1./(2*pi*sigma**2)*np.exp(-0.5*((x-x0)**2/sigma**2 +
		 (y - y0)**2/sigma**2))
	return potent

#  Set up figure
figure(1)
clf()
set_cmap('gray')
axis([-10, 10, -10, 10])

# Set up the potential
sigma = 3.0
nx = 30
dx = 20./nx
x = np.arange(-10,10,dx)
y = np.arange(-10,10,dx)
ax = np.tile(x,(nx,1))
ay = np.tile(y,(nx,1)).T

# Plot the potential
pot = mypotential(ax,ay);
imshow(pot,extent=(-10,10,-10,10))

# Set up the "sampling balls"
dstep = 0.5	# Size of steps
burn  = 100	# No. of steps before show contours
n     = 15	# No. of balls
ntime = 3000	# Lenght of run

# Define properties of the "sampling balls"
pos   = (20 * random_sample(n*2) - 10).reshape(n, 2)
sx = []
sy = []
sizes = 90 + ones(n)
alt = mypotential(pos[:,0],pos[:,1])

# Colors where each row is (Red, Green, Blue, Alpha).  Each can go
# from 0 to 1.  Alpha is the transparency.
colors = random_sample([n, 4])

# Draw all the circles and return an object ``circles`` that allows
# manipulation of the plotted circles.
circles = scatter(pos[:,0], pos[:,1], marker='o', s=sizes, c=colors)

for i in range(ntime):
	# generate proposed new positions
	prop = pos + dstep*randn(n,2)
	palt = mypotential(prop[:,0],prop[:,1])
	pmove = palt/alt
	mrand = rand(n)
	# figure out which balls make the jump
	move = pmove > mrand 
	pos[move] = prop[move]
	alt[move] = palt[move]

	# save positions
	if (i > burn):
		sx   = concatenate((sx,pos[:,0]),axis=0)
		sy   = concatenate((sy,pos[:,1]),axis=0)
	# update contours
	if (mod(i,10) == 1 and i > burn):
		clf()
		axis([-10, 10, -10, 10])
		imshow(pot,extent=(-10,10,-10,10))
		H,xedges,yedges = histogram2d(sx,sy,bins=nx)
		xcen = (xedges + roll(xedges,1))/2
		ycen = (yedges + roll(yedges,1))/2
		xcen = xcen[1:nx+1]
		ycen = ycen[1:nx+1]
		set_cmap('gray')
		contour(xcen,ycen,H.T,linewidth=2)
		set_cmap('jet')
		circles = scatter(pos[:,0], pos[:,1], marker='o', s=sizes, c=colors)

	circles.set_offsets(pos)    # Change the positions of the balls
	draw()
