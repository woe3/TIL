def solution(str1, str2):
    answer = 0
    strings = ["", ""]
    # 변수 1,2 모두 소문자로 만들기
    strings[0] = str1.lower()
    strings[1] = str2.lower()
    string_dic = [{}, {}]
    string_length = 0
    # 알파벳이 아닌 다른 글자를 빼고 2개씩 역어서 딕셔너리에 추가
    # 중복된 글자가 나오면 딕셔너리의 value를 증가
    # 추가 될때마다 전체 길이(string_length)를 ++
    for i in range(2):
        for l in range(len(strings[i]) - 1):
            if not strings[i][l].isalpha():
                continue
            if not strings[i][l + 1].isalpha():
                continue
            string_length += 1
            new_string = strings[i][l] + strings[i][l + 1]
            if new_string in string_dic[i]:
                string_dic[i][new_string] += 1
            else:
                string_dic[i][new_string] = 1
    intersection = 0
    # 딕셔너리를 모두 돌면서 있는지 확인해서 교집합의 개수 확인
    for i in string_dic[0]:
        while string_dic[0][i]:
            string_dic[0][i] -= 1
            if i in string_dic[1]:
                if string_dic[1][i]:
                    string_dic[1][i] -= 1
                    intersection += 1

    # 합집합 = (전체 길이 - 교집합)
    union = string_length - intersection

    # 조건에 따라 다른 출력
    # 정수 값만 출력하기 위해 int()사용
    if (not union) and (not intersection):
        return 65536
    elif not intersection:
        return 0
    return int((intersection / union) * 65536)


print(solution("aa1+aa2", "AAAA12"))
