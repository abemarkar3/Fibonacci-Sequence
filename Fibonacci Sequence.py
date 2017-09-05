''' Fibonacci Sequence - Enter a number and have the program generate the Fibonacci 
	sequence to that number or to the Nth number.'''


x = 11 # Use this to find fibonacci sequence of a number
def Fibonacci(n):
    if n < 2:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)



print(Fibonacci(x))
