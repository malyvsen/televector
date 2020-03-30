import numpy as np
import plotly.express as px
from .display import Display


class PlotDisplay(Display):
    def __init__(self, resolution=64):
        super().__init__()
        self.resolution = resolution

    def display(self, visible, start_frame=0, num_frames=1):
        points = visible.render(self.resolution, start_frame=start_frame, num_frames=num_frames)
        frames = np.linspace(start_frame, start_frame + num_frames, num=points.shape[1], endpoint=False)
        frames = frames.astype(int)
        return px.line(
            x=points[0], y=points[1], animation_frame=frames,
            range_x=[-1, 1], range_y=[-1, 1],
            width=700, height=750,
            template='plotly_dark'
        )
