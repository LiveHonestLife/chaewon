# 두 정수 사이의 합 : https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    if a>b:
        temp=b
        b=a
        a=temp
    answer=0
    for i in range(a,b+1):
        answer+=i
    return answer
