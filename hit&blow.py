import random

kotae = []
while len(kotae) != 3:
	x = random.randint(1,9)
	if x not in kotae:
		kotae.append(x)

print(kotae)