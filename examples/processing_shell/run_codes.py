import os
import asciitable

smoothing = 30  # Smoothing window length
freqs = [2, 4]  # Frequency values for making data
noises = [1, 5] # Noise amplitude inputs

figure(1)
clf()

# Loop over freq and noise values, running standalone code to create noisy data
# and smooth it.  Get the data back into Python and plot.

plot_num = 1
for freq in freqs:
    for noise in noises:
        # Run the compiled code "make_data" to make data as a list of x, y, y_smooth
        cmd = 'make_data %s %s %s' % (freq, noise, smoothing)
        print 'Running', cmd
        out = os.popen(cmd).read()
        # out now contains the output from <cmd> as a single string

        # Parse the output string as a table
        dat = asciitable.read(out)

        # Make a plot
        subplot(2, 2, plot_num)
        plot(dat['x'], dat['y'])
        plot(dat['x'], dat['y_smooth'], linewidth=3, color='r')

        plot_num += 1
