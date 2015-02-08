from matplotlib import image

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.get_frame().set_alpha(1.0)
axis([-10, 10, -10, 10])

# Download a dolphin image
import urllib
url = 'http://www.webweaver.nu/clipart/img/nature/ocean/dolphin.gif'
urllib.urlretrieve(url, 'dolphin.gif')

im = image.imread('dolphin.gif')

# Define properties of the "bouncing balls"
n = 1
pos = ((20 * random_sample(n*2) - 10)*0.7).reshape(n, 2)
vel = (0.3 * normal(size=n*2)).reshape(n, 2)
#sizes = 100 * random_sample(n) + 100

# Colors where each row is (Red, Green, Blue, Alpha).  Each can go
# from 0 to 1.  Alpha is the transparency.
# colors = random_sample([n, 4])

# Draw all the circles and return an object ``circles`` that allows
# manipulation of the plotted circles.
# ax.circles = scatter(pos[:,0], pos[:,1], s=sizes, marker='*', c=colors)

# Several kinds of forces
elastic = 1.0
gravity = 0.03
ffloat = 0.06

#ax.figdol = figimage(im,100,100,origin="lower")
#angle = 60
#dolphin2=dolphin.set_transform(matplotlib.transforms.Affine2D().rotate_deg(angle))

# Plot the 'aquarium'.
ax.text(-1, 9, 'a poorly designed aquarium', fontsize=15,bbox={'facecolor':'yellow','alpha':0.5,'pad':10})
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
x = np.linspace(-10, 10, 500)
ax.fill_between(x,-10,0,color='b', alpha=0.3)

for i in range(200):
	bounce = abs(pos) > 8      # Find balls that are outside walls
	vel[bounce] = -elastic * vel[bounce]  # Bounce if outside the walls
	floating = pos[:,1] < 0
	vel[floating,1] += ffloat  # Floating force
	vel[:,1] -= gravity        # Gravity force
#	vel[floating,:] += random_sample(2) / 10.0
	pos = pos + vel
        # Replace markers with dolphin, however I don't know how to draw more than one dolphin.
	line, = ax.plot(pos[:,0]-1.4,pos[:,1]-1.0,"bo",mfc="None",mec="None",markersize=5)
	line._transform_path()
	path, affine = line._transformed_path.get_transformed_points_and_affine()
	path = affine.transform_path(path)
	for pixelPoint in path.vertices:
		dol = fig.figimage(im,pixelPoint[0]-10,pixelPoint[1]-10,origin="lower", zorder=1)
	draw()
	dol.set_zorder(0)

# Reference:
# http://stackoverflow.com/questions/2318288/how-to-use-custom-marker-with-plot
