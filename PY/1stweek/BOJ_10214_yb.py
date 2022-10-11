t=int(input())
y,k=0,0
for i in range(t):
    for i in range(9):
        a,b=map(int,input().split())
        if a>b:
            y+=1
        elif b<a:
            k+=1
    if y>k:
        print("Yonsei")
    elif k>y:
        print("korea")
    else:
        print("Draw")
