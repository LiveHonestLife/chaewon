# [카카오 인턴] 키패드 누르기 : https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    keypad={1:[0,0],2:[0,1],3:[0,2],
           4:[1,0], 5:[1,1],6:[1,2],
           7:[2,0], 8:[2,1],9:[2,2],
                   0:[3,1]}
    lh=[3,0]
    rh=[3,2]

    for i, num in enumerate(numbers):
        if num == 1 or num == 4 or num==7:
            numbers[i] = 'L'
            lh=keypad[num]
            continue
        if num ==3 or num==6 or num==9:
            numbers[i]= 'R'
            rh=keypad[num]
            continue
            
        purpose=keypad[num]
        l_value= abs(purpose[0]-lh[0]) + abs(purpose[1]-lh[1])
        r_value= abs(purpose[0]-rh[0]) + abs(purpose[1]-rh[1])
        
        if r_value== l_value:
            numbers[i]=hand[0].upper()
            if numbers[i] == 'R':
                rh=keypad[num]
            elif numbers[i] == 'L':
                lh=keypad[num]
        elif r_value<l_value:
            numbers[i]= 'R'
            rh=keypad[num]
        elif l_value<r_value:
            numbers[i]= 'L'
            lh=keypad[num]

    answer=str("".join(numbers))
    # print(answer)
    return answer
