from time import time

t_1 = time()
print t_1

while time() - t_1 < 1.0:
	i = 0
print time()