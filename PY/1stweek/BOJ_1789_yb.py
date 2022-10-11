s=int(input())
n=1
sum=0
cnt=0

while 1:
    if(sum<=s):
        sum+=n
        n+=1
        cnt+=1
    else:
        break


print(cnt-1)



