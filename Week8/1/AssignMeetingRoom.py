#시간초과
# 1931번 회의실 배정 : https://www.acmicpc.net/problem/1931
import sys
sys.stdin = open("input.txt", "r")
n=int(sys.stdin.readline())
times=[list(map(int, sys.stdin.readline().split())) for i in range(0,n) ]
reserve=list([False]*(max(sum(times, []))+2))
cnt=0

for time in times:
    available=0
    for t in range(time[0],time[1]):
        if reserve[t] != True:
            available+=1
        else:
            continue
    if available == (time[1]-time[0]):
        if time[0]==time[1]:
            if reserve[time[0]]==False:
                cnt+=1
        else:
            cnt+=1
            for t in range(time[0], time[1]):
                reserve[t]=True

print(cnt)
