from itertools import product
def solution(relation):
    answer = 0
    answer_set = set()
    case_index_list = []
    # 후보키가 될 수 있는 모든 경우의 수 (1은 +-     )
    cases = list(product((0,1), repeat=len(relation[0])))[1:]
    
    # 경우의 수를 인덱스 형식으로 변환 후, 길이가 작은 순대로 정렬
    for case in cases:
        temp_case = []
        for i in range(len(case)):
            if case[i]:
                temp_case.append(i)
        case_index_list.append(temp_case)    
    case_index_list.sort(key = len)
    
    # 이미 추가된 정답set을 통해 최소성 검증
    # !추가: 차집합을 이용해서 공집합인지 아닌지만 확인하면 됨
    for l in range(len(cases)):
        case_temp = tuple(case_index_list[l])
        min = True
        for x in answer_set:
            cnt = 0
            for y in x:
                if y in case_temp:
                    cnt += 1
            if cnt == len(x):
                min = False
                break
        if not min:
            continue
        
        # 유일성 검증
        temp_set = set()
        determine_key = True
               
        for r in relation:
            temp_list = []
            for c in case_temp:
                temp_list.append(r[c])
            temp_list = tuple(temp_list)
            if not temp_list in temp_set:
                temp_set.add(temp_list)
            else:
                determine_key = False
                break
        if determine_key:
            answer_set.add(case_temp)
            answer += 1

    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))