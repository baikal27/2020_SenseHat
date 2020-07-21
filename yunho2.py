import numpy as np
import matplotlib.pyplot as plt

d0 = 4.42e3 # Mpc
v0 = 3e5 # km/s
v0 = 0
t0 = 4.35e17
H = 67.8 # km/(s * Mpc)

dd = 1 * 3.09e19 # km from Mpc
tim = []
dist = []
tsum = 0

while tsum < t0:
	v = v0 + d0*H
	t = 1*dd / v
	d = d0 + 1
	v0 = v
	d0 = d
	tsum += t
	tim.append(tsum)
	print(f't = {tsum} s')
#	print(f'v = {v0} km/s')
#	print(f'd = {d0} Mpc')
	print('\n')

'''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(tim, dist, 'ro')
plt.show()
'''



