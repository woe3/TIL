from itertools import combinations

def solution(orders, course):
    answer_temp = [[] for _ in range(course[-1]+1)]
    checked_list = []
    length = len(orders)
    course_max = [0] * (course[-1]+1)
    for i in range(length):
        menu_1 = set(orders[i])
        for j in range(i+1, length):
            menu_2 = set(orders[j])
            menu = menu_1 & menu_2
            if len(menu) >= course[0]:
                menu = list(menu)
                for x in course:
                    if len(menu) >= x:
                        combi_list = combinations(menu, x)
                    for y in combi_list:
                        y = list(y)
                        y.sort()
                        menu_str = "".join(y)
                        if menu_str in checked_list:
                            continue
                        count = 0
                        for k in orders:
                            count_if_in = 0
                            for l in y:
                                if l in k:
                                    count_if_in += 1

                            if count_if_in == len(y):
                                count += 1

                        if count == course_max[len(y)]:
                            answer_temp[len(y)].append(menu_str)
                        elif count > course_max[len(y)]:
                            course_max[len(y)] = count
                            answer_temp[len(y)] = []
                            answer_temp[len(y)].append(menu_str)
                        checked_list.append(menu_str)
    answer = []
    for i in answer_temp:
        answer += i
    answer.sort()
    return answer