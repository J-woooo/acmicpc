# 10진법을 n진법으로 변환

num_dic = {
    1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
    6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
    11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
    16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K',
    21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P',
    26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U',
    31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'
}


def find_digit(num, n):
    digit = 0
    while(num >= n**digit):
        digit += 1
    return (digit-1)


def make_digit(dec_num, digit, n):  # 10진수숫자, 최대자리, 진수
    result = ""
    for i in range(digit, -1, -1):
        if dec_num >= n**i:
            key = dec_num // (n**i)
            # print("추가", dec_num,  n**i, key)
            result += num_dic[key]
            dec_num -= (n**i * key)
        else:
            # print("스킵", dec_num, n**i)
            result += "0"
    return result


dec_num, n = map(int, input().split(" "))
digit = find_digit(dec_num, n)
# print("digit", digit)
print(make_digit(dec_num, digit, n))
