T=int(input())


for i in range (T):
    A, B = map(int,input().split())
    A1,B1=A,B
    while A!=0: #0이 될때 까지 반복
        B=B%A #B는 나머지
        A,B=B,A #교환
    gcd=B
    lcm=A1*B1//B
    print(lcm)

