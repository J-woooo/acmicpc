def sol(n):
    num = 1
    while(num<n):
        num*=2
    return n*2-num

n = input("")
print(sol(int(n)))