from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

while True:
	orien = sense.get_orientation()
	pitch = round(orien['pitch'],3)
	roll = round(orien['roll'], 3)
	yaw = round(orien['yaw'], 3)
	print('pitch: {} roll: {} yaw {}'.format(pitch, roll, yaw))
	time.sleep(0.05)
