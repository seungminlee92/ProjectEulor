def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)

x = 0
 
total = 0
 
while fib(x) < 4000000:
	x+=1
	if fib(x)%2 == 0:
		total+=fib(x)
	else:
		continue
print(total)