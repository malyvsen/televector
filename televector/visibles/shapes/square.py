import numpy as np
from ..visible import Visible


class Square(Visible):
    def __init__(self, roundness=.1):
        super().__init__()
        self.roundness = roundness
    
    def points(self, length, frame=0):
        span = np.linspace(0, 2 * np.pi, length)
        cos = np.cos(span)
        x = np.sign(cos) * np.abs(cos) ** self.roundness
        sin = np.sin(span)
        y = np.sign(sin) * np.abs(sin) ** self.roundness
        return np.stack([x, y])