n=int(input("enter the no. of songs in the playlist"))
l=list(map(int,input("before sorting numbering of songs").split()))
k=int(input("position of computing paradox"))
a=l[k-1]
m=sorted(l)
b=m.index(a)
print("position of computing paradox after sorting is ",b+1)