from ..visible import Visible
from televector.utils import call_maybe


class Scale(Visible):
    def __init__(self, subject, scale=[1, 1]):
        super().__init__()
        self.subject = subject
        self.scale = scale
    
    def points(self, length, frame=0):
        to_scale = self.subject.points(length, frame)
        scale = [call_maybe(s, frame) for s in self.scale]
        return [t * s for t, s in zip(to_scale, scale)]