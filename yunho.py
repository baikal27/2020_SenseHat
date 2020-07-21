import numpy as np
import matplotlib.pyplot as plt

d0 = 4.42e3 # Mpc
d0 = 1
v0 = 3e5 # km/s
t = 4.35e17
H = 67.8 # km/(s * Mpc)

dd = 1 * 3.09e19 # km from Mpc
lin_t = np.linspace(0, t, 100)
lin_t2 = np.linspace(0, t, 100)
tim = []
dist = []
tim2 = []
dist2 = []

for i in range(len(lin_t)):
	v = v0 + d0*H
	d = d0*dd + v * lin_t[1]
	v0 = v
	d0 = d / dd
	t = i*lin_t[1]
	print(f't = {t} s')
	print(f'v = {v0} km/s')
	print(f'd = {d0} Mpc')
	print('\n')
	tim.append(t)
	dist.append(v0)
'''
d0 = 4.42e3 # Mpc
v0 = 3e5 # km/s
t = 4.35e17
H = 67.8 # km/(s * Mpc)

dd = 1 * 3.09e19 # km from Mpc

for i in range(len(lin_t2)):
	v = v0 + d0*H
	d = d0*dd + v * lin_t2[1]
	v0 = v
	d0 = d / dd
	t = i*lin_t2[1]
	print(f't = {t} s')
	print(f'v = {v0} km/s')
	print(f'd = {d0} Mpc')
	print('\n')
	tim2.append(t)
	dist2.append(d0)
'''


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(tim, dist, 'ro')
ax.plot(tim2, dist2, 'bo')
plt.show()




