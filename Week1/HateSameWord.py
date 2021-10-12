# 같은 숫자는 싫어 : https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer=[]
    answer.append(arr[0])
    make_stack(arr,answer)

    return answer

def make_stack(arr,answer):
    stack=0
    for i in range(1, len(arr)):
        prev=arr[i-1]
        now=arr[i]
        if prev==now:
            stack+=1
        else:
            stack=0

        if stack==0:
            answer.append(arr[i])
