# 프린터 : https://programmers.co.kr/learn/courses/30/lessons/42587
import collections
def solution(priorities, location):
    answer = 0
    wait=collections.deque()
    
    # (몇번째, 우선순위) 로 덱 만들기
    for i in range(0,len(priorities)):
        wait.extend([i])
        wait.extend([priorities[i]])
    #print(wait)===>deque([0, 2, 1, 1, 2, 3, 3, 2])
    
    while len(wait)>0:
        max_pr=max(priorities)
        
        now_index=wait.popleft()
        now_pr=wait.popleft()
        
        if max_pr>now_pr: #우선순위가 작은 경우
            wait.extend([now_index])
            wait.extend([now_pr])
            continue
        elif max_pr == now_pr: #우선순위인 경우
            answer+=1     
            priorities.remove(now_pr)
            if now_index==location:
                return answer
            
    return answer
