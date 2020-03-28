from ..visible import Visible
from televector.utils import call_maybe


class Shift(Visible):
    def __init__(self, subject, shift=[0, 0]):
        super().__init__()
        self.subject = subject
        self.shift = shift
    
    def points(self, length, frame=0):
        to_shift = self.subject.points(length, frame)
        shift = [call_maybe(s, frame) for s in self.shift]
        return [t + s for t, s in zip(to_shift, shift)]