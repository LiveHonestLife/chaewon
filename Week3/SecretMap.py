# [1차] 비밀지도 : https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    
    arr1=makeBinary(n,arr1)
    arr2=makeBinary(n,arr2)
    
    for row1,row2 in zip(arr1,arr2):
        row_answer=[]
        for r1,r2 in zip(row1, row2):
            if int(r1)|int(r2) ==0 :
                row_answer.append(' ')
            else:
                row_answer.append('#')
        answer.append(str("".join(row_answer)))
    print(answer)
    return answer

def makeBinary(n,arr):
    temp_arr=[]
    for num in arr:
        temp=''
        while num>=1:
            temp=str(num%2)+temp
            num=num//2
            # print(temp, num)
        temp_arr.append(temp.zfill(n))
    return temp_arr
