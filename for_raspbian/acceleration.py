from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
	acceleration = sense.get_accelerometer_raw()
	x = round(acceleration['x'], 0)
	y = round(acceleration['y'], 0)
	z = round(acceleration['z'], 0)

	print('x = {}, y = {}, z = {}'.format(x, y, z))
