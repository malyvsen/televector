import numpy as np
from ..visible import Visible


class Compose(Visible):
    def __init__(self, *subjects):
        super().__init__()
        self.subjects = subjects
    
    def points(self, length, frame=0):
        cumulative_lengths = np.linspace(0, length, len(self.subjects) + 1, endpoint=True).astype(int)
        lengths = cumulative_lengths[1:] - cumulative_lengths[:-1]
        to_compose = [subject.points(length, frame) for subject, length in zip(self.subjects, lengths)]
        return np.concatenate(to_compose, axis=1)