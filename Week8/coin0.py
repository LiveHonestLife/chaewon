# 동전 0 : https://www.acmicpc.net/problem/11047
# memory : 29200KB
# 시간 : 72ms
# 코드길이 344B

import sys
n,k=map(int, sys.stdin.readline().split())

coin=[list(map(int, sys.stdin.readline().split())) for i in range(0,n) ]
coins = sum(coin, [])
cnt=0
while k!=0:
    if k >= coins[len(coins)-1]:
        c=k//coins[len(coins)-1]
        cnt+=c
        k=k-coins[len(coins)-1]*c
        coins.pop()
    else:
        coins.pop()

print(cnt)
