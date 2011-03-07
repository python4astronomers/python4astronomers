import aplpy

# Convert all images to common projection
aplpy.make_rgb_cube(['m1.fits', 'i3.fits', 'i2.fits'], 'rgb.fits')

# Make 3-color image
aplpy.make_rgb_image('rgb.fits', 'rgb.png', vmin_r=20, vmax_r=400,
                     vmin_g=0, vmax_g=150, vmin_b=-2,vmax_b=50)

# Create a new figure
f = aplpy.FITSFigure('rgb_2d.fits')

# Show the RGB image
f.show_rgb('rgb.png')

# Add contours
f.show_contour('sc.fits', cmap='gist_heat', levels=[0.2,0.4,0.6,0.8,1.0])

# Overlay a grid
f.add_grid()
f.grid.set_alpha(0.5)

# Save image
f.save('plot.png')
