import numpy as np
import plotly.graph_objects as go


class Shape:
    def __init__(self):
        pass

    def points(self, length):
        '''
        Should return NumPy array of points constituting the shape
        Its shape should be (2, `length`)
        Its values should be between -1 and 1 - everything else will be clamped
        '''
        raise NotImplementedError('Should return NumPy array of points constituting the shape')

    def plot(self, repetition_length=64, num_repetitions=1):
        points = self.render(repetition_length, num_repetitions)
        return go.Figure().update_layout(
            title=f'{type(self).__name__}',
            template='plotly_dark',
            autosize=False,
            width=700,
            height=700,
            xaxis=dict(
                range=(-1, 1)
            ),
            yaxis=dict(
                range=(-1, 1)
            )
        ).add_trace(go.Scatter(
            x=points[0],
            y=points[1]
        ))

    def render(self, repetition_length, num_repetitions=1):
        # call `points` multiple times because the shape could change on each repetition
        points = [self.points(length=repetition_length) for _ in range(num_repetitions)]
        points = np.concatenate(points, axis=-1)
        points = np.clip(points, -1, 1)
        return points