str0 = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
str1 = "\"재귀함수가 뭔가요?\""
str2 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
str3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
str4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
str5 = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
str6 = "라고 답변하였지."
bar = "____"


def recur(count, now):
    now_bar = now*bar
    print(now_bar+str1)
    if(now < count):
        print(now_bar+str2)
        print(now_bar+str3)
        print(now_bar+str4)
        recur(count, now+1)
    elif(now == count):
        print(now_bar+str5)
    print(now_bar+str6)


count = input()
print(str0)
recur(int(count),0)
