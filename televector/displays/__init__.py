from .plot_display import PlotDisplay
from .audio_display import AudioDisplay
try:
    from .pwm_display import PWMDisplay
except ImportError:
    pass # RasPi dependencies are not installed, that's okay

from .display import Display
from .realtime_display import RealtimeDisplay