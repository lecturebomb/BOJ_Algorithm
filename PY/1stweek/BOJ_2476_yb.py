N=int(input())
d=[]

for i in range (N):
    a,b,c=map(int,input().split())

    if a==b==c:
       d.append(10000+a*1000)
    elif a==b or a==c :
       d.append(1000+a*100)
    elif b==c:
        d.append(1000+b*100)
    else:
        d.append(max(a,b,c)*100)

print(max(d))
