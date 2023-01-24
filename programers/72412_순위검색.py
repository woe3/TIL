from itertools import product
import bisect
dictionaryOfQuerys = {}

# 전체 경우의 수를 key:[]로 딕셔너리를 만든다.
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
    for i in terms_list[n]:
        querys(n+1, term+i)
# 지원자가 해당되는 모든 key의 value인 리스트에 점수를 추가
# ex) 'pythonfrontendseniorchicken': ['210', '150']       
def info_input(info : list, n = 0):
    if n == 4:
        dictionaryOfQuerys["".join(info[:4])].append(int(info[4]))
        return
    info_input(info, n+1)
    info_input(info[:n] + ["-"] + info[n+1:], n+1)

def solution(info, query):
    answer = []
    global dictionaryOfQuerys
    
    querys()
    for i in info:
        temp = list(i.split())
        info_input(temp)
        
    # 모든 리스트를 정렬한다.
    for i in dictionaryOfQuerys:
        dictionaryOfQuerys[i].sort()
    
    # query에 해당되는 value리스트에서 이분 탐색을 이용해서 해당 값의 인덱스를 찾는다.
    for i in query:
        temp = list(i.split())
        temp_q = []
        for j in temp:
            if j != "and":
                temp_q.append(j)
        query_key = "".join(temp_q[:4])
        score = int(temp_q[4])
        # 인덱스 값은 들어 갈수 없는 점수 중 가장 큰 점수이기 때문에
        # 전체 길이에서 인덱스를 빼준다.
        answer.append(len(dictionaryOfQuerys[query_key]) - 
                      bisect.bisect_left(dictionaryOfQuerys[query_key], score))
        
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))