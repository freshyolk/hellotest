
def fizz_buzz(n):
	print(n)
	n=int(n)
	type(int(n))
	if n % 3 == 0 and  n % 5 == 0:
        	return "fizz buzz!"
	elif n % 5 == 0:
        	return "buzz!"
	elif n % 3 == 0: 
		return "fizz!"

result = fizz_buzz(25)
print(result)
