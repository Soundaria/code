n=int(input())
l=list(map(int,input().split()))
a=l
if(n==len(l)):
    max=a[0]
    for i in range(len(a)):
        if(a[i]>max):
            max=a[i]
    a.remove(max)
    for i in range(len(a)):
        if(max in a):
            a.remove(max)
    min=a[0]
    for i in range(len(a)):
        if(a[i]>min):
            min=a[i]
    print(min,end="")
    
