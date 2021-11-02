# 다리를 지나는 트럭 : https://programmers.co.kr/learn/courses/30/lessons/42583

import collections
def solution(bridge_length, weight, truck_weights):
    time = 0
    current_weight=0
    arrive_trucks=list()
    truck_weights_len=len(truck_weights)
    
    bridge=collections.deque([0]*bridge_length,maxlen=bridge_length)
    
    while len(arrive_trucks)<truck_weights_len:
        #한 칸씩 옮기기    
        arrive=bridge.popleft()
        current_weight= current_weight - arrive
        if arrive != 0:
            arrive_trucks.append(arrive)
        
        #다리 위에 올리기
        if len(truck_weights)>0:
            if bridge_length>len(bridge) and (truck_weights[0]+current_weight)<=weight:
                print(truck_weights[0])
                bridge.extend( [ truck_weights[0] ] )
                current_weight+=truck_weights[0]
                del truck_weights[0]
            else:
                bridge.extend([0])
                
        time+=1
    return time
