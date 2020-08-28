
# Abhishek Parashar

# counting zeroes in an array

t= int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in a:
        if(i==0):
            count=count+1
    print(count)
    t=t-1