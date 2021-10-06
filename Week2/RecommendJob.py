# 4주차 직업군 추천하기 : https://programmers.co.kr/learn/courses/30/lessons/84325
def solution(table, languages, preference):
    answer = ''
    
    #점수와 직업군 dictionary 만들기
    score_list=list(range(6,0,-1))
    total_list=list()
    for line in table:
        temp=line.split(' ')
        temp_dict={}
        for i in range(0,len(temp)):
            if i==0:
                temp_dict={'직업군':temp[i]}
            else:
                temp_dict[temp[i]]=score_list[i]
        total_list.append(temp_dict)
        
    #언어별 점수 dictionary 만들기
    prefer_dict={}
    for i, lan in enumerate(languages):
        prefer_dict[lan]= preference[i]
    # print(prefer_dict)
    
    #더하기
    scores={}
    for tdict in total_list:
        temp=0
        for lan in languages:
            # print('lan',lan)
            # print("tdict.get(lan)",tdict.get(lan))
            if lan in tdict:
                temp+=tdict.get(lan)*prefer_dict.get(lan)
        scores[tdict['직업군']]=temp
        
    #가장 큰 값
    max_val=(max(scores.values()))
    pre_answer=list()
    for key in scores:
        if scores.get(key)==max_val:
            pre_answer.append(key)
    
    print(pre_answer)
    pre_answer_ord=list()
    for a in pre_answer:
        pre_answer_ord.append(ord(a[0]))
    # print(min(pre_answer_ord))
    answer=pre_answer[pre_answer_ord.index(min(pre_answer_ord))]
    return answer
