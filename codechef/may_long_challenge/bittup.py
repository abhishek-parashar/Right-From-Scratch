t= int(input())
while(t>0):
    l=list(map(int,input().split(' ')))
    a=l[0]
    b=l[1]
    c=pow(2,a,1000000007)-1
    print(pow(c,b,1000000007))
    t=t-1