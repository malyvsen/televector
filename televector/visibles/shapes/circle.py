import numpy as np
from ..visible import Visible


class Circle(Visible):
    def __init__(self):
        super().__init__()
    
    def points(self, length, frame=0):
        span = np.linspace(0, 2 * np.pi, length)
        x = np.cos(span)
        y = np.sin(span)
        return np.stack([x, y])