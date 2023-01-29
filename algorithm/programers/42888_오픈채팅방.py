def solution(record):
    answer = []
    tempAnswer = []
    userLog = {}
    
    # 마지막으로 변경된 닉네임 찾기
    for i in record:
        temp = list(i.split(" "))
        if temp[0] != "Leave":
            userLog[temp[1]] = temp[2]
        tempAnswer.append(temp)
    
    # 변경된 닉네임으로 로그 리스트 만들기
    for i in tempAnswer:
        if i[0] == "Enter":
            answer.append(userLog[i[1]] + "님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(userLog[i[1]] + "님이 나갔습니다.")
    return answer