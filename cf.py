def check(m,b):
    flag=1
    l=list(map(int,input().split()))
    
    for j in range(1,m,1):
        if(abs(l[j]-l[j-1])>=b):
            flag+=1
    return(flag)
        
t=int(input())
for i in range(t):
    n,b,m=map(int,input().split())
    print(check(m,b))