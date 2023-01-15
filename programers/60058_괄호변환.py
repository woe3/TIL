# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
# 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.  
def split_p(w):
    cnt = 0
    u = ''
    v = ''
    for i in range(len(w)):
        if w[i] == "(":
            u += "("
            cnt += 1
        else:
            u += ")"
            cnt -= 1
        if cnt == 0:
            v = w[i+1:]
            return(u, v)
        
def determine_p(u):
    cnt = 0
    for bracket in u:
        if bracket == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
        else:
            return True

def recursive(v, u=''):

    if not v:
        return u
    cnt = 0
    temp_u = ''
    for i in range(len(v)):
        if v[i] == "(":
            temp_u += "("
            cnt += 1
        else:
            temp_u += ")"
            cnt -= 1
        if cnt == 0:
            v = v[i+1:]
            break
    if determine_p(temp_u):
        return recursive(v, u + temp_u)
    else:
        print(temp_u)
        temp ='('
        temp += recursive(v)
        temp += ')'
        reverse_u = ''
        for index_num in range(1,len(temp_u)-1):
            if temp_u[index_num] == '(':
                reverse_u += ')'
            else:
                reverse_u += '('
        print(reverse_u)
        return u + temp + reverse_u
        
            
            
def solution(p):
    answer = recursive(p)
    
    
    
    return answer

print(solution("()))((()"))