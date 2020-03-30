import numpy as np
from .display import Display


class RealtimeDisplay(Display):
    def __init__(self, point_rate, refresh_rate):
        super().__init__()
        self.point_rate = point_rate
        self.refresh_rate = refresh_rate

    def render(self, visible, duration):
        num_frames = int(np.ceil(duration * self.refresh_rate))
        frame_length = int(np.ceil(self.point_rate / self.refresh_rate))
        points = visible.render(frame_length=frame_length, num_frames=num_frames)
        return points
