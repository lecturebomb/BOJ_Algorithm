T=int(input())

for _ in range(T):
    li=list(map(str,input().split()))
    sum=0
    for i in range(len(li)):
        if i ==0:
            sum+=float(li[i])
        else:
            if li[i]=="#":
                sum-=7
            elif li[i]=="%":
                sum+=5
            elif li[i]=="@":
                sum*=3

    print("%0.2f" % sum)