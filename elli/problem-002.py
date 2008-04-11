first = 1
second = 2
total = 0
swap = 0
while (second < 4000000):
	if second % 2 == 0:
		total += second
	swap = first
	first = second
	second = swap + first
print total