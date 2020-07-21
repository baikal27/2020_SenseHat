from sense_hat import SenseHat
import time
from random import choice

sense = SenseHat()

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)
#colour_lst = [red, green, blue, yellow, magenta, cyan, white, black]

sense.set_pixel(0, 5, r)
time.sleep(2)
creeper_pixels = [
    r, g, g, g, g, g, g, g,
    g, r, g, g, g, g, g, g,
    g, b, r, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, r, g, g,
    g, g, b, b, b, b, r, g,
    g, g, b, g, g, b, g, r
]

sense.set_pixels(creeper_pixels)
time.sleep(2)
sense.set_rotation(90)
time.sleep(2)
sense.set_rotation(180)
time.sleep(2)
sense.set_rotation(270)
time.sleep(2)
sense.set_rotation(0)
time.sleep(2)
sense.flip_h()
time.sleep(2)
sense.flip_v()
time.sleep(2)
sense.clear()
