import sys
n = int(sys.stdin.readline())
paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))
answer = [0, 0, 0]

def paper_cut(paper, n):
    global answer
    number = paper[0][0]
    for i in range(n):
        for j in range(n):
            if paper[i][j] != number:
                paper_1 = []
                paper_2 = []
                paper_3 = []
                paper_4 = []
                paper_5 = []
                paper_6 = []
                paper_7 = []
                paper_8 = []
                paper_9 = []
                for k in range(n):
                    if k < n//3:
                        paper_1.append(paper[k][0:n//3])
                        paper_2.append(paper[k][n//3:2*n//3])
                        paper_3.append(paper[k][2*n//3:n])
                    elif k < 2*n//3:
                        paper_4.append(paper[k][0:n//3])
                        paper_5.append(paper[k][n//3:2*n//3])
                        paper_6.append(paper[k][2*n//3:n])
                    else:
                        paper_7.append(paper[k][0:n//3])
                        paper_8.append(paper[k][n//3:2*n//3])
                        paper_9.append(paper[k][2*n//3:n])
                paper_cut(paper_1, n//3)
                paper_cut(paper_2, n//3)
                paper_cut(paper_3, n//3)
                paper_cut(paper_4, n//3)
                paper_cut(paper_5, n//3)
                paper_cut(paper_6, n//3)
                paper_cut(paper_7, n//3)
                paper_cut(paper_8, n//3)
                paper_cut(paper_9, n//3)
                return
    answer[number] += 1
    return

paper_cut(paper, n)
print(answer[-1])
print(answer[0])
print(answer[1])