#https://coderedirect.com/questions/110806/custom-matplotlib-plot-chess-board-like-table-with-colored-cells
import matplotlib.pyplot as plt
import numpy as np
import pandas

from matplotlib.table import Table

def checkerboard_table(data, fmt='{:}'):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    tb = Table(ax, bbox=[0,0,1,1])

    nrows, ncols = data.shape
    width, height = 1.0 / ncols, 1.0 / nrows

    # Add cells
    for (i,j), val in np.ndenumerate(data):
        # Index either the first or second item of bkg_colors based on
        # a checker board pattern
        idx = [j % 2, (j + 1) % 2][i % 2]

        tb.add_cell(i, j, width, height, text=fmt.format(val), 
                    loc='center')

    ax.add_table(tb)
    return fig