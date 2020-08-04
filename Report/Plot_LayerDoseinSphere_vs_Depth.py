#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
# https://matplotlib.org/gallery/images_contours_and_fields/contourf_log.html#sphx-glr-gallery-images-contours-and-fields-contourf-log-py
from matplotlib import ticker, cm

#filename = sys.argv[1]

filename = 'LayerDoseinSphere_vs_Depth'

depth, dose = np.loadtxt(filename + '.txt', unpack=True)

fig, ax = plt.subplots()

y_pos = np.arange(np.size(depth))

#ax.semilogy(depth, dose)
ax.bar(y_pos, dose, width=1.0)
plt.xticks(y_pos, depth)
ax.set_yscale('log')

ax.set_ylabel('Dose per 0.2 mm (rad)')
ax.set_xlabel('Depth in carbon composite (mm)')
ax.set_title('Layer Dose in Sphere vs. Depth\nUsing Radiation Environment DSNE Table 3.3.1.10.2-1\nComputing Dose in SRIM 2013')

# #https://riptutorial.com/matplotlib/example/14063/plot-with-gridlines
# Show the major grid lines with dark grey lines
ax.grid(b=True, which='major', color='#666666', linestyle='-')

# # Show the minor grid lines with very faint and almost transparent grey lines
# ax.minorticks_on()
# ax.grid(b=True, which='minor', color='#999999', linestyle='-')
# ax.xaxis.set_tick_params(which='minor', bottom=False)

plt.savefig(filename + '.eps', dpi=600)

plt.show()