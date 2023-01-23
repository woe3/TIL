from itertools import product
import bisect
dictionaryOfQuerys = {}
def querys(n = 0, term = ""):
    global dictionaryOfquery
    if n == 4:
        dictionaryOfQuerys[term] = []
        return
    terms_list = [
        ["cpp", "java", "python", "-"],
        ["backend", "frontend", "-"],
        ["junior", "senior", "-"],
        ["chicken", "pizza", "-"]
    ]
    # if n > 0:
    #     term += " and "
    for i in terms_list[n]:
        querys(n+1, term+i)
        
def info_input(info : list, n = 0):
    if n == 4:
        dictionaryOfQuerys["".join(info[:4])].append(int(info[4]))
        return
    info_input(info, n+1)
    info_input(info[:n] + ["-"] + info[n+1:], n+1)

def solution(info, query):
    answer = []
    global dictionaryOfQuerys
    # 딕셔너리 만들기 지원자 정보를 key로 점수를 리스트 형태의 value로 만들어서 추가
    # ex) 'pythonfrontendseniorchicken': ['210', '150']
    querys()
    for i in info:
        temp = list(i.split())
        info_input(temp)
    for i in dictionaryOfQuerys:
        dictionaryOfQuerys[i].sort()
    
    for i in query:
        temp = list(i.split())
        temp_q = []
        for j in temp:
            if j != "and":
                temp_q.append(j)
        query_key = "".join(temp_q[:4])
        score = int(temp_q[4])
        answer.append(len(dictionaryOfQuerys[query_key]) - 
                      bisect.bisect_left(dictionaryOfQuerys[query_key], score))
        
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))