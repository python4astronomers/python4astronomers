import asciitable

dat = asciitable.read('fermi_agn.dat')

redshift = dat['redshift']
flux = dat['photon_flux']
gamma = dat['spectral_index']

# Select rows that have a measured redshift
with_z = redshift != -999

figure(1)
semilogx(flux, gamma, '.b', label='All')
semilogx(flux[with_z], gamma[with_z], 'or', label='With Z')
legend(numpoints=1)
grid()
xlabel('Flux (photon/cm$^2$/s)')
ylabel('Spectral index $\Gamma$')

# Select low- and high-z samples
lowz = with_z & (redshift < 0.8)
highz = with_z & (redshift >= 0.8)

figure(2)
bins = arange(1.2, 3.0, 0.1)
hist(gamma[lowz], bins, color='b', alpha=0.5, label='z < 0.8')
hist(gamma[highz], bins, color='r', alpha=0.5, label='z > 0.8')
xlabel('Spectral index $\Gamma$')
title('$\Gamma$ for low-z and high-z samples')
legend(loc='upper left')

asciitable.write(dat[with_z], 'fermi_agn_with_z.dat')
