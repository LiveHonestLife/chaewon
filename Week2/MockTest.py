# 모의고사 : https://programmers.co.kr/learn/courses/30/lessons/42840 
def solution(answers):
    answer = []
    
    a1=[1,2,3,4,5]*2000
    a2=[2, 1, 2, 3, 2, 4, 2, 5]*1250
    a3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    
    correct1=[ans for i,ans in enumerate(answers) if ans==a1[i]]
    correct2=[ans for i,ans in enumerate(answers) if ans==a2[i]] 
    correct3=[ans for i,ans in enumerate(answers) if ans==a3[i]] 

    len_list=[len(correct1), len(correct2),len(correct3)]
    len_max=max(len_list)

    answer=[i+1 for i in range(0,len(len_list)) if len_max==len_list[i] ]
    # for i in range(0,len(len_list)):
    #     if len_max==len_list[i]:
    #         answer.append(i+1)
            
    return answer
