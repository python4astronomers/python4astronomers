# The documentation for curve_fit is here:
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

import numpy as np
from scipy.optimize import curve_fit

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


# Create function
def gaussian(x, a, b, c):
    return a * np.exp(-(x - b) ** 2 / c ** 2)

# Generate fake data
n = 100
x = np.random.uniform(-10., 10., n)
y = np.exp(-(x - 3.) ** 2 / 2. ** 2) * 10. + np.random.normal(0., 2., n)
e = np.random.uniform(0.1, 1., n)

# Fit
popt, pcov = curve_fit(gaussian, x, y, sigma=e)

# Print results
print "Scale =  %.3f +/- %.3f" % (popt[0], np.sqrt(pcov[0, 0]))
print "Offset = %.3f +/- %.3f" % (popt[1], np.sqrt(pcov[1, 1]))
print "Sigma =  %.3f +/- %.3f" % (popt[2], np.sqrt(pcov[2, 2]))

# Create new figure
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Plot data
ax.errorbar(x, y, yerr=e, lw=1, color='black', fmt=None)

# Plot model
xm = np.linspace(-10., 10., 100)
ax.plot(xm, gaussian(xm, *popt))

# Save figure
fig.savefig('fit.png')
