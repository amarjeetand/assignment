N=int(input())
p=[]
s=[]

#function to find prime no.

def prime(n):
	for i in range(2,n,1):
		if(n%i==0):
			break
		else:
			p.append(n)
	if(n==2):
		p.append(n)

#find all prime no. less than n

for i in range(2,N,1):
	prime(i)
a=len(p)

#find semi prime no.

for i in range(a):
	for j in range(i+1,a,1):
		x=p[i]*p[j]
		s.append(x)
b=len(s)

#find weather it is written in this for or not

for i in range(b):
	for j in range(b):
		if(s[i]+s[j]==N):
			print("yes")
			quit()
print("no")