import numpy as np
from ..visible import Visible
from televector.utils import call_maybe


class Rotate(Visible):
    def __init__(self, subject, radians=0):
        super().__init__()
        self.subject = subject
        self.radians = radians
    
    def points(self, length, frame=0):
        to_rotate = self.subject.points(length, frame)
        radians = call_maybe(self.radians, frame)
        return [
            to_rotate[0] * np.cos(radians) + to_rotate[1] * -np.sin(radians),
            to_rotate[0] * np.sin(radians) + to_rotate[1] * np.cos(radians)
        ]