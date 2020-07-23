global index
index=-1
stack = []
result = []
def push(stack,num):
    global index
    index+=1
    stack.append(num)

def pop(stack):
    global index
    if(empty(stack)):
        return -1
    else:
        index-=1
        return stack.pop()

def size(stack):
    global index
    return (index+1)

def empty(stack):
    global index
    if(index == -1): return 1
    else: 
        return 0

def top(stack):
    global index
    if(index == -1): return -1
    else:
        return stack[index]

def process_stack(command):

    if(command[0] == "push"):
        push(stack,command[1])
        pass
    elif(command[0] == "pop"):
        result.append(pop(stack))
        pass
    elif(command[0] == "size"):
        result.append((size(stack)))
        pass
    elif(command[0] == "empty"):
        result.append((empty(stack)))
        pass
    elif(command[0] == "top"):
        result.append((top(stack)))
        pass
    else:
        print("Input Error")

n = int(input())
for i in range(n):
    command = input().split(" ")
    process_stack(command)
for r in result:
    print(r)