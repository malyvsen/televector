import numpy as np
from ..visible import Visible


class Integrate(Visible):
    def __init__(self, subject):
        super().__init__()
        self.subject = subject
    
    def points(self, length, frame=0):
        to_integrate = self.subject.points(length, frame)
        integrated = np.cumsum(to_integrate, axis=1)
        reshaped = np.moveaxis(integrated, [0, 1], [1, 0])
        mean_centered = reshaped - np.mean(reshaped, axis=0)
        rescaled = mean_centered / np.max(mean_centered, axis=0)
        return np.moveaxis(rescaled, [0, 1], [1, 0])