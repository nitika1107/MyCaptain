a=0
b=1
c=0
n=int(input("Enter a number:"))
print(n,"fibonacci numbers are given below:")
for i in range (1,n):
	print(a,end=' ')
	c=a+b
	a=b
	b=c
print()
print('{:^25}'.format('end'))
