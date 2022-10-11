import sys
from collections import Counter
n=int(sys.stdin.readline())
arr=[]
sum=0
for i in range(n):
    arr.append(int(sys.stdin.readline()))#리스트에 삽입
for j in arr:
    sum+=j
print(round(sum/n))#산술 평균

arr.sort()
print(arr[n//2])# 중앙값

# most frequent_value
mf=Counter(arr).most_common()
if len(mf)>1:
    if mf[0][1]==mf[1][1]:
        print(mf[1][0])
    else:
        print(mf[0][0])
else:
    print(mf[0][0])
print(max(arr)-min(arr))# 범위










