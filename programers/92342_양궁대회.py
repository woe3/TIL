from itertools import permutations


def point_cal(A, R):
    point = 0
    for i in range(10):
        if R[i] == 0 and A[i] == 0:
            pass
        elif R[i] > A[i]:
            point += (10-i)
        else: point -= (10-i)
    return point


def solution(n, info):
    answer = []
    R = [0] * 10
    point_index = []
    max_point = 0
    
    
    for i in range(10):
        if info[i] > 0:
            point_index.append(i)
    
    perm_list = permutations(point_index)
        
    for j in perm_list:
        for i in j:
            while R[i] <= info[i] and n > 0:
                n -= 1
                R[i] += 1
                if n == 0:
                    break
        if n > 0:
                   
        
    print(R)
    
    print(point_cal(info, R))
    return answer