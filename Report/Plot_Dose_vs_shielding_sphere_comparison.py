#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
# https://matplotlib.org/gallery/images_contours_and_fields/contourf_log.html#sphx-glr-gallery-images-contours-and-fields-contourf-log-py
from matplotlib import ticker, cm

#filename = sys.argv[1]

filename = 'Dose_vs_shielding_sphere_comparison'

thickness, dose = np.loadtxt(filename + '.txt', unpack=True)
thickness2, dose2 = np.loadtxt(filename + '2.txt', unpack=True)

fig, ax = plt.subplots(constrained_layout=True)

ax.loglog(thickness, dose, label='SPENVIS-SHIELDOSE2',marker='o')
ax.loglog(thickness2, dose2, '--', label='SRIM 2013' ,marker='o')

ax.set_xlabel('Al Shielding Thickness (mm)')
ax.set_ylabel('Dose in Sphere (rad)')

plt.legend()

#https://riptutorial.com/matplotlib/example/14063/plot-with-gridlines
# Show the major grid lines with dark grey lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-')

plt.savefig(filename + '.eps', dpi=600)

plt.show()