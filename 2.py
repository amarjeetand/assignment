r=[]
c=[]
n=int(input("enter the no. of row"))
m=int(input("enter the no. column"))
for i in range(n):
	for j in range(m):
		x=int(input("enter the elements of matrix"))
		c.append(x)
	r.append(c)

#check weather it is binary matrix or not

for i in range(n):
	for j in range(m):
		if(r[i][j]!=0 and r[i][j]!=1):
			print("it is not a binary matrix")
			quit()
print("yes")