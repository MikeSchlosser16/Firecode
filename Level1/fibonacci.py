def fib(n):
    if n == 1:
        return 1
    elif n == 0:
    	return 0
    else:
        return fib(n - 1) + fib(n - 2)

##########################################

def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2)


'''
Simple recursion problem. Notice the much cleaner 
comparasion so that we don't need two in provided solution.
'''