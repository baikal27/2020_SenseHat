from sense_hat import SenseHat
import time
from random import choice

sense = SenseHat()

r = 255 
g = 255
b = 255

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)
colour_lst = [red, green, blue, yellow, magenta, cyan, white, black]

sense.clear(white)
time.sleep(0.5)
sense.show_message("Jung Sin Woo gogogon!", text_colour=cyan, back_colour=black, scroll_speed=0.1)

color = choice(colour_lst)
sense.show_letter('Y', color)
time.sleep(1.)
color = choice(colour_lst)
sense.show_letter('N', color)
time.sleep(1.)
color = choice(colour_lst)
sense.show_letter('W', color)
time.sleep(1.)
color = choice(colour_lst)
sense.show_letter('A', color)
time.sleep(1.)
sense.show_message("YNWA", text_colour=red, back_colour=black)
sense.clear()
