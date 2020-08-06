def isNum(n):
    if(n == "0" or n == "1" or n == "2" or n == "3" or n == "4" or n == "5" or n == "6" or n == "7" or n == "8" or n == "9"):
        return True
    else:
        return False


inputNum, dec = input().split(" ")
dec = int(dec)
result = 0
for i in range(len(inputNum)):
    if isNum(inputNum[i]):
        # print("type1", int(inputNum[i]), int(inputNum[i])*dec**(len(inputNum)-1-i))
        result += (int(inputNum[i])*dec**(len(inputNum)-1-i))
    else:
        # print("type2", (ord(inputNum[i])-55), (ord(inputNum[i])-55)*dec**(len(inputNum)-1-i))
        result += ((ord(inputNum[i])-55)*dec**(len(inputNum)-1-i))
print(result)
