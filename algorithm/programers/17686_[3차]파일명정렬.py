def solution(files):
    temp_answer = []
    answer = []
    for file_index in range(len(files)):
        temp_list = [files[file_index]] + [""] * 3
        start = 1
        temp_index = 0
        
        # 파일 이름 나누기
        # HEAD
        for i in range(temp_index, len(files[file_index])):
            if files[file_index][i].isdigit():
                start += 1
                temp_index = i
                break
            temp_list[start] += files[file_index][i]
            
        # NUMBER
        for i in range(temp_index, len(files[file_index])):
            if not files[file_index][i].isdigit():
                start += 1
                temp_index = i
                break
            temp_list[start] += files[file_index][i]
            
        #TAIL
        for i in range(temp_index, len(files[file_index])):
            if files[file_index][i].isdigit():
                start += 1
                temp_index = i
                break
            temp_list[start] += files[file_index][i]
        
        # HEAD 소문자로 4번 인덱스에 추가    
        temp_list.append(temp_list[1].lower())
        # NUMBER 정수형으로 5번 인덱스에 추가
        temp_list.append(int(temp_list[2]))
        # 원래 인덱스를 6번 인덱스에 추가
        temp_list.append(file_index)
        temp_answer.append(temp_list)
    # 우선 순위 별로 정렬 (1. head, 2. 숫자크기, 3.원래 인덱스)
    temp_answer.sort(key = lambda x : (x[4], x[5], x[6]))
        
    # 0번 인덱스에는 원래의 파일명이 들어 있으므로
    # 0번 인덱스 값만 추출
    for name in temp_answer:
        answer.append(name[0])
    return answer