from random import randint

hex = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
contain = []

for x in range(0, 5000):
	a = "\""

	for y in range(0, 8):
		b = randint(0, len(hex)-1)
		a += hex[b]

	a += "\", "
	contain.append(a)

for x in range(0, len(contain)-1):
	print contain[x],