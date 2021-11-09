def solution(name):
    answer = 0
    # ['A', 'A', 'B', 'C', 'D', 'E', 'F' ... ] 만들기
    alphabet = "ABCDEFGHIJKLMNOPQRSTVUWXYZ"

    # cost=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 만들기
    cost = [0] * len(alphabet)
    right = 0
    left = 0
    for i in range(0, len(alphabet) // 2 + 1):
        cost[right] = i
        cost[left] = i
        right += 1
        left -= 1

    # 이미 A인 것을 True로 만들기
    complete = [False] * len(name)
    for i, a in enumerate(name):
        if a == "A":
            complete[i] = True
    # [False, True, False]

    now = 0  # 현재 커서 위치
    while False in complete:
        # False인 위치로 이동
        right = now
        left = now
        right_True = 0
        left_True = 0
        for i in range(0, len(name) // 2 + 1):
            if (complete[right] == False) and (complete[left] == False):
                now = right
                break
            elif (complete[right] == True) and (complete[left] == False):
                now = left
                break
            elif (complete[right] == False) and (complete[left] == True):
                now = right
                break
            else:
                right += 1
                left -= 1
                answer += 1
        # 이제 now는 고쳐야 할 index
        print('now', now)

        # 원하는 문자로 만들기
        print("cost", cost[alphabet.index(name[now])])
        answer += cost[alphabet.index(name[now])]
        complete[now] = True
    answers = []
    answers.append(answer)
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
    answer = 0
    # 이미 A인 것을 True로 만들기
    complete = [False] * len(name)
    for i, a in enumerate(name):
        if a == "A":
            complete[i] = True
    # [False, True, False]

    now = 0  # 현재 커서 위치
    while False in complete:
        # False인 위치로 이동
        right = now
        left = now
        right_True = 0
        left_True = 0
        for i in range(0, len(name) // 2 + 1):
            if (complete[right] == False) and (complete[left] == False):
                now = left
                break
            elif (complete[right] == True) and (complete[left] == False):
                now = left
                break
            elif (complete[right] == False) and (complete[left] == True):
                now = right
                break
            else:
                right += 1
                left -= 1
                answer += 1
        # 이제 now는 고쳐야 할 index
        print('now', now)

        # 원하는 문자로 만들기
        print("cost", cost[alphabet.index(name[now])])
        answer += cost[alphabet.index(name[now])]
        complete[now] = True

    answers.append(answer)
    print(answers)
    return min(answers)
