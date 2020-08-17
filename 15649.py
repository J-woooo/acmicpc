n, m = map(int, input().split(" "))


def process(tmp_store, tmp_value):
    if len(tmp_value) == m:
        result = ''
        for c in tmp_value:
            result += (c + ' ')
        print(result)
        return

    for i in range(0, n):
        if tmp_store[i] == 0:
            tmp_store[i] = 1
            process(tmp_store, tmp_value + str(i+1))
            tmp_store[i] = 0


for i in range(0, n):
    store = [0 for i in range(n)]
    store[i] = 1
    value = str(i+1)
    process(store, value)
