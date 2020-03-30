import numpy as np


class Visible:
    def __init__(self):
        pass

    def points(self, length, frame=0):
        '''
        Should return NumPy array of points constituting the visible
        Its shape should be (2, `length`)
        Its values should be between -1 and 1 - everything else will be clamped
        '''
        raise NotImplementedError('Should return NumPy array of points constituting the visible')

    def render(self, frame_length, start_frame=0, num_frames=1):
        frame_range = range(start_frame, start_frame + num_frames)
        points = [self.points(length=frame_length, frame=frame) for frame in frame_range]
        points = np.concatenate(points, axis=-1)
        points = np.clip(points, -1, 1)
        return points