def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for tree in skill_trees:
        index = []
        for i in skill:
            index.append(tree.find(i))
        print(index)
        possible = True
        for j in range(1, len(index)):
            if index[j-1] == -1 and index[j] != -1:
                possible = False
            elif index[j] != -1 and index[j-1] > index[j]:
                possible = False
        print(possible)
        if possible:
            answer += 1

    return answer

print(solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]))