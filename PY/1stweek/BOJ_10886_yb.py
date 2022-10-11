N=int(input())
agree,disagree=0,0

for i in range (N):
    b=int(input())
    if b==1:
        agree+=1
    elif b==0:
        disagree+=1


if agree>disagree:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

