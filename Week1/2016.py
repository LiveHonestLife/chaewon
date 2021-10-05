def solution(a, b):
    # answer=''
    total=cal_prev(a,b)
    day=total%7
    print(day)

    if day==0:
        answer=days[4]
    elif day==1:
        answer=days[5]
    elif day==2:
        answer=days[6]
    elif day==3:
        answer=days[0]
    elif day==4:
        answer=days[1]
    elif day==5:
        answer=days[2]
    elif day==6:
        answer=days[3]
    print(answer)
    return answer

days=['SUN','MON','TUE','WED','THU','FRI','SAT']
#5부터 시작
monthes=[31,29,31,30,31,30,31,31,30,31,30,31]

def cal_prev(a,b):
    temp=0
    for i in range(0,a-1):
        temp+=monthes[i]
    temp+=b
    return temp
solution(1,3)
