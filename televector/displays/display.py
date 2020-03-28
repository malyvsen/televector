import numpy as np


class Display:
    def __init__(self, point_rate, refresh_rate):
        self.point_rate = point_rate
        self.refresh_rate = refresh_rate

    def display(self, visible):
        raise NotImplementedError('Should display the visible')

    def render(self, visible, duration):
        refresh_count = int(np.ceil(duration * self.refresh_rate))
        points_per_refresh = int(np.ceil(self.point_rate / self.refresh_rate))
        points = visible.render(points_per_refresh, refresh_count)
        return points