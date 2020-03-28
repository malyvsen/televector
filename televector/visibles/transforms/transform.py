from ..visible import Visible
from .rotate import Rotate
from .scale import Scale
from .shift import Shift
from televector.utils import call_maybe


def Transform(subject, scale_radians=0, scale=[1, 1], radians=0, shift=[0, 0]):
    return Shift(
        Rotate(
            Rotate(
                Scale(
                    Rotate(
                        subject=subject,
                        radians=scale_radians
                    ),
                    scale=scale
                ),
                radians=lambda frame: -call_maybe(scale_radians, frame)
            ),
            radians=radians
        ),
        shift=shift
    )