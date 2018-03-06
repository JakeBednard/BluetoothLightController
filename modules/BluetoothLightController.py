from random import randint
from time import sleep
from .BluetoothLight import BluetoothLight

class BluetoothLightController(object):

    def __init__(self, addresses):
        self.BluetoothLights = [BluetoothLight(address) for address in addresses]
        self.duration = 4
        self.fps = 30
        self.frames = self.duration * self.fps
        self.red = randint(0, 255)
        self.green = randint(0, 255)
        self.blue = randint(0, 255)

    def set_color(self, red, green, blue):
        for light in self.BluetoothLights:
            light.set_color(red, green, blue)

    def transition_to_color(self, next_red, next_green, next_blue):

        dx_red = (next_red - self.red) / self.frames
        dx_green = (next_green - self.green) / self.frames
        dx_blue = (next_blue - self.blue) / self.frames

        for i in range(self.frames):
            self.red += dx_red
            self.green += dx_green
            self.blue += dx_blue
            self.set_color(self.red, self.green, self.blue)
            sleep(1.0 / self.fps)

    def turn_on(self):
        self.transition_to_color(255, 255, 255)

    def turn_off(self):
        self.transition_to_color(0, 0, 0)

    def orb(self):
        next_red = randint(0, 255)
        next_green = randint(0, 255)
        next_blue = randint(0, 255)
        self.transition_to_color(next_red, next_green, next_blue)

    def orb_night(self):
        next_red = randint(0, 50)
        next_green = randint(0, 10)
        next_blue = randint(0, 10)
        self.transition_to_color(next_red, next_green, next_blue)

