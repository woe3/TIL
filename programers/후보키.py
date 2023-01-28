from itertools import product
def solution(relation):
    answer = 0
    answer_set = set()
    case_index_list = []
    cases = list(product((0,1), repeat=len(relation[0])))[1:]
    for case in cases:
        temp_case = []
        for i in range(len(case)):
            if case[i]:
                temp_case.append(i)
        case_index_list.append(temp_case)    
    case_index_list.sort(key = len)
    for l in range(len(cases)):
        case_temp = tuple(case_index_list[l])
        d = True
        for x in answer_set:
            for y in x:
                if y in case_temp:
                    d= False
                    break
            if not d:
                break
        if not d:
            continue
        
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