import random

P = input("Do You Want To Generate a Random Number? \n")

if P == "Yes" or "yes":
	MinRange = int(input("Whats The Minimum Number? \n"))
	MaxRange = int(input("Whats the Maximum Number? \n"))
	Number = (random.randint(MinRange, MaxRange))
	print("Your Number is:", Number)
	
else:
	exit()
	