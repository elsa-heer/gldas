import numpy as np

from pygeogrids.grids import BasicGrid


def GLDAS025Cellgrid():
    """
    Class for the GLDAS-Noah Version1 0.25deg cell grid.
    """

    resolution = 0.25

    lon, lat = np.meshgrid(
        np.arange(-180 + resolution/2, 180 + resolution/2, resolution),
        np.arange(-90 + resolution/2, 90 + resolution/2, resolution))

    return BasicGrid(lon.flatten(), lat.flatten()).to_cell_grid(cellsize=5.)
