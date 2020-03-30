from IPython.display import Audio
from .realtime_display import RealtimeDisplay


class AudioDisplay(RealtimeDisplay):
    def __init__(self, point_rate=16000, refresh_rate=60):
        super().__init__(point_rate, refresh_rate)
    
    def display(self, visible, duration):
        points = self.render(visible, duration)
        return Audio(points, rate=self.point_rate, normalize=False)
