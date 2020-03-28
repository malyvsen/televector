from gpiozero import PWMLED
from time import sleep
from .display import Display


class PWMDisplay(Display):
    def __init__(self, pins, pwm_rate=1e6, point_rate=16000, refresh_rate=60):
        super().__init__(point_rate, refresh_rate)
        self.pins = [PWMLED(pin, initial_value=.5, frequency=pwm_rate) for pin in pins]
    
    def display(self, visible, duration):
        points = self.render(visible, duration)
        points = (points + 1) / 2 # translate to PWM coordinates
        for x, y in zip(points[0], points[1]):
            self.pins[0].value = x
            self.pins[1].value = y
            sleep(1 / self.point_rate)