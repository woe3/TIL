def solution(today, terms, privacies):
    answer = []
    terms_dic = {}
    
    # terms를 딕셔너리 형태로 변환 시킨다. 예) {"A" : 10}
    for term in terms:
        term = list(term.split())
        terms_dic[term[0]] = int(term[1])
    
    # 각 사용자에 대한 유효기간 판별
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        date = list(map(int, date.split(".")))
        term_num = terms_dic[term]
        date[1] += term_num
        date[2] -= 1
        if date[2] < 1:
            date[2] = 28
            date[1] -= 1
        if date[1] > 12:
            date[0] += (date[1]-1)//12
            date[1] = (date[1]-1)%12+1
            
            
        # 마지막 date를 스트링으로 변환
        date = list(map(str, date))
        for k in range(1,3):
            if len(date[k]) < 2:
                date[k] = "0" + date[k]
        date = ".".join(date)
        
        if date < today:
            answer.append(i+1)
        
        
        
    return answer