from scipy.spatial import Delaunay
from scipy.interpolate import LinearNDInterpolator

class PixelInterpolator:
    def __init__(self, pts_in, pts_out):
        self.tri = Delaunay(pts_in)
        self.pts_out = pts_out
    
    def __call__(self, vals):
        interp = LinearNDInterpolator(self.tri, vals)
        return interp(self.pts_out)