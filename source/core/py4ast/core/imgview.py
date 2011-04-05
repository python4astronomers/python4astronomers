import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from mpl_toolkits.axes_grid1 import make_axes_locatable

class ImgView(object):
    def __init__(self, img, fig_id=None, imin=None, imax=None):
        self.fig = plt.figure(fig_id)
        self.ax = self.fig.add_axes([0.1, 0.25, 0.8, 0.7])
        self.fig.subplots_adjust(bottom=0.25)

        axcolor = 'lightgoldenrodyellow'
        self.axlo = self.fig.add_axes([0.15, 0.1, 0.65, 0.03], axisbg=axcolor)
        self.axhi = self.fig.add_axes([0.15, 0.15, 0.65, 0.03], axisbg=axcolor)
        self.axrefr = self.fig.add_axes([0.15, 0.05, 0.10, 0.03], axisbg=axcolor)

        imsort = np.sort(img.flatten())
        n = len(imsort)
        if imin is None:
            imin = imsort[int(n * 0.005)]
        if imax is None:
            imax = imsort[int(n * 0.995)]
        self.slo = Slider(self.axlo, 'Scale min', imin, imax, valinit=imsort[int(n * 0.02)])
        self.shi = Slider(self.axhi, 'Scale max', imin, imax, valinit=imsort[int(n * 0.98)])
        self.brefr = Button(self.axrefr, 'Refresh')
        self.slo.on_changed(self.update_slider)
        self.shi.on_changed(self.update_slider)
        self.brefr.on_clicked(self.refresh)
        self.set_img(img)

    def update_slider(self, val):
        if self.shi.val <= self.slo.val:
            self.shi.set_val(self.slo.val + 1)
        self.imgplt.set_clim(self.slo.val, self.shi.val)
        self.fig.canvas.draw()

    def set_img(self, img=None):
        if img is not None:
            self.img = img
        self.ax.set_xlim(0, self.img.shape[1]-1)
        self.ax.set_ylim(0, self.img.shape[0]-1)
        self.imgplt = self.ax.imshow(self.img, vmin=self.slo.val, vmax=self.shi.val,
                                     cmap='hot', origin='lower',
                                     interpolation='nearest')
        self.imgplt.set_cmap('hot')
        divider = make_axes_locatable(self.ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        self.fig.colorbar(self.imgplt, cax=cax)
        self.fig.canvas.draw()

    def refresh(self, event=None):
        self.set_img()
        
