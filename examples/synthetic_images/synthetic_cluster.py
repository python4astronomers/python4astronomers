# This example demonstrates how to create a synthetic image of a cluster,
# including convolution with a Gaussian filter and the addition of noise

import pyfits
from numpy import random, cos, sin, pi, zeros
from scipy.ndimage import gaussian_filter

# Create empty image
nx, ny = 512, 512
image = zeros((ny, nx))

# Set number of stars
n = 10000

# Generate random positions
r = random.random(n) * nx
theta = random.uniform(0., 2. * pi, n)

# Generate random fluxes
f = random.random(n) ** 2

# Compute position
x = nx / 2 + r * cos(theta)
y = ny / 2 + r * sin(theta)

# Add stars to image
for i in range(n):
    if x[i] >= 0 and x[i] < nx and y[i] >= 0 and y[i] < ny:
        image[y[i], x[i]] += f[i]

# Convolve with a gaussian
image = gaussian_filter(image, 1)

# Add noise
image += random.normal(3., 0.01, image.shape)

# Write out to FITS image
pyfits.writeto('cluster.fits', image, clobber=True)
