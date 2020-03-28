import numpy as np
import plotly.express as px


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

    def plot(self, frame_length=64, start_frame=0, num_frames=1):
        points = self.render(frame_length, start_frame=start_frame, num_frames=num_frames)
        frames = np.linspace(start_frame, start_frame + num_frames, num=points.shape[1], endpoint=False)
        frames = frames.astype(int)
        return px.line(
            x=points[0], y=points[1], animation_frame=frames,
            range_x=[-1, 1], range_y=[-1, 1],
            width=700, height=750,
            template='plotly_dark'
        )


    def render(self, frame_length, start_frame=0, num_frames=1):
        frame_range = range(start_frame, start_frame + num_frames)
        points = [self.points(length=frame_length, frame=frame) for frame in frame_range]
        points = np.concatenate(points, axis=-1)
        points = np.clip(points, -1, 1)
        return points