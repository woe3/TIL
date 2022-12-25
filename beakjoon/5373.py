import sys
from collections import deque
def it_self_1(list_t,x):
    temp = deque()
    temp.append(list_t[1])
    temp.append(list_t[2])
    temp.append(list_t[3])
    temp.append(list_t[6])
    temp.append(list_t[9])
    temp.append(list_t[8])
    temp.append(list_t[7])
    temp.append(list_t[4])
    if x == '-':
        list_t[3] = temp.popleft()
        list_t[6] = temp.popleft()
        list_t[9] = temp.popleft()
        list_t[8] = temp.popleft()
        list_t[7] = temp.popleft()
        list_t[4] = temp.popleft()
        list_t[1] = temp.popleft()
        list_t[2] = temp.popleft()
    else:
        list_t[7] = temp.popleft()
        list_t[4] = temp.popleft()
        list_t[1] = temp.popleft()
        list_t[2] = temp.popleft()
        list_t[3] = temp.popleft()
        list_t[6] = temp.popleft()
        list_t[9] = temp.popleft()
        list_t[8] = temp.popleft()  

def it_self_2(list_t,x):
    temp = deque()
    temp.append(list_t[1])
    temp.append(list_t[2])
    temp.append(list_t[3])
    temp.append(list_t[6])
    temp.append(list_t[9])
    temp.append(list_t[8])
    temp.append(list_t[7])
    temp.append(list_t[4])
    if x == '+':
        list_t[3] = temp.popleft()
        list_t[6] = temp.popleft()
        list_t[9] = temp.popleft()
        list_t[8] = temp.popleft()
        list_t[7] = temp.popleft()
        list_t[4] = temp.popleft()
        list_t[1] = temp.popleft()
        list_t[2] = temp.popleft()
    else:
        list_t[7] = temp.popleft()
        list_t[4] = temp.popleft()
        list_t[1] = temp.popleft()
        list_t[2] = temp.popleft()
        list_t[3] = temp.popleft()
        list_t[6] = temp.popleft()
        list_t[9] = temp.popleft()
        list_t[8] = temp.popleft()
        
def access (list_t):
    global temp_list
    side = list_t[0]
    if side == "U":
        for i in range(1,4):
            temp_list.append(U[list_t[i]])
    elif side == "D":
        for i in range(1,4):
            temp_list.append(D[list_t[i]])
    elif side == "F":
        for i in range(1,4):
            temp_list.append(F[list_t[i]])
    elif side == "B":
        for i in range(1,4):
            temp_list.append(B[list_t[i]])
    elif side == "L":
        for i in range(1,4):
            temp_list.append(L[list_t[i]])
    elif side == "R":
        for i in range(1,4):
            temp_list.append(R[list_t[i]])
    return
    
def change (list_t):
    global temp_list

    side = list_t[0]
    if side == "U":
        for i in range(1,4):
            U[list_t[i]] = temp_list.popleft()
    elif side == "D":
        for i in range(1,4):
            D[list_t[i]] = temp_list.popleft()
    elif side == "F":
        for i in range(1,4):
            F[list_t[i]] = temp_list.popleft()
    elif side == "B":
        for i in range(1,4):
            B[list_t[i]] = temp_list.popleft()
    elif side == "L":
        for i in range(1,4):
            L[list_t[i]] = temp_list.popleft()
    elif side == "R":
        for i in range(1,4):
            R[list_t[i]] = temp_list.popleft()
    return

def turn(v):
    global temp_list
    
    if v[0] == "U":
        it_self_2(U,v[1])
        for i in U_t:
            access(i)
        if v[1] == "+":
            for _ in range(3):
                temp_list.append(temp_list.popleft())
        else:
            for _ in range(3):
                temp_list.appendleft(temp_list.pop())
        
        for i in U_t:
            change(i)
            
    elif v[0] == "D":
        it_self_1(D,v[1])
        for i in D_t:
            access(i)
        if v[1] == "+":
            for _ in range(3):
                temp_list.append(temp_list.popleft())
        else:
            for _ in range(3):
                temp_list.appendleft(temp_list.pop())
        
        for i in D_t:
            change(i)
            
    elif v[0] == "F":
        it_self_2(F,v[1])
        for i in F_t:
            access(i)
        if v[1] == "+":
            for _ in range(3):
                temp_list.append(temp_list.popleft())
        else:
            for _ in range(3):
                temp_list.appendleft(temp_list.pop())
        
        for i in F_t:
            change(i)
            
    elif v[0] == "B":
        it_self_1(B,v[1])
        for i in B_t:
            access(i)
        if v[1] == "+":
            for _ in range(3):
                temp_list.append(temp_list.popleft())
        else:
            for _ in range(3):
                temp_list.appendleft(temp_list.pop())
        
        for i in B_t:
            change(i)
            
    elif v[0] == "L":
        it_self_1(L,v[1])
        for i in L_t:
            access(i)
        if v[1] == "+":
            for _ in range(3):
                temp_list.append(temp_list.popleft())
        else:
            for _ in range(3):
                temp_list.appendleft(temp_list.pop())
        for i in L_t:
            change(i)
            
    elif v[0] == "R":
        it_self_2(R,v[1])
        for i in R_t:
            access(i)
        if v[1] == "+":
            for _ in range(3):
                temp_list.append(temp_list.popleft())
        else:
            for _ in range(3):
                temp_list.appendleft(temp_list.pop())
        
        for i in R_t:
            change(i)
            
case = int(sys.stdin.readline())
answer = []

for _ in range(case):
    n = int(sys.stdin.readline())
    direction = list(sys.stdin.readline().split())

    U = [0,"w", "w", "w",
    "w", "w", "w",
    "w", "w", "w"
    ]
    D = [0,"y", "y", "y",
        "y", "y", "y",
        "y", "y", "y"
        ]
    F = [0,"r", "r", "r",
        "r", "r", "r",
        "r", "r", "r"
        ]
    B = [0,"o", "o", "o",
        "o", "o", "o",
        "o", "o", "o"
        ]
    L = [0,"g", "g", "g",
        "g", "g", "g",
        "g", "g", "g",
        ]
    R = [0,"b", "b", "b",
        "b", "b", "b",
        "b", "b", "b"
        ]

    U_t = [["F",1,2,3],
        ["R",1,2,3],
        ["B",3,2,1],
        ["L",3,2,1]]

    D_t = [["F",9,8,7],
        ["L",7,8,9],
        ["B",9,8,7],
        ["R",9,8,7]
        ]

    F_t = [["U",9,8,7],
        ["L",1,4,7],
        ["D",7,8,9],
        ["R",7,4,1]]

    B_t = [["U",1,2,3],
        ["R",3,6,9],
        ["D",3,2,1],
        ["L",9,6,3]]

    L_t = [["U",7,4,1],
        ["B",1,4,7],
        ["D",1,4,7],
        ["F",7,4,1]]

    R_t = [["U",3,6,9],
        ["F",3,6,9],
        ["D",9,6,3],
        ["B",9,6,3]]

    for k in range(n):
        temp_list = deque()
        turn(direction[k])
        print(U)
        print(D)
        print(F)
        print(B)
        print(L)
        print(R)
        print()
    for j in range(1,10,3):
        temp_answer = str(U[j]) + str(U[j+1]) + str(U[j+2])
        answer.append(temp_answer)
    
for i in answer:
    print(i)