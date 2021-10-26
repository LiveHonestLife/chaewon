# 로또의 최고 순위와 최저 순위 : https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = [0,0]
    
    cnt=0
    zero_cnt=0
    
    for i, num in enumerate(win_nums):
        if num in lottos:
            cnt+=1
        if lottos[i]==0:
            zero_cnt+=1
            
    rank=[6,6,5,4,3,2,1]
    
    answer[0]=rank[zero_cnt+cnt]
    answer[1]=rank[cnt]
    return answer
