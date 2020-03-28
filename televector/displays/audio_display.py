from IPython.display import Audio
from .display import Display


class AudioDisplay(Display):
    def __init__(self, point_rate=16000, refresh_rate=60):
        super().__init__(point_rate, refresh_rate)
    
    def display(self, visible, duration):
        points = self.render(visible, duration)
        return Audio(points, rate=self.point_rate, normalize=False)
