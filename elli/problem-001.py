counter = 1
total = 0

while (counter < 1000):
	if counter % 3 == 0:
		total += counter
	elif counter % 5 == 0:
		total += counter
	counter+=1
print total


#  print sum([i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0])