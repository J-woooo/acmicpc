
def greedyChange(coin, money):
    count = 0
    i = 0
    while(money != 0):
        if(coin[i] <= money):
            money -= coin[i]
            count += 1
        else:
            i += 1
    return count


count = 0

coin = [500, 100, 50, 10, 5, 1]

price = int(input(""))

money = 1000-price

print(greedyChange(coin, money))
