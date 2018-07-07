import numpy as np
 
def karatsuba(x, y):
	""" This function is an implementation of Karatsuba multiplication 

	Args: 
		x (int): first operand with n digits which is power of 2 
		y (int): second operand with the same digits as x
	Returns:
		result (int): multiplication result 
	"""

	# Convert integers to strings for split operation 
	x_str = str(x)
	y_str = str(y)

	# Base case
	if len(x_str) == 1 and len(y_str) == 1:
		return x*y
	else:

		# make sure integers are of even digits
		num_bit = max(len(x_str), len(y_str))
		if num_bit%2 != 0:
			num_bit += 1

		while len(x_str)!=num_bit:
			x_str = '0'+ x_str
		while len(y_str)!=num_bit:
			y_str = '0' + y_str

		n = len(x_str)	
		mid = int(n/2)
		# Manipulation on x
		a = int(x_str[:mid])
		b = int(x_str[mid:])
		# Manipulation on y
		c = int(y_str[:mid])
		d = int(y_str[mid:])
		p = a+b
		q = c+d

		ac = karatsuba(a, c)
		bd = karatsuba(b, d)
		abcd = karatsuba(p, q) - ac - bd

		return 10**n*ac + 10**int(n/2)*abcd + bd 



if __name__ == '__main__':
	x = 3141592653589793238462643383279502884197169399375105820974944592
	y = 2718281828459045235360287471352662497757247093699959574966967627
	result = karatsuba(x,y)
	print(result, len(str(result)))
