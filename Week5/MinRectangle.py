# 최소직사각형 : https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    width=[]
    height=[]
    # [0]에 둘 중 큰 길이가 들어가도록 정렬
    for size in sizes:
        if size[0] <size[1]:
            tmp=size[0]
            size[0]=size[1]
            size[1]=tmp
        width.append(size[0])
        height.append(size[1])

    return max(width)*max(height)
