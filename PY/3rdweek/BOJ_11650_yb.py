import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

for i in sorted(li):
    print(i[0], i[1])