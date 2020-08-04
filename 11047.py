def greedy(coin, sum):
    length = len(coin)
    count = 0
    i = length-1
    while(sum!=0):
        count += sum//coin[i]
        sum %= coin[i]
        i-=1
    return count

coin_num, sum = input().split(" ")

coin = []

for i in range(int(coin_num)):
    money = int(input())
    coin.append(int(money))
print(greedy(coin, int(sum)))
