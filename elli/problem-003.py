import math

def factors(n):
	ans = [1,n]
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			ans.append(i)
			if n / i != i:
				ans.append(n / i) 
		i += 1
	ans.sort()
	return ans
	
def is_prime(n):
	if len(factors(n)) == 2:
		return True
	else:
		return False

answer = 0
for i in factors(600851475143):
	if is_prime(i):
		answer = i
print answer