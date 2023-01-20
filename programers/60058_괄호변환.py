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
