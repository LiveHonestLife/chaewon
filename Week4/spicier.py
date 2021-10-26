# 더 맵게 : https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq
def solution(scoville, K):
    if sum(scoville)==0:
        return -1
    
    heapq.heapify(scoville)
    # sort한 것 처럼 정렬됨
    
    cnt=0
    while scoville[0]<K:
        temp=heapq.heappop(scoville)+heapq.heappop(scoville)*2
        
        # 왜 이건 틀릴까
        # temp=scoville[0]+scoville[1]*2
        # heapq.heappop(scoville)
        # heapq.heappop(scoville)
        
        heapq.heappush(scoville, temp)
        cnt+=1
        
        if len(scoville)<=1:
            if scoville[0]<K:
                cnt=-1
            break
    return cnt
