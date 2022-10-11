N=int(input())
li=list(map(int,input().split()))

sum=0
for i in range (N):
    if li[i]==sum%3:
        sum+=1
print(sum)