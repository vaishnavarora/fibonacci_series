#Fibonacci  series

a = 0
b = 1
n = int(input("enter the number of values you want the series upto : "))
print(a)
print(b)
for c in range(n):
	c = a + b
	a = b
	b = c
	print(c)

