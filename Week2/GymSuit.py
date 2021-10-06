#체육복 : https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    if len(lost) == 0:
        return n
    lost.sort()
    reserve.sort()
    answer = 0
    temp=lost.copy()
    # 여벌 체육복을 가져온 학생이 도난당한 경우
    for l in temp:
        if len(reserve) == 0:
            break
        if l in (reserve):
            reserve.remove(l)
            lost.remove(l)
            continue
    temp=lost.copy()
    for l in temp:
        if len(reserve) == 0:
            break
        minus = l - 1
        plus = l + 1
        if minus in (reserve):
            reserve.remove(minus)
            lost.remove(l)
            continue
        if plus in (reserve):
            reserve.remove(plus)
            lost.remove(l)
    answer = n - len(lost)
    return answer
