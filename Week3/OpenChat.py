# 오픈채팅방 : https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
def solution(record):
    answer = []
    record=[line.split(" ") for line in record]
    
    #{userid:nickname}
    user=dict()
    for line in record:
        if line[0] == "Enter" or line[0] =="Change":
            user[line[1]]=line[2]
    
    for line in record:
        if line[0] == "Enter":
            s=str(user[line[1]]+"님이 들어왔습니다.")
        elif line[0] == "Leave":
            s=str(user[line[1]]+"님이 나갔습니다.")
        elif line[0] == "Change":
            continue
        answer.append(s)
    return answer
