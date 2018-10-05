import random

with open("trashdata.txt") as f:
	content = f.readlines()
pairs = [x.split() for x in content]
eta = 0.0001611
#eta = 0.00016


seed = 1000

random.seed(seed)
w1 = random.randint(0,100)
w0 = random.randint(0,100)

for i in range(5000):
	for pair in range(len(pairs)):
		my_x = float(pairs[pair][0])
		my_y = float(pairs[pair][1])
		y_cap = w0+w1*my_x
		delta = my_y - y_cap
		w0 = w0 + eta * delta
		w1 = w1 + eta * delta * my_x


with open("moretrashdata.txt") as f:
	content = f.readlines()
pairs2 = [x.split() for x in content]

sumOfSqr = 0 

for pair in range(len(pairs2)):
	my_x = float(pairs2[pair][0])
	my_y = float(pairs2[pair][1])
	sumOfSqr += (my_y-(w0+w1*my_x))**2


print("CS-5001: HW#1\nProgrammer: Ari Sherman")
print ("\nTRAINING\nUsing random seed =",seed)
print("Using learning rate eta =",eta)
print("After 5000 iterations:\nWeights:")
print("w0 = ",w0, "\nw1 =" ,w1) 
print("\nVALIDATION\nSum-of-Squares Error =",sumOfSqr)
