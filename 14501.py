n = int(input())
food = list(map(int, input().split(" ")))

size = [0]*101
size[0] = food[0]
size[1] = max(food[1], food[0])

for i in range(2, len(food)):
    size[i] = max(size[i-1], size[i-2] + food[i])

print(size[len(food)-1])