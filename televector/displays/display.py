import numpy as np


class Display:
    def __init__(self, point_rate, refresh_rate):
        self.point_rate = point_rate
        self.refresh_rate = refresh_rate

    def display(self, visible):
        raise NotImplementedError('Should display the visible')

    def render(self, visible, duration):
        num_frames = int(np.ceil(duration * self.refresh_rate))
        frame_length = int(np.ceil(self.point_rate / self.refresh_rate))
        points = visible.render(frame_length=frame_length, num_frames=num_frames)
        return points
