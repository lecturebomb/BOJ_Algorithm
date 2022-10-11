N=int(input())
li=list(map(int,str(N)))
li.sort(reverse=True)

for i in li:
    print(i,end='')
