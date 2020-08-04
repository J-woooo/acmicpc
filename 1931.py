
def find(conference):
    count = 0
    start = 0
    for time in conference:
        if(time[0] >= start):
            start = time[1]
            count += 1
    return count


conNum = int(input())
conference = []

for i in range(conNum):
    start, end = input().split(" ")
    start = int(start)
    end = int(end)
    conf = (start, end)
    conference.append(conf)

conference = sorted(conference, key=lambda time: time[0])
conference = sorted(conference, key=lambda time: time[1])
print(find(conference))
