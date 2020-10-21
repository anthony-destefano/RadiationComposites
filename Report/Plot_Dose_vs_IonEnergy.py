#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
# https://matplotlib.org/gallery/images_contours_and_fields/contourf_log.html#sphx-glr-gallery-images-contours-and-fields-contourf-log-py
from matplotlib import ticker, cm

#filename = sys.argv[1]

filename = 'Dose_vs_IonEnergy'

depth, dose = np.loadtxt(filename + '.txt', unpack=True)

fig, ax = plt.subplots()

#y_pos = np.arange(np.size(depth))

#ax.semilogy(depth, dose)
#ax.bar(depth, dose, width=1.0)
#plt.xticks(y_pos, depth)
ax.loglog(depth, dose, marker='o')
# ax.set_yscale('log')
# ax.set_xscale('log')

ax.set_ylabel('Dose per 0.1 MeV (rad)')
ax.set_xlabel('Proton Energy (MeV)')
ax.set_title('Dose per 0.1 MeV vs. Proton Energy\nUsing Radiation Environment DSNE Table 3.3.1.10.2-1\nComputing Dose in SRIM 2013')

#https://riptutorial.com/matplotlib/example/14063/plot-with-gridlines
# Show the major grid lines with dark grey lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-')

plt.savefig(filename + '.eps', dpi=600)

plt.show()