t= int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    a=sorted(a)
    for i in range(n+1):
        if i==k:
            print(a[i-1])
    t=t-1
        