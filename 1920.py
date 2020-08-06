def isList(n, m, start, end):
    mid = (start+end)//2
    if(n[mid] == m):
        return 1
    elif(start == mid):
        return 0
    elif(n[mid] > m):
        return isList(n, m, start, mid)
    elif(n[mid] < m):
        return isList(n, m, mid, end)


n_size = int(input())
n = list(map(int, input().split(" ")))
m_size = int(input())
m = list(map(int, input().split(" ")))


n.sort()
result = []
for i in range(m_size):
    result.append(isList(n, m[i], 0, n_size))

for r in result:
    print(r)
