import sys

arguments = sys.argv[1:]
n = arguments[0]
print(n)
n=int(n)
type(int(n))
if n % 3 == 0 and  n % 5 == 0:
        print ("fizz buzz!")
elif n % 5 == 0:
        print ("buzz!")
elif n % 3 == 0: 
	print("fizz!")

