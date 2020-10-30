n=int(input("enter the no. of blocks"))
vw=int(input("speed on walking"))
vc=int(input("speed of cab"))
tw=(2.828*n)//vw
tc=n//vc
if(tc<tw):
	print("min time when man is in cab and equal to ",tc)
else:
	print("min time when man is walking and equal to ",tw)