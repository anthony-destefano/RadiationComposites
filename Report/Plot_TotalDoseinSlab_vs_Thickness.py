#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
# https://matplotlib.org/gallery/images_contours_and_fields/contourf_log.html#sphx-glr-gallery-images-contours-and-fields-contourf-log-py
from matplotlib import ticker, cm

#filename = sys.argv[1]

filename = 'TotalDoseinSlab_vs_Thickness'

depth, dose = np.loadtxt(filename + '.txt', unpack=True)

fig, ax = plt.subplots()

ax.plot(depth, dose)

ax.set_ylabel('Total Dose (rad)')
ax.set_xlabel('Thickness of carbon composite (mm)')
ax.set_title('Total Dose in Slab vs. Thickness\nUsing Radiation Environment DSNE Table 3.3.1.10.2-1\nComputing Dose in SRIM 2013')
ax.set_xlim((0,20))

#https://riptutorial.com/matplotlib/example/14063/plot-with-gridlines
# Show the major grid lines with dark grey lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-')

plt.savefig(filename + '.eps', dpi=600)

plt.show()