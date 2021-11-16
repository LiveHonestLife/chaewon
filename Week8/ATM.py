# 11399번 : https://www.acmicpc.net/problem/11399
# 메모리 29200KB
# 시간 72ms
# 코드길이 191B

import sys
n=int(sys.stdin.readline())
times=list(map(int, sys.stdin.readline().split()))
times.sort()
now=0
total=0
for i in range(0,n):
    now=now+times[i]
    total=now+total
print(total)
