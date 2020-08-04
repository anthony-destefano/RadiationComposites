#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
# https://matplotlib.org/gallery/images_contours_and_fields/contourf_log.html#sphx-glr-gallery-images-contours-and-fields-contourf-log-py
from matplotlib import ticker, cm

#filename = sys.argv[1]

filename = '3.3.1.10.2-1'

energy, Iflux, Dflux = np.loadtxt('DSNE_Table_' + filename + '.txt', unpack=True)

fig, ax = plt.subplots(constrained_layout=True)

ax.loglog(energy, Iflux, label='SPE Proton Integral Fluence')
ax.loglog(energy, Dflux, '--', label='SPE Proton Differential Fluence')

ax.set_xlabel('Proton Energy (MeV)')
ax.set_ylabel(r'SPE Integral Fluence (Protons/cm$^2$)')

secaxy = ax.secondary_yaxis('right')
secaxy.set_ylabel(r'SPE Differential Fluence (Protons/MeV-cm$^2$)')
plt.legend()

#https://riptutorial.com/matplotlib/example/14063/plot-with-gridlines
# Show the major grid lines with dark grey lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-')

plt.savefig('DSNE_Plot_' + filename + '.eps', dpi=600)

plt.show()