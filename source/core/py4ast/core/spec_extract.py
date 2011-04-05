import pyfits

hdus = pyfits.open('3c120_stis.fits.gz')
img = hdus[1].data
err = hdus[2].data
dq = hdus[3].data

from imgview import ImgView
ImgView(img)
ImgView(err)
ImgView(dq)

spectrum = img.sum(axis=0)
profile = img.sum(axis=1)
figure()
plot(spectrum)
figure()
plot(profile)

plot(img[:, 205])
plot(
