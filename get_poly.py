import shapely
import bcdp

def get_poly_bnd(*args, **kwargs):
    bnds = bcdp.PolygonBounds(*args, **kwargs)
    bnds.shapes = shapely.geometry.MultiPolygon([bnds.shapes])
    return bnds