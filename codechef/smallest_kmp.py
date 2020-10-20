for _ in range(int(input())):
 a=list(input())
 b=input()
 for i in b:
  a.remove(i)
 a.sort()
 m=0
 n=0
 for i in a:
    if i>=b[0]:
        break
    n=n+1
 for i in a:
    if i>b[0]:
        break
    m=m+1 
 s=''.join(a[:n])+b+''.join(a[n:])
 t=''.join(a[:m])+b+''.join(a[m:])
 print(min(s,t))