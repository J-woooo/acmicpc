
num, size = map(int, input().split(" "))
# num, size = 7, 3
numDic = {}
for i in range(1, num+1):
    numDic[i] = False

exit = 0
count = 0
i = 1
result = []
while(exit != num):
    if(numDic[i] == False):
        count += 1
        if count == size:
            numDic[i] = True
            exit += 1
            count = 0
            result.append(i)
        else:  # count != size
            i += 1
            if i > num:
                i %= num
    else:
        i += 1
        if i > num:
            i %= num
r = "<"
r += str(result)[1:len(str(result))-1]
r += ">"
print(r)
