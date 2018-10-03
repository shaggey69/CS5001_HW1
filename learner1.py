with open("trashdata.txt") as f:
	content = f.readlines()
pairs = [x.split() for x in content]
eta = 0.000001
w1 = 0.4
w0 = 0.3

for i in range(5000):
	for pair in pairs:
		my_x = pairs[int(pair[0])]
		my_y = pairs[int(pair[1])]
		y_cap = w0+w1*my_y
		delta = my_y - y_cap
		w0 = w0 + eta * delta * my_x
		w1 = w1 + eta * delta * my_x


print(w0+w1) 