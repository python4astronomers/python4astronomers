import os
# set path to save images, if not current working directory
impath = ''


import pyfits

hdus = pyfits.open('3c120_stis.fits.gz')
img = hdus[1].data
err = hdus[2].data
dq = hdus[3].data


plt.clf()
plt.imshow(img)

plt.clf()
plt.imshow(img, origin = 'lower')

plt.clf()
plt.imshow(img, origin = 'lower', vmin = -10, vmax = 65)
plt.colorbar()

plt.savefig(os.path.join(impath, 'imgview_img.png'))

plt.clf()
plt.imshow(err, origin = 'lower', vmin = 5, vmax = 25)
plt.colorbar()
plt.savefig(os.path.join(impath, 'imgview_err.png'))

plt.clf()
plt.imshow(dq, origin = 'lower', vmax = 25)
plt.colorbar()
plt.savefig(os.path.join(impath, 'imgview_dq.png'))


spectrum = img.sum(axis=0)
profile = img.sum(axis=1)
figure()
plot(spectrum)
figure()
plot(profile)

import scipy.signal
img_sm = scipy.signal.medfilt(img, 5)
sigma = median(err)
bad = abs(img - img_sm) / sigma > 8.0
img_cr = img.copy()
img_cr[bad] = img_sm[bad]
img_cr[230:280,:] = img[230:280,:]

x = append(arange(10, 200), arange(300, 480))
y = img_cr[x, 10]
clf()
plot(x, y)
pfit = polyfit(x, y, 2)
yfit = polyval(pfit, x)
plot(x, yfit)

xrows = arange(img_cr.shape[0])
bkg = zeros_like(img_cr)
for col in range(img_cr.shape[1]):
    pfit = polyfit(x, img_cr[x, col], 2)
    bkg[:, col] = polyval(pfit, xrows)

img_bkg = img_cr - bkg

plt.clf()
plt.imshow(bkg, origin = 'lower', vmin=0, vmax=20)
plt.colorbar()
plt.savefig(os.path.join(impath,'bkg_fit1.png'))

plt.clf()
plt.imshow(img_bkg, origin = 'lower', vmin=0, vmax=60)
plt.colorbar()
plt.savefig(os.path.join(impath,'bkg_fit2.png'))

spectrum = img_bkg[250:260, :].sum(axis=0)
plt.clf()
plt.plot(spectrum)
plt.savefig(os.path.join(impath,'spectrum_final.png'))
