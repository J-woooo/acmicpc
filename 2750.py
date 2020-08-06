num = int(input(""))
numList = []
for i in range (0,num):
    a = int(input())
    numList.append(a)
for i in range(len(numList)):
    for j in range(i,len(numList)):
        if(numList[i]>numList[j]):
            tmp = numList[j]
            numList[j] = numList[i]
            numList[i] = tmp
for num in numList:
    print(num)
