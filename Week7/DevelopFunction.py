# 기능개발 : https://programmers.co.kr/learn/courses/30/lessons/42586

import collections
def solution(progresses, speeds):
    answer = []
    progresses=collections.deque(progresses)
    speeds=collections.deque(speeds)
    while speeds:
        #일을 한다
        for i in range(0,len(speeds)):
            sp=speeds.popleft()
            progresses.append(progresses.popleft()+sp)
            speeds.append(sp)

        #100이상인 것 갯수 세기
        cnt=0
        while True:
            #if 안 넣으면 error:더 이상 pop할 것이 없어서
            if progresses:
                check=progresses.popleft()
            else:
                break
                
            if  check>=100:
                cnt+=1
                speeds.popleft()
            else:
                progresses.appendleft(check)
                break        
        #갯수 추가
        if cnt!=0:
            answer.append(cnt)
            
    return answer
