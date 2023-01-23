
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
    if n > 0:
        term += " and "
    for i in terms_list[n]:
        querys(n+1, term+i)
        
            


def solution(info, query):
    answer = []
    global dictionaryOfQuerys
    # 딕셔너리 만들기 지원자 정보를 key로 점수를 리스트 형태의 value로 만들어서 추가
    # ex) 'pythonfrontendseniorchicken': ['210', '150']
    querys()
    print(dictionaryOfQuerys)
    
    
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","cpp backend senior pizza 280","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))