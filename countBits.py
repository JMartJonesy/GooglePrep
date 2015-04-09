def countBits(n):
	if n <= 0:
		return 0
	else:
		if n % 2 == 0:
			return 0 + countBits(n//2)
		else:
			return 1 + countBits(n//2)

print(countBits(3))
