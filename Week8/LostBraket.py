# 미해결
# 잃어버린 괄호 https://www.acmicpc.net/problem/1541
# 파싱은 했으나 방법이 전혀 떠오르지 않음

import sys

sys.stdin = open("input.txt", "r")
original = sys.stdin.readline()
print(original)
x = original.split('-')
x = [xx.split('+') for xx in x]
x = sum(x, [])
x = list(map(int, x))
# print(x)
op = []
for i, o in enumerate(original):
    if '-' == o:
        op.append('-')
    if '+' == o:
        op.append('+')

for i in range(0, len(op)):
    x.insert((i + 1) * 2 - 1, op[i])

x = map(str, x)
print(eval("".join(x)))
