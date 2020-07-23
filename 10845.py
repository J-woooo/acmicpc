
queue = []
result = []
global front
global back
front = 0
back = -1
def startQueue(command):
    global front
    global back
    if(command[0] == 'push'): # 정수를 큐에 넣는다        
        back+=1
        queue.append(command[1])
    elif(command[0]=='pop'): # 가장 앞에 있는 정수를 빼고, 그 수를 출력, 정수가 없으면 -1 출력
        if(front>back):
            result.append(-1)
        else:
            result.append(queue[front])
            front+=1
    elif(command[0]=='size'):
        result.append(back-front+1)
    elif(command[0]=='empty'):
        if(front>back):
            result.append(1)
        else:
            result.append(0)
    elif(command[0]=='front'):
        if(front>back):
            result.append(-1)
        else:
            result.append(queue[front])
    elif(command[0]=='back'):
        if(front>back):
            result.append(-1)
        else:
            result.append(queue[back])


num = int(input())
for i in range(num):
    command = input().split()
    startQueue(command)
    # print(result)
for r in result:
    print(r)