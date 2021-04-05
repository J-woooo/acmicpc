import sys
input = sys.stdin.readline

n = int(input())
studentList = list(map(int, input().split(" ")))
b, c = map(int, input().split(" "))
result = n
# for i in range(n):
#     studentList[i] -= b
#     if studentList[i] <= 0:
#         continue
#     elif not studentList[i] == 0:
#         if studentList[i] % c == 0:
#             result += (studentList[i] // c)
#         else:
#             result += (studentList[i] // c) + 1
for num in studentList:
    num -= b
    if num <= 0:
        continue
    result += num // c if num % c == 0 else num // c + 1

print(result)