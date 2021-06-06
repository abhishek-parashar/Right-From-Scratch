t=int(input())
while(t>0):
    a=list(map(int,input().split(' ')))
    xa=a[0]
    xb=a[1]
    Xa=a[2]
    Xb=a[3]
    total=int((Xa/xa)+(Xb/xb))
    print(total,"\n")
    t=t-1
