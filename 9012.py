t = int(input())
result = []
for _ in range(t):
    open_cnt = 0

    for vps_str in input():
        if vps_str == "(":
            open_cnt += 1
        elif vps_str == ")":
            open_cnt -= 1
            if open_cnt < 0:
                break
    if open_cnt == 0:
        result.append("YES")
    else:
        result.append("NO")
for r in result:
    print(r)
