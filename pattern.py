n=int(input("Enter a number: "))

x=" "

y="*"
for i in range(0,n):
	print((x*n)+(y*(1+i*2)))
	n-=1
