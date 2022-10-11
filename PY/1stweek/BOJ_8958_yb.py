n=int(input())
for i in range(n):
    a=list(input())
    score=0
    sum=0
    for i in a:
        if i=='O':
            score+=1
            sum+=score
        else:
            score=0
    print(sum)