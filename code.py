def sg(n):
    if n>=0:
        return 1
    else:
        return -1
for _ in range(int(input())):
    n = input()
    lis = list(map(int,input().split(" ")))
    l = []
    s = lis[0]
    for i in range(1,len(lis)):
        if sg(lis[i]) == sg(lis[i-1]):
            s =s+ lis[i]
        else:
            l.append(s)
            s = lis[i]
    if(s!=0):
        l.append(s)
    d = []
    for i in range(len(l)):
        if l[i]<0:
            d.append([l[i],i])
    print(l)    
    print(d)
    d.sort()
    lf = 0
    ri = len(d)-1
    while(lf < ri):
        
            
        