import numpy as np
from .shape import Shape


class Circle(Shape):
    def __init__(self, center=[0, 0], radius=1):
        super().__init__()
        self.center = center
        self.radius = radius
    
    def points(self, length):
        span = np.linspace(0, 2 * np.pi, length)
        x = np.cos(span) * self.radius + self.center[0]
        y = np.sin(span) * self.radius + self.center[1]
        return np.stack([x, y])