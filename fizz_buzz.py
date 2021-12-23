
def fizz_buzz(n):
	if n % 3 == 0 and  n % 5 == 0:
        	return "fizz buzz!"
	elif n % 5 == 0:
        	return "buzz!"
	elif n % 3 == 0: 
		return "fizz!"

n_1 = 25
n_2 = 6
n_3 = 15
print("called with {}, result is  {}".format( n_1, fizz_buzz(n_1) ))
print("called with {}, result is  {}".format( n_2, fizz_buzz(n_2) ))
print("called with {}, result is  {}".format( n_3, fizz_buzz(n_3) ))

for n in range(11)[1:]: 
	result = fizz_buzz(n) 
	print (result)
 


