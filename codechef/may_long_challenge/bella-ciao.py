t = int(input())
while(t>0):
    a=list(map(int,input().split(' ')))
    D=a[0]
    d=a[1]
    p=a[2]
    q=a[3]
    remainder=D%d
    n=D//d
    value=(n*p*d) + (d*q*(n*(n-1)//2))+(p*remainder+(remainder*q*n))
    print(value,"\n")
    t=t-1
    