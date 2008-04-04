from useful_euler import factorial
side_length = 20
print "Side Length %s has %s paths." % (side_length, factorial(side_length * 2) / (factorial(side_length) ** 2))