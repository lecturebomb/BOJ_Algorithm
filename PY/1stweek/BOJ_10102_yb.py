v=int(input())
vote=list(input())
A,B=0,0
for i in range (v):
    if vote[i]=='A':
        A+=1
    else:
        B+=1

if A>B:
    print('A')
elif B>A:
    print('B')
else:
    print("Tie")
